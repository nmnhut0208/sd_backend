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
                data = await self.crud.read_all_cms(self.collection_name)
                return data
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.get("/cms/get_items/{category}")
        async def get_items(category: str):
            """
            Get all items from the database.
            args:
                None
            return:
                List[ItemResponse]: A list of items.
            """
            try:
                data = await self.crud.read_by_category_cms(self.collection_name, category)
                return data
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.post("/cms/update_category/{category}")
        async def update_category(category: str, request: dict):
            """
            Update an item in the database.
            args:
                category (str): The category to update.
                request (dict): The item to update.
            return:
                dict: The status of the operation.
            """
            try:
                await self.crud.update_by_name_cms(self.collection_name, category, request)
                return {"status": "success"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.post("/cms/update_item/{category}/{item_name}")
        async def update_item(category: str, item_name: str, request: dict):
            """
            Update an item in the database.
            args:
                category (str): The category to update.
                item_name (str): The item name to update.
                request (dict): The item to update.
            return:
                dict: The status of the operation.
            """
            try:
                await self.crud.update_item_by_name_cms(self.collection_name, category, item_name, request)
                return {"status": "success"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        # check if the item exists
        @self.router.post("/cms/add_category")
        async def add_category(request: dict):
            """
            Add a category to the database.
            args:
                request (dict): The category to add.
            return:
                dict: The status of the operation.
            """
            try:
                exists = await self.crud.category_exists_cms(self.collection_name, request['name'])
                if exists:
                    return {"status": "exists"}
                await self.crud.add_category_cms(self.collection_name, request)
                return {"status": "success"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.post("/cms/add_item/{category}")
        async def add_item(category: str, request: dict):
            """
            Add an item to the database.
            args:
                category (str): The category to add the item to.
                request (dict): The item to add.
            return:
                dict: The status of the operation.
            """
            try:
                exists = await self.crud.item_exists_in_category_cms(self.collection_name, category, request['name'])
                if exists:
                    return {"status": "exists"}
                await self.crud.add_item_to_category_cms(self.collection_name, category, request)
                return {"status": "success"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.delete("/cms/delete_category/{category}")
        async def delete_category(category: str):
            """
            Delete a category from the database.
            args:
                category (str): The category to delete.
            return:
                dict: The status of the operation.
            """
            try:
                await self.crud.delete_category_cms(self.collection_name, category)
                return {"status": "success"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.delete("/cms/delete_item/{category}/{item_name}")
        async def delete_item(category: str, item_name: str):
            """
            Delete an item from the database.
            args:
                category (str): The category to delete the item from.
                item_name (str): The item name to delete.
            return:
                dict: The status of the operation.
            """
            try:
                await self.crud.delete_item_cms(self.collection_name, category, item_name)
                return {"status": "success"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        # get payload
        @self.router.get("/cms/get_payload/{category}/{item_name}")
        async def get_payload(category: str, item_name: str):
            """
            Get the payload of an item.
            args:
                category (str): The category of the item.
                item_name (str): The name of the item.
            return:
                dict: The payload of the item.
            """
            try:
                data = await self.crud.get_payload_by_category_and_item_name_cms(self.collection_name, category, item_name)
                return data
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_router(self):
        return self.router