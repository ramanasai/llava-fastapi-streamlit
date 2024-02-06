# app.py
from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
import os
import uvicorn
import src.OllamaLlava as OllamaLlava
import uuid
from PIL import Image


app = FastAPI()

load_dotenv()

@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
  file_location = os.getenv("UPLOAD_FOLDER") + uuid.uuid4().hex + file.filename
  try:
    ol.save_image(file, file_location)
    pil_image = Image.open(file_location)
    img_base64 = ol.convert_to_base64(pil_image)
    global llm_with_image_context
    llm_with_image_context = model_llava.bind(images=[img_base64])
  except Exception as e:
    return {"error": str(e)}
  return llm_with_image_context.invoke("What does the image contain?")

@app.get("/input-text"
async def input_text(text: str):
  return llm_with_image_context.invoke(text)

if __name__ == "__main__":
  ol = OllamaLlava()

  model_llava = ol.model_load()
  uvicorn.run(app, host=os.getenv("HOST"), port=os.getenv("PORT"))
