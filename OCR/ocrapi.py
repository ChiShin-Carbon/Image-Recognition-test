from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import pytesseract
import io


ocrapi = APIRouter()

@ocrapi.post("/ocrapi")
async def ocr_image(image: UploadFile = File(...)):
    try:
        # Read the uploaded image file
        image_data = await image.read()
        img = Image.open(io.BytesIO(image_data))  # Open image from bytes

        # Use pytesseract to perform OCR
        text = pytesseract.image_to_string(img, lang='chi_tra+eng')

        return {"recognized_text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
