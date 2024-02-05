from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
from io import BytesIO
import base64
from IPython.display import HTML, display



class OllamaLlava(Ollama):
    def __init__(self):
        """
        Initialize the OllamaLlava class
        """
        load_dotenv()
        super().__init__()

    def model_load(self):
        """
        Load the Ollama model
        """
        return Ollama(model=os.getenv("MODEL_NAME"))

    def convert_to_base64(self, pil_image):
        """
        Convert PIL images to Base64 encoded strings

        :param pil_image: PIL image
        :return: Re-sized Base64 string
        """

        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")  # You can change the format if needed
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_str


    def plt_img_base64(self, img_base64):
        """
        Disply base64 encoded string as image

        :param img_base64:  Base64 string
        """
        # Create an HTML img tag with the base64 string as the source
        image_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'
        # Display the image by rendering the HTML
        display(HTML(image_html))

    def save_image(self, img, path):
        """
        Save the image to a specified path

        :param img: Image
        :param path: Path to save the image
        """
        open(path, 'wb').write(img.file.read())
