from fastapi import APIRouter


class HealthEndpoints:
    def __init__(self):
        self.router = APIRouter()
        @self.router.get("/healthcheck")
        def healthcheck():
            return True

    def get_router(self):
        return self.router
