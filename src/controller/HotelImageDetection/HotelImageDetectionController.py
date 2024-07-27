import logging
from fastapi import APIRouter, File, UploadFile
from src.service import HotelImageDetectionService, FileManagementService
from PIL import Image
from io import BytesIO


class HotelImageDetectionController (object):
    def __init__(self, app):
        self._prefix = "/hotel-image-detection"
        self._router = APIRouter()
        self._file_management = app.get_service(FileManagementService)
        self._hotel_image_detection = app.get_service(HotelImageDetectionService)
        self._logger = logging.getLogger(HotelImageDetectionController.__name__)
        self._init_routes()

    def _init_routes(self):
        """
        Initializes the routes for the hotel image detection operations.
        """
        @self._router.post(f"{self._prefix}/predict", tags=["Hotel Image Detection"])
        async def icon_detection_predict(file: UploadFile = File(...)):
            image_bytes = await file.read()
            image = Image.open(BytesIO(image_bytes))

            image_path = self._file_management.save_image(image, format='webp')

            high_prob_classes, all_class_probabilities, prediction_time = self._hotel_image_detection.make_prediction(image_path)

            sorted_predictions = sorted(all_class_probabilities, key=lambda x: x[1], reverse=True)

            return {
                'predictions': sorted_predictions,
                'prediction_time': prediction_time,
            }

    def get_router(self):
        """
        Returns the router associated with the icon detection controller.

        Returns:
            APIRouter: The API router for icon detection operations.
        """
        return self._router