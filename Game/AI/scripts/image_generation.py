import requests
import base64
import numpy as np
# Define the URL and the payload to send.
class ImageGeneration():
    def __init__(self):
        url = "http://127.0.0.1:7860"
        self.payloadType = {}

        self.payloadType["character"] = {
        "prompt": rf"the painting of a character, art by character <hypernet:character:1>",
        "steps": 50,
        "height":128,
        "width": 128
        } 
        self.payloadType["tile"] = {
                "prompt": rf"a rendering of tile, art by tile <hypernet:tile:1>",
                "steps": 50,
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
                
        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
        r = response.json()

        # Decode and save the image.
        with open(rf"Game Assets/generated/{type}{self.generationNum[type]}.png", 'wb') as f:
            f.write(base64.b64decode(r['images'][0]))
