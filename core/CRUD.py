from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
import asyncio
from urllib.parse import quote_plus

class MongoCRUD:
    def __init__(self, database_name, uri='mongodb://localhost:27017/'):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[database_name]

    ### flutter

    async def create(self, collection_name, document):
        collection = self.db[collection_name]
        result = await collection.insert_one(document)
        return str(result.inserted_id)

    async def read_all(self, collection_name):
        collection = self.db[collection_name]
        cursor = collection.find({}, {"_id": 0, "payload": 0})
        return await cursor.to_list(length=None)

    async def read_by_style(self, collection_name, style):
        collection = self.db[collection_name]
        document = await collection.find_one({"style": style}, {"payload": 1, "_id": 0})
        return document

    # async def update(self, collection_name, document_id, updates):
    #     collection = self.db[collection_name]
    #     result = await collection.update_one({"_id": ObjectId(document_id)}, {"$set": updates})
    #     return result.modified_count

    # update with style
    async def update_by_style(self, collection_name, style, updates):
        collection = self.db[collection_name]
        result = await collection.update_many({"style": style}, {"$set": updates})
        return result.modified_count

    # async def delete(self, collection_name, document_id):
    #     collection = self.db[collection_name]
    #     result = await collection.delete_one({"_id": ObjectId(document_id)})
    #     return result.deleted_count

    # clear all documents in a collection
    async def clear_collection(self, collection_name):
        collection = self.db[collection_name]
        await collection.delete_many({})
        return True

    # delete with style
    async def delete_by_style(self, collection_name, style):
        collection = self.db[collection_name]
        result = await collection.delete_many({"style": style})
        return result.deleted_count

    # check style exists
    async def style_exists(self, collection_name, style):
        collection = self.db[collection_name]
        document = await collection.find_one({"style": style})
        return document is not None

    # get document_id by style
    async def get_document_id_by_style(self, collection_name, style):
        collection = self.db[collection_name]
        document = await collection.find_one({"style": style})
        return document.get("_id")

    async def get_categories(self, collection_name):
        collection = self.db[collection_name]
        categories = await collection.distinct("category")
        return categories

    # read with category if "all" return all
    async def read_by_category(self, collection_name, category):
        collection = self.db[collection_name]
        if category == "all":
            cursor = collection.find({}, {"_id": 0, "payload": 0})
        else:
            cursor = collection.find({"category": category}, {"_id": 0, "payload": 0})
        return await cursor.to_list(length=None)


    ### cms
    async def read_all_cms(self, collection_name):
        collection = self.db[collection_name]
        cursor = collection.find({}, {"_id": 0, "items": 0})
        return await cursor.to_list(length=None)

    # get items by category
    async def read_by_category_cms(self, collection_name, category):
        collection = self.db[collection_name]
        document = await collection.find_one({"name": category}, {"_id": 0, "items": 1})
        return document

    # update by name
    async def update_by_name_cms(self, collection_name, name, updates):
        collection = self.db[collection_name]
        result = await collection.update_many({"name": name}, {"$set": updates})
        return result.modified_count

    # update item by category and item name but still fields not in updates will be kept
    async def update_item_by_name_cms(self, collection_name, category, item_name, updates):
        collection = self.db[collection_name]
        update_fields = {f"items.$.{k}": v for k, v in updates.items()}
        result = await collection.update_many({"name": category, "items.name": item_name}, {"$set": update_fields})
        return result.modified_count

    # add category
    async def add_category_cms(self, collection_name, document):
        collection = self.db[collection_name]
        result = await collection.insert_one(document)
        return str(result.inserted_id)

    # add item to category
    async def add_item_to_category_cms(self, collection_name, category, item):
        collection = self.db[collection_name]
        result = await collection.update_one({"name": category}, {"$push": {"items": item}})
        return result.modified_count

    # delete category
    async def delete_category_cms(self, collection_name, category):
        collection = self.db[collection_name]
        result = await collection.delete_one({"name": category})
        return result.deleted_count

    # delete item from category
    async def delete_item_from_category_cms(self, collection_name, category, item_name):
        collection = self.db[collection_name]
        result = await collection.update_one({"name": category}, {"$pull": {"items": {"name": item_name}}})
        return result.modified_count

    # check exists category
    async def category_exists_cms(self, collection_name, category):
        collection = self.db[collection_name]
        document = await collection.find_one({"name": category})
        return document is not None

    # check exists item in category
    async def item_exists_in_category_cms(self, collection_name, category, item_name):
        collection = self.db[collection_name]
        document = await collection.find_one({"name": category, "items.name": item_name})
        return document is not None

    # get payload by category and item name
    async def get_payload_by_category_and_item_name_cms(self, collection_name, category, item_name):
        collection = self.db[collection_name]
        document = await collection.find_one({"name": category, "items.name": item_name}, {"items.$": 1, "_id": 0})
        return document.get("items")[0].get("payload")


