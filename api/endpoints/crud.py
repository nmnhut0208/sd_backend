from utils.logging import Logger
from fastapi import APIRouter, HTTPException, status, Request
from core.CRUD import MongoCRUD
import config

class CRUDEndpoints:
    def __init__(self, logger: Logger, crud: MongoCRUD) -> None:
        self.logger = logger
        self.router = APIRouter()
        self.crud = crud

        # CREATE
        @self.router.post("/crud/create/{collection}")
        async def create(collection: str, request: dict):
            """
            Create an item in the database.
            args:
                collection (str): The collection to insert the item into.
                request (dict): The item to insert.
            return:
                dict: The status of the operation.
            """
            try:
                document_id = await self.crud.create(collection, request)
                return {"status": "success"}
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.get("/crud/read_all/{collection}")
        async def read_all(collection: str):
            """
            Read all items from the database.
            args:
                None
            return:
                List[ItemResponse]: A list of items.
            """
            try:
                data = await self.crud.read_all(collection)
                return data
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.get("/crud/read_by_style/{collection}/{style}")
        async def read_by_style(collection: str, style: str):
            """
            Read items by style from the database.

            Args:
                style (str): The style to filter items by.

            Returns:
                ItemResponse: The item with the given style.
            """
            try:
                data = await self.crud.read_by_style(collection, style)
                return data
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        # @self.router.put("/crud/update/{document_id}")
        # async def update(document_id: str, request: dict):
        #     """
        #     Update an item in the database.
        #     args:
        #         document_id (str): The id of the item to update.
        #         request (dict): The updated item.
        #     return:
        #         dict: The status of the operation.
        #     """
        #     try:
        #         modified_count = await self.crud.update("items", document_id, request)
        #         return {"status": "success"}
        #     except Exception as e:
        #         # self.logger.error({"error": str(e)})
        #         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        # update by style
        @self.router.put("/crud/update_by_style/{collection}/{style}")
        async def update_by_style(collection: str, style: str, request: dict):
            """
            Update items by style in the database.
            args:
                style (str): The style to filter items by.
                request (dict): The updated item.
            return:
                dict: The status of the operation.
            """
            try:
                modified_count = await self.crud.update_by_style(collection, style, request)
                return {"status": "success"}
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        # @self.router.delete("/crud/delete/{document_id}")
        # async def delete(document_id: str):
        #     """
        #     Delete an item from the database.
        #     args:
        #         document_id (str): The id of the item to delete.
        #     return:
        #         dict: The status of the operation.
        #     """
        #     try:
        #         deleted_count = await self.crud.delete("items", document_id)
        #         return {"status": "success"}
        #     except Exception as e:
        #         # self.logger.error({"error": str(e)})
        #         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.delete("/crud/clear_collection/{collection}")
        async def clear_collection(collection: str):
            """
            Clear all items from the database.
            args:
                None
            return:
                dict: The status of the operation.
            """
            try:
                await self.crud.clear_collection(collection)
                return {"status": "success"}
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.delete("/crud/delete_by_style/{collection}/{style}")
        async def delete_by_style(collection: str, style: str):
            """
            Delete items by style from the database.
            args:
                style (str): The style to filter items by.
            return:
                dict: The status of the operation.
            """
            try:
                deleted_count = await self.crud.delete_by_style(collection, style)
                return {"status": "success"}
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        
        @self.router.get("/crud/style_exists/{collection}/{style}")
        async def style_exists(collection: str, style: str):
            """
            Check if a style exists in the database.
            args:
                style (str): The style to check.
            return:
                dict: The status of the operation.
            """
            try:
                exists = await self.crud.style_exists(collection, style)
                return {"exists": exists}
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


        # get document id by style
        @self.router.get("/crud/get_document_id_by_style/{collection}/{style}")
        async def get_document_id_by_style(collection: str, style: str):
            try:
                document_id = await self.crud.get_document_id_by_style(collection, style)
                return str(document_id)
            except Exception as e:
                self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_router(self):
        return self.router