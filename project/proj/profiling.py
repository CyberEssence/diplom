""" 

    Author: Solovov N. G. (CyberEssence)
    
"""


import time
import requests

def get_text():
        url = "http://88.87.79.40:8000/aZj6awUBVn/"
        with open(r"/home/manjaro/Desktop/diplom/project/audio/mod_2.wav", "rb") as f:
                files = {"file": f.read()}      
        r = requests.post(url, files=files)
        text = r.text
        text = text.replace("[", "")
        text = text.replace("]", "")
        return text


# проверка скорости генерации текста
start_time = time.time()
get_text()
print("--- %s seconds ---" % (time.time() - start_time))
