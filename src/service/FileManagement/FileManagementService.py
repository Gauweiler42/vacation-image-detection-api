import logging
import os
import uuid
from PIL import Image

class FileManagementService(object):
    def __init__(self, app):
        self._logger = logging.getLogger(FileManagementService.__name__)
        self._logger.debug(f"Initialising {FileManagementService.__name__}")

        self._data_folder = os.path.join(app.get_data_folder(), FileManagementService.__name__)
        if not os.path.exists(self._data_folder):
            os.makedirs(self._data_folder)

        self._logger.info(f"Initialized {FileManagementService.__name__}")

    def save_image(self, image: Image, format='webp'):
        """
        Saves an image with a UUID filename in the data folder and returns the path.

        Args:
            image (PIL.Image): The image to save.
            format (str): The format to save the image in.

        Returns:
            str: The file path where the image was saved.
        """
        filename = f"{uuid.uuid4()}.{format.lower()}"
        file_path = os.path.join(self._data_folder, filename)

        image.save(file_path, format=format)
        self._logger.info(f"Image saved at {file_path}")

        return file_path
