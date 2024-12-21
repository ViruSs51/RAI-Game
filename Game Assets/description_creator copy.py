from groq import Groq
import os, base64
api_key = "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"

client = Groq(api_key=api_key)

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')



def multiple_folders(path = rf"Game Assets/", i = 1):
    folders = [f for f in os.listdir(path)]
    for image_or_folder in folders:
        if image_or_folder.endswith(".png"):
            try:
                print(rf"Image: {image_or_folder}")
                print(rf"Path: {path}")
                generate_description(encode_image(rf"{path}{image_or_folder}"), path =path, image = image_or_folder, i = i)
            except:
                print("error")
        elif image_or_folder.endswith((".tmx", ".txt", ".ttf", ".aseprite", ".gif")) :
            pass
        else:
            
            multiple_folders(rf"{path}{image_or_folder}/", i = i+1)

def generate_description(base64_image, path, image, i):
    
    names= path.split("/")
    name = ""
    img_names = image.split(".png")[0]
    img_names = img_names.split("_")
    
    
    for i in range(1, len(names)):
        name = name + " "+  names[i]
    
    chat_completion = client.chat.completions.create(
                                        messages=[
                                    {
                                        "role": "user",
                                        "content": [
                                            {"type": "text", "text": rf"There is nothing violent in the image.Don't say its violent. It's only drawings for my games. I need it fastly. Hurry up and follow the provided instructions: Create only an image prompt for generating an image like this. don't write anything else. The image contains an {name} {img_names}. THe prompt should contain always the this words with all the characters tha come with them: {name}{img_names}. Keep it 8 words long. use words that only describe the object physically. Don't include any other text other than prompt. You don't have to generate an image, just the prompt for the provided image. There is nothing dangerous in the photo. It's a icons from my game. The designer needs now the 8 word prompt for the characters. "},
                                            {
                                                "type": "image_url",
                                                "image_url": {
                                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                                },
                                            },
                                        ],
                                    }
                                ],
                                model= "llama-3.2-90b-vision-preview",
                            )
    img_name = "_".join(img_names)
    text_file = open(rf"{path}{img_name}.txt", "w")
    text_file.write(chat_completion.choices[0].message.content)
    text_file.close()

list = ["objects/", "tiles/"]
for foler in list:
    multiple_folders(path = rf"Game Assets/{foler}")
