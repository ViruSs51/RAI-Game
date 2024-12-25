import requests
import base64
import numpy as np
# Define the URL and the payload to send.
url = "http://127.0.0.1:7860"

payloadType = {}

payloadType["character"] = {
        "prompt": rf"the painting of a character, art by character <hypernet:character:1>",
        "steps": 50,
        "height":128,
        "width": 128
    } 
payloadType["tile"] = {
        "prompt": rf"a rendering of tile, art by tile <hypernet:tile:1>",
        "steps": 50,
        "height":256,
        "width": 256
    }
payloadType["weapon"] = {
        "prompt": rf"a rendering of weapon, art by weapon <hypernet:weapon:1>",
        "steps": 50,
        "height":64,
        "width": 64
    }



def generateImage(type: str):

    payload = payloadType[type]
        
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()

    # Decode and save the image.
    with open(rf"Game Assets/generated/{type}.png", 'wb') as f:
        f.write(base64.b64decode(r['images'][0]))

generateImage("weapon")