async def main():
    # mongodb://%s:%s@%s/?authSource=admin
    mongodb_uri = "mongodb://%s:%s@%s/?authSource=admin" % (
        quote_plus("root"), quote_plus("vtd@123!@#"),quote_plus("localhost:27017"))
    crud = MongoCRUD('mydatabase', mongodb_uri)
    # check connection
    # print(crud.db)

    # Tạo mới một tài liệu
    makeup_id = await crud.create('items', {
        "category": "MakeUp",
        "subcategory": "Realistic",
        "style": "Sweety",
        "img_url": "https://example.com/sweety.jpg",
        "payload": {
            "alwayson_scripts": {
                "ControlNet": {
                    "args": [
                        {
                            "advanced_weighting": None,
                            "batch_images": "",
                            "control_mode": "Balanced",
                            "enabled": True,
                            "guidance_end": 1,
                            "guidance_start": 0,
                            "hr_option": "Both",
                            "image": None,
                            "inpaint_crop_input_image": False,
                            "input_mode": "simple",
                            "is_ui": True,
                            "loopback": False,
                            "low_vram": False,
                            "model": "control_v11p_sd15_canny [d14c016b]",
                            "module": "canny",
                            "output_dir": "",
                            "pixel_perfect": True,
                            "processor_res": 512,
                            "resize_mode": "Crop and Resize",
                            "save_detected_map": True,
                            "threshold_a": 100,
                            "threshold_b": 200,
                            "weight": 1
                        }
                    ]
                }
            },
            "batch_size": 1,
            "cfg_scale": 7,
            "denoising_strength": 0.5,
            "height": 512,
            "width": 512
        }
    })
    print(f"Inserted Makeup ID: {makeup_id}")

    # Tạo thêm một tài liệu khác
    makeup_id_2 = await crud.create('items', {
        "category": "MakeUp",
        "subcategory": "Realistic",
        "style": "Girly",
        "img_url": "https://example.com/girly.jpg",
        "payload": {
            "alwayson_scripts": {
                "ControlNet": {
                    "args": [
                        {
                            "advanced_weighting": None,
                            "batch_images": "",
                            "control_mode": "Balanced",
                            "enabled": True,
                            "guidance_end": 1,
                            "guidance_start": 0,
                            "hr_option": "Both",
                            "image": None,
                            "inpaint_crop_input_image": False,
                            "input_mode": "simple",
                            "is_ui": True,
                            "loopback": False,
                            "low_vram": False,
                            "model": "control_v11p_sd15_canny [d14c016b]",
                            "module": "canny",
                            "output_dir": "",
                            "pixel_perfect": True,
                            "processor_res": 512,
                            "resize_mode": "Crop and Resize",
                            "save_detected_map": True,
                            "threshold_a": 100,
                            "threshold_b": 200,
                            "weight": 1
                        }
                    ]
                }
            },
            "batch_size": 1,
            "cfg_scale": 7,
            "denoising_strength": 0.5,
            "height": 512,
            "width": 512
        }
    })
    print(f"Inserted Makeup ID: {makeup_id_2}")

    # # Đọc tất cả các tài liệu mà không bao gồm payload
    # items = await crud.read_all('items')
    # print("Items excluding payload:", items)

    # # Đọc payload theo style
    # payload = await crud.read_by_style('items', 'Sweety')
    # print("Payload for style 'Sweety':", payload)

    # # Cập nhật tài liệu
    # update_count = await crud.update('items', makeup_id, {"img_url": "https://example.com/new_sweety.jpg"})
    # print(f"Number of documents updated: {update_count}")

    # # # Xóa tài liệu
    # # delete_count = await crud.delete('items', makeup_id)
    # # print(f"Number of documents deleted: {delete_count}")

if __name__ == "__main__":
    asyncio.run(main())