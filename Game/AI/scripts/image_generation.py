import requests, base64, cv2
import numpy as np
from rembg import remove
from PIL import Image
# Define the URL and the payload to send.
class ImageGeneration():
    def __init__(self):
        self.url = "http://127.0.0.1:7860"
        self.payloadType = {}

        self.payloadType["character"] = {
        "prompt": rf"the painting of a character, art by character <hypernet:character:1>",
        "steps": 50,
        "height":128,
        "width": 128
        } 
        self.payloadType["tile"] = {
                "prompt": rf"a rendering of tile, art by tile <hypernet:tile:1>",
                "steps": 20,
                "height":256,
                "width": 256
            }
        self.payloadType["weapon"] = {
                "prompt": rf"a rendering of weapon, art by weapon <hypernet:weapon:1>",
                "steps": 50,
                "height":64,
                "width": 64
            }

        self.payloadType["spaceship"] = {
                "prompt": rf"a bright photo of the space ship <hypernet:space ship:1>",
                "steps": 50,
                "height":128,
                "width": 128
            }

        self.generationNum = {
            "weapon": 0,
            "tile": 0,
            "spaceship":0,
            "character":0
        }



    def generateImage(self, type: str):
        self.generationNum[type] +=1
        payload = self.payloadType[type]
                
        response = requests.post(url=f'{self.url}/sdapi/v1/txt2img', json=payload)
        r = response.json()

        generated_image_path = rf"Game Assets/generated/{type}/{type}{self.generationNum[type]}.png"

        # Decode and save the image.
        with open(generated_image_path, 'wb') as f:
            f.write(base64.b64decode(r['images'][0]))

        with open(generated_image_path, 'rb') as input_file:
            input_image = input_file.read()
            output_image = remove(input_image)

        # Save the background-removed image
        bg_removed_image_path = rf"Game Assets/generated/{type}/{type}{self.generationNum[type]}_no_bg.png"
        with open(bg_removed_image_path, 'wb') as f:
            f.write(output_image)

        self.flip_image_horizontally(bg_removed_image_path, type=type)

    def flip_image_horizontally(self, image_path, type):
         # Open the original image
        original_image = Image.open(image_path)
        image_array = np.array(original_image)

        # Flip the image horizontally
        flipped_image = cv2.flip(image_array, 1)

        # Convert flipped image back to PIL
        flipped_image_pil = Image.fromarray(flipped_image)

        # Save the flipped image temporarily
        flipped_image_path = rf"Game Assets/generated/{type}{self.generationNum[type]}_flipped_temp.png"
        flipped_image_pil.save(flipped_image_path, format="PNG")

        # Remove the background from the flipped image
        with open(flipped_image_path, 'rb') as f:
            input_image = f.read()
            output_image = remove(input_image)

        # Save the final flipped and background-removed image
        flipped_no_bg_image_path = rf"Game Assets/generated/{type}/{type}{self.generationNum[type]}_flipped.png"
        with open(flipped_no_bg_image_path, 'wb') as f:
            f.write(output_image)