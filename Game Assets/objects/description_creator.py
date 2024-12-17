from groq import Groq
import os



def multiple_folders():
    folders = [f for f in os.listdir(rf"Game Assets/objects")]
    
    for folder in folders:
        
        files = [f for f in os.listdir(rf"Game Assets/objects/{folder}/")]
        print(files)
            
multiple_folders()