import requests
from moviepy.editor import *
import pysrt
from pysrt import SubRipFile
from pysrt import SubRipItem
""" 

    Author: Solovov N. G. (CyberEssence)
    
"""

import subprocess
import os


# класс создан для юнит-тестов (проверки правильности генерации субтитров)
class Text:
	def get_text(self):
		url = "http://88.87.79.40:8000/aZj6awUBVn/"
		#file = os.listdir(path="/home/manjaro/Desktop/diplom/project/audio") 
		with open(r'/home/manjaro/Desktop/diplom/project/audio/mod_2.wav', 'rb') as f:
			files = {'file': f.read()}
		r = requests.post(url, files=files)
		text = r.text
		text = text.replace("[", "")
		text = text.replace("]", "")
		return text
