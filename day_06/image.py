# FastAPI
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import io
from PIL import Image
import asyncio

class ImageSummary(BaseModel):
    width: int
    height: int
    mode: str
    mean_brightness: float
    comment: str

app = FastAPI("Image Analyzer")

def analyze_image(img: Image.Image) -> ImageSummary:
    rgb = img.convert("RGB")
    arr = np.arr(rgb)

    gray = arr.mean(axis=2)
    mean_brightness = float(gray.mean())

    if mean_brightness < 50:
        comment = "Image looks quite dark"
    elif mean_brightness > 190:
        comment = "Image looks very bright"
    else:
        comment = "Image looks normal"


    return ImageSummary(
        width=img.width,
        height=img.height,
        mode=img.mode,
        mean_brightness=mean_brightness,
        comment=comment
    )

@app.post("/analyze", response_model=ImageSummary)
async def image_analyze(file: UploadFile = File(...)):
    if file.content_type not in {"image/png", "image/jpg", "image/jpeg", "image/webp"}:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # read file
    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="Empty file")

    try:
        img = Image.open(io.BytesIO(data))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

    summary = analyze_image(img)
    return summary
