import logging
import os


class FileManagementService(object):
    def __init__(self, app):
        self._logger = logging.getLogger(FileManagementService.__name__)
        self._logger.debug(f"Initialising {FileManagementService.__name__}")

        self._tmp_folder = os.path.join(app.get_data_folder(), FileManagementService.__name__)
        if not os.path.exists(self._tmp_folder):
            os.makedirs(self._tmp_folder)

        self._logger.info(f"Initialized {FileManagementService.__name__}")
