from fastapi import APIRouter
import logging

class RootReadController:
    """
    A controller for managing the root routes in a FastAPI application.
    Provides a basic route to confirm that the application is running.
    """

    def __init__(self, app):
        """
        Initializes the RootReadController with its routes.

        Args:
            app: The main application instance (not used in this controller but typical for consistency in larger apps).
        """
        self._prefix = ""
        self._router = APIRouter()
        self._init_get_routes()
        self._logger = logging.getLogger(RootReadController.__name__)

        self._logger.info("Initialized controller: " + RootReadController.__name__)

    def _init_get_routes(self):
        """
        Initializes a GET route for the root path to provide application status.
        """

        @self._router.get(self._prefix + "/")
        async def get_alive():
            """
            Endpoint to confirm that the application is running.

            Returns:
                dict: A dictionary confirming that the service is alive, along with a link to the API documentation.
            """
            return {
                "status": "OK",
                "message": "Alive",
                "docs": "/docs",
            }

    def get_router(self):
        """
        Returns the router associated with the root read operations.

        Returns:
            APIRouter: The API router for the root routes.
        """
        return self._router
