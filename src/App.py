from fastapi import FastAPI
import logging
import os


class App (object):
    def __init__(self, name, controller, services, repositories, entities, models, loglevel, tmp_folder=None, data_folder=None):
        """
        Eine Klasse die eine FastAPI App repräsentiert.

        :param name: Der Name der App
        :param controller: Die Controller Klassen als list
        :param services: Die Service Klassen als list
        :param repositories: Die Repository Klassen als list
        """
        self._name = name
        if tmp_folder is None:
            self._tmp_folder = os.path.join(os.getcwd(), 'tmp')
        else:
            self._tmp_folder = tmp_folder
        if not os.path.exists(self._tmp_folder):
            os.makedirs(self._tmp_folder)

        if data_folder is None:
            self._data_folder = os.path.join(os.getcwd(), 'data')
        else:
            self._data_folder = data_folder
        if not os.path.exists(self._data_folder):
            os.makedirs(self._data_folder)

        self._controller = controller
        self._services = services
        self._repositories = repositories
        self._entities = entities
        self._models = models

        self._app = FastAPI()

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        logging.basicConfig(level=loglevel, format='%(levelname)s:    %(name)-20s - %(message)s')

        self._logger = logging.getLogger(name)
        self._init_repositories()
        if not self._init_services():
            return None

        self._init_controller()

    def _init_controller(self):
        """
        Initialisiert alle Controller die in der App registriert sind.

        :return: None
        """
        self._logger.info("Initializing controller")
        for i in range(len(self._controller)):
            self._controller[i] = self._controller[i](self)
            self._app.include_router(self._controller[i].get_router())
            self._logger.debug("Initialized controller: " + str(self._controller[i].__class__.__name__))

    def _init_repositories(self):
        """
        Initialisiert alle Repositories die in der App registriert sind.

        :return: None
        """
        self._logger.info("Initializing repositories")
        for i in range(len(self._repositories)):
            self._repositories[i] = self._repositories[i](self)
            self._logger.debug("Initialized repository: " + str(self._repositories[i].__class__.__name__))

    def _init_services(self):
        """
        Initialisiert alle Services die in der App registriert sind.

        :return: Returns if all services were created successfully as a boolean
        """
        self._logger.info("Initializing services")
        for i in range(len(self._services)):
            new_service = self._services[i](self)
            if new_service is not None:
                self._services[i] = new_service
                self._logger.debug("Initialized service: " + str(self._services[i].__class__.__name__))
            else:
                self._logger.error(f"Error while creating services. App will shut down now...")
                return False
        return True

    def get_model(self, model_class):
        """
        Gibt ein Model Objekt zurück, welches in der App registriert ist.

        :param model_class: Die Klasse des Model Objekts
        :return: Die Model Klasse oder None
        """
        for model in self._models:
            if isinstance(model, model_class):
                self._logger.debug("Found model: " + str(model.__class__.__name__))
                return model
        self._logger.warning("Model not found: " + str(model_class.__class__.__name__))
        return None

    def get_entity(self, entity_class):
        """
        Gibt ein Entity Objekt zurück, welches in der App registriert ist.
        
        :param entity_class: Die Klasse des Entity Objekts
        :return: 
        """
        for entity in self._entities:
            if isinstance(entity, entity_class):
                self._logger.debug("Found entity: " + str(entity.__class__.__name__))
                return entity
        self._logger.warning("Entity not found: " + str(entity_class.__class__.__name__))
        return None

    def get_repository(self, repository_class):
        """
        Gibt ein initialisiertes Repository Objekt zurück, welches in der App registriert ist.

        :param repository_class: Das Repository Objekt
        :return: Das Repository Objekt oder None
        """
        for repository in self._repositories:
            if isinstance(repository, repository_class):
                self._logger.debug("Found repository: " + str(repository.__class__.__name__))
                return repository
        self._logger.warning("Repository not found: " + str(repository_class.__class__.__name__))
        return None

    def get_service(self, service_class):
        """
        Gibt ein initialisiertes Service Objekt zurück, welches in der App registriert ist.

        :param service_class: Das Service Objekt
        :return: Das Service Objekt oder None
        """
        for service in self._services:
            if isinstance(service, service_class):
                self._logger.debug("Found service: " + str(service.__class__.__name__))
                return service
        self._logger.warning("Service not found: " + str(service_class.__class__.__name__))
        return None

    def get_app(self):
        """
        Returns the FastAPI application instance.

        :return: FastAPI application instance
        """
        return self._app
    
    def get_tmp_folder(self):
        """
        Returns the temporary folder path.

        :return: str The path to the temporary folder
        """
        return self._tmp_folder
    
    def get_data_folder(self):
        """
        Returns the temporary folder path.

        :return: str The path to the temporary folder
        """
        return self._data_folder
