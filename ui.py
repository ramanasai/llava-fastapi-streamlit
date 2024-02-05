import streamlit as st
from dotenv import load_dotenv
import requests

def main():
  st.title("OllamaLlava")
  st.write("Welcome to OllamaLlava, the image recognition app")

  file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

  if st.button("Submit"):
    if file is not None:
      url_upload = "http://localhost:8098/uploadfile"
      files = {"file": file}
      response = requests.post(url_upload, files=files)
      st.write(response.json())

    else:
      st.write("Please upload an image")


if __name__ == "__main__":
  load_dotenv()
  main()
