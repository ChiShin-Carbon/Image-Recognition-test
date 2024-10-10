import base64
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from connect import collection

router = APIRouter()

@router.get("/image/{image_id}")
async def get_image(image_id: str):
    try:
        image_data = collection.find_one({"_id": ObjectId(image_id)})
        if image_data is None:
            raise HTTPException(status_code=404, detail="Image not found")

        # Return image as base64 string
        base64_image = base64.b64encode(image_data['image']).decode('utf-8')
        return {"image": base64_image, "filename": image_data.get("filename")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
