import logging
import os
import time
import torch
from torch.nn.functional import softmax
from torchvision.models import ResNet18_Weights
from torchvision import models, transforms
import json
from PIL import Image


class HotelImageDetectionService(object):
    def __init__(self, app):
        self._logger = logging.getLogger(HotelImageDetectionService.__name__)
        self._logger.debug(f"Initialising {HotelImageDetectionService.__name__}")
        self._model = None
        self._idx_to_class = None
        self._data_folder = os.path.join(app.get_data_folder(), HotelImageDetectionService.__name__)
        if not os.path.exists(self._data_folder):
            os.makedirs(self._data_folder)

        if not os.path.exists(os.path.join(self._data_folder, 'model.pt')):
            self._logger.error(f"No model was provided. Please provide a model in {os.path.join(self._data_folder, 'model.pt')}")
            return None

        if not os.path.exists(os.path.join(self._data_folder, 'class_indices.json')):
            self._logger.error(f"No class indices were provided. Please provide them in {os.path.join(self._data_folder, 'class_indices.json')}")
            return None

        self._model_path = os.path.join(self._data_folder, 'model.pt')
        self._class_indices_path = os.path.join(self._data_folder, 'class_indices.json')

        self._load_model()
        self._logger.info(f"Initialized {HotelImageDetectionService.__name__}")

    def _load_model(self):
        """
        Loads the model used for detection.

        Returns:
            Model: The loaded PyTorch model.
        """
        start_time = time.time()

        # Load classes
        with open(self._class_indices_path, 'r') as f:
            class_to_idx = json.load(f)
        self._idx_to_class = {v: k for k, v in class_to_idx.items()}

        num_classes = len(class_to_idx)
        self._model = models.resnet18()
        num_ftrs = self._model.fc.in_features
        self._model.fc = torch.nn.Linear(num_ftrs, num_classes)

        self._model.load_state_dict(torch.load(self._model_path, map_location=torch.device('cpu'), weights_only=False))
        self._model.eval()

        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000

        self._logger.info(f"Model was loaded from {self._model_path}. Loading time: {elapsed_time_ms:.2f} ms")

    def _predict(self, transformed_image):
        start_time = time.time()
        with torch.no_grad():
            outputs = self._model(transformed_image)
            probabilities = softmax(outputs, dim=1)[0]
            all_class_probabilities = [(self._idx_to_class[idx], prob.item()) for idx, prob in enumerate(probabilities)]
            high_prob_classes = [(self._idx_to_class[idx], prob.item()) for idx, prob in enumerate(probabilities) if prob.item() > 0.5]
        end_time = time.time()
        prediction_time = (end_time - start_time) * 1000

        return high_prob_classes, all_class_probabilities, prediction_time
    
    def make_prediction(self, image_path):
        self._logger.info(f"Transforming image for detection...")
        transformed_image, transform_time = HotelImageDetectionService._transform_image(image_path)
        self._logger.info(f"Transforming image took {transform_time} ms.")
        return self._predict(transformed_image)

    @staticmethod
    def transform_image(image_path):
        start_time = time.time()

        weights = ResNet18_Weights.DEFAULT
        transformation = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=weights.transforms().mean, std=weights.transforms().std)
        ])
        image = Image.open(image_path).convert('RGB')
        transformed_image = transformation(image).unsqueeze(0)

        end_time = time.time()
        load_time_ms = (end_time - start_time) * 1000

        return transformed_image, load_time_ms
