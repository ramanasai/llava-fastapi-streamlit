import streamlit as st
from dotenv import load_dotenv
import requests


def image_upload():
  with st.sidebar:
    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if file is not None:
        try:
            files = {"file": file}
            response = requests.post(url_upload, files=files)
        except Exception as e:
            st.write(str(e))
    else:
        st.write("Please upload an image")


def main():
    st.title("OllamaLlava")
    st.write("Welcome to OllamaLlava, the image recognition app")

    image_upload()

    messages = st.container(height=300)
    prompt = st.text_input("Say something")
    if st.button("Send"):
        if prompt:
            messages.chat_message("user").write(prompt)
            messages.chat_message("assistant").write(
                f"Echo: {requests.get(url_input_text + prompt).json()}"
            )


if __name__ == "__main__":
    load_dotenv()
    url_upload = "http://127.0.0.1:8099/uploadfile"
    url_input_text = "http://127.0.0.1:8099/input-text?text="
    main()
