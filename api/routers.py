from fastapi import APIRouter
from utils.logging import Logger
from api.endpoints.health import HealthEndpoints
from api.endpoints.flutter_backend import FlutterBackendEndpoints
from api.endpoints.cms_backend import CMSBackendEndpoints
from api.endpoints.crud import CRUDEndpoints
from core.CRUD import MongoCRUD
import config

class Endpoints:
    def __init__(self, logger: Logger, crud: MongoCRUD) -> None:
        self.health_routers = HealthEndpoints().get_router()
        self.flutter_backend_routers = FlutterBackendEndpoints(logger, crud).get_router()
        self.cms_backend_routers = CMSBackendEndpoints(logger, crud).get_router()
        self.crud_routers = CRUDEndpoints(logger, crud).get_router()
        self.routers = APIRouter(prefix=config.SERVICE_NAME)
        self.routers.include_router(self.health_routers, tags=["health"])
        self.routers.include_router(self.flutter_backend_routers, tags=["flutter-backend"])
        self.routers.include_router(self.cms_backend_routers, tags=["cms-backend"])
        self.routers.include_router(self.crud_routers, tags=["crud"])

    def get_routers(self):
        return self.routers
