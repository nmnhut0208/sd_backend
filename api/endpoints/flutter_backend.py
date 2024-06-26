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
from schemas.schemas import Item, ItemsResponse, MakeupRequest, ClothesRequest, HairRequest, PostModelResponse

def get_image_dimensions(base64_str: str):
    image_data = base64.b64decode(base64_str)
    image = Image.open(BytesIO(image_data))
    return image.width, image.height

class FlutterBackendEndpoints:
    def __init__(self, logger: Logger, crud: MongoCRUD) -> None:
        self.logger = logger
        self.router = APIRouter()
        self.crud = crud
        self.collection_name = 'flutter'
        self.ai_type = {
            "MakeUp": "sd-img2img",
            "Clothes": "sd-img2img",
            "Hair": "sd-txt2img"
        }
        self.colors = json.load(open('assets/colors.json'))
        # print("nhut: ", self.crud.db)
        # basic auth
        # self.auth = BasicAuth(config.USERNAME, config.PASSWORD)

        # @self.router.get("/get_img", response_model=ItemsResponse)
        # async def get_img():
        #     """
        #     Get all items from the database.
        #     args:
        #         None
        #     return:
        #         List[ItemResponse]: A list of items.
        #     """
        #     try:
        #         # start = time.time()
        #         data = await self.crud.readre_all('items')
        #         items = [Item(**item) for item in data]
        #         # self.logger.info({'message': f'GET img time: {round(time.time() - start, 4)} data: {str(items)}'})
        #         return ItemsResponse(items=items)
        #     except Exception as e:
        #         # self.logger.error({"error": str(e)})
        #         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        # read by category
        @self.router.get("/flutter/get_img/{category}", response_model=ItemsResponse)
        async def get_img(category: str):
            """
            Get all items from the database by category (all if category is "all") .
            args:
                category (str): The category to filter items by.
            return:
                List[ItemResponse]: A list of items.
            """
            try:
                data = await self.crud.read_by_category(self.collection_name, category)
                items = [Item(**item) for item in data]
                return ItemsResponse(items=items)
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.post("/flutter/makeup", response_model=PostModelResponse)
        async def makeup(request: MakeupRequest):
            """
            Make up the image with the given style.
            args:
                request (MakeupRequest): The request object containing the image and style.
            return:
                PostModelResponse: The response object containing the request id.
            """
            data = await self.crud.read_by_style(self.collection_name, request.style)
            payload = data['payload']
            payload['init_images'] = [request.img]
            width, height = get_image_dimensions(request.img)
            # print(width, height)
            payload['width'], payload['height'] = width, height
            # print(payload)
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(f'{config.URL_PREFIX}/submit?ai-type=sd-img2img', json=payload) as response:
                        response = await response.json()
                        # print(response)
                        if response['isSuccess']:
                            return PostModelResponse(request_id=response['data']['request_id'])
                        else:
                            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=response['message'])
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.post("/flutter/clothes", response_model=PostModelResponse)
        async def clothes(request: ClothesRequest):
            """
            Change the style of the clothes of the image.
            args:
                request (ClothesRequest): The request object containing the image and style.
            return:
                PostModelResponse: The response object containing the request id.
            """
            try:
                data = await self.crud.read_by_style(self.collection_name, request.style)
                # print(data)
                payload = data['payload']
                # print(payload)
                payload['alwayson_scripts']['roop']['args'][0] = request.img
                payload['init_images'] = [request.img]
                width, height = get_image_dimensions(request.img)
                payload['width'], payload['height'] = width, height
                # print(payload)
                async with aiohttp.ClientSession() as session:
                    async with session.post(f'{config.URL_PREFIX}/submit?ai-type=sd-img2img', json=payload) as response:
                        response = await response.json()
                        # print(response)
                        if response['isSuccess']:
                            return PostModelResponse(request_id=response['data']['request_id'])
                        else:
                            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=response['message'])
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.post("/flutter/hair", response_model=PostModelResponse)
        async def hair(request: HairRequest):
            """
            Change the style, color hair of the image.
            args:
                request (HairRequest): The request object containing the image, style and color.
            return:
                PostModelResponse: The response object containing the request id.
            """
            try:
                data = await self.crud.read_by_style(self.collection_name, request.style)
                payload = data['payload']
                payload['prompt'] = payload['prompt'].replace('param_hair color', request.color + " hair color")
                # print(payload['prompt'])
                payload['alwayson_scripts']['roop']['args'][0] = request.img
                payload['width'], payload['height'] = 512, 512
                # print(payload)
                async with aiohttp.ClientSession() as session:
                    async with session.post(f'{config.URL_PREFIX}/submit?ai-type=sd-txt2img', json=payload) as response:
                        response = await response.json()
                        # print(response)
                        if response['isSuccess']:
                            return PostModelResponse(request_id=response['data']['request_id'])
                        else:
                            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=response['message'])

            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.get("/flutter/result/{request_id}")
        async def result(request: Request, request_id: str, category: str):
            """
            Get the result of the AI model.
            args:
                request_id (str): The request id of the AI model.
                category (str): The category of AI model.
            return:
                dict: The result of the AI model.
            """
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'{config.URL_PREFIX}/status/{request_id}?ai-type={self.ai_type[category]}') as response:
                        response_data = await response.json()
                        # print(response_data)
                        if response_data['isSuccess']:
                            return response_data
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.get("/flutter/get_categories")
        async def get_categories():
            """
            Get all categories from the database.
            args:
                None
            return:
                List[str]: A list of categories.
            """
            try:
                data = await self.crud.get_categories(self.collection_name)
                return data
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        @self.router.get("/flutter/get_colors")
        async def get_colors():
            """
            Get all colors from the database.
            args:
                None
            return:
                List[str]: A list of colors.
            """
            try:
                return self.colors
            except Exception as e:
                # self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        
    def get_router(self):
        return self.router
