from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    category: str
    subcategory: str
    style: str
    img_url: str

class ItemsResponse(BaseModel):
    items: List[Item]

class MakeupRequest(BaseModel):
    img: str
    style: str

class ClothesRequest(BaseModel):
    img: str
    style: str

class HairRequest(BaseModel):
    img: str
    style: str
    color: str

class PostModelResponse(BaseModel):
    request_id: str

# class GetModelResponse(BaseModel):
#     img: str

class CMSRequest(BaseModel):
    img: str
    category: str
    item_name: str
    properties: dict