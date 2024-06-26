from fastapi import APIRouter, HTTPException, status, Request
from utils.logging import Logger
from core.CRUD import MongoCRUD
import config
import time
import aiohttp
from aiohttp import BasicAuth
import base64
from PIL import Image
from io import BytesIO
import json


class CMSBackendEndpoints:
    def __init__(self, logger: Logger, crud: MongoCRUD) -> None:
        self.logger = logger
        self.router = APIRouter()
        self.crud = crud
        self.collection_name = 'cms'

        # create
        @self.router.get("/cms/get_categories")
        async def get_categories():
            """
            Get all categories from the database.
            args:
                None
            return:
                List[ItemResponse]: A list of items.
            """
            try:
                data = await self.crud.read_all(self.collection_name)
                return data
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_router(self):
        return self.router