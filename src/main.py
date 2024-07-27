from .App import App
from .controller import *
from .service import *
from dotenv import load_dotenv
import os


load_dotenv()
name = os.getenv('APP_NAME', 'SET-A-NAME')
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

controller = [
    RootReadController,
    HotelImageDetectionController,
]

services = [
    FileManagementService,
    HotelImageDetectionService,
]

repositories = []

entities = []

models = []

app_instance = App(name, controller, services, repositories, entities, models, log_level)
app = app_instance.get_app()
