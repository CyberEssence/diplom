""" 

    Author: Solovov N. G. (CyberEssence)
    
"""

from moviepy.editor import * 
from pydub import AudioSegment
#import torch
import requests
#import nemo.collections.asr as nemo_asr
import numpy as np
from pyxdameraulevenshtein import damerau_levenshtein_distance_seqs
import pysrt
from pysrt import SubRipFile
from pysrt import SubRipItem
import subprocess
import moviepy.editor as mp 
from pydub import AudioSegment
import re

def fix_command(text, words=['что', 'происходит', 'малыш', 'тебе', 'уже', 'третий раз', 'ловят', 'на', 'драке', 'я', 'знаю']):
        array = np.array(words)

        result = list(zip(words, list(damerau_levenshtein_distance_seqs(text, array))))

        command, rate = min(result, key=lambda x: x[1])

        # Подобранное значение для определения совпадения текста среди значений указанного списка
        # Если True, считаем что слишком много ошибок в слове, т.е. text среди all_commands нет
        #if rate > 0.40:
        #   return

        return command

def rename_video():
    n = 1
    os.chdir(r'/home/manjaro/Desktop/diplom/project/media/video/22')
    for i in os.listdir('/home/manjaro/Desktop/diplom/project/media/video/22'):
        os.rename(i, re.sub(r'\w+.mp4', '{n}.mp4'.format(n=n), i))
        n += 1
    os.chdir(r'/home/manjaro/Desktop/diplom/project/')



def convert():
    files = os.listdir(path="/home/manjaro/Desktop/diplom/project/media/video/22") 
    #print(len(files))
    for i in range(1, len(files)+1):
        clip = mp.VideoFileClip(f"/home/manjaro/Desktop/diplom/project/media/video/22/{i}.mp4")
        clip.audio.write_audiofile(f"/home/manjaro/Desktop/diplom/project/audio/{i}.mp3")
        sound = AudioSegment.from_mp3(f"/home/manjaro/Desktop/diplom/project/audio/{i}.mp3")
        sound.export(f"/home/manjaro/Desktop/diplom/project/audio/pre_{i}.wav", format="wav")
        sound1 = AudioSegment.from_wav(f"/home/manjaro/Desktop/diplom/project/audio/pre_{i}.wav")
        sound1 = sound1.set_channels(1)
        sound1.export(f"/home/manjaro/Desktop/diplom/project/audio/mod_{i}.wav", format="wav")

def get_text():
    url = "http://88.87.79.40:8000/aZj6awUBVn/"
    #file = os.listdir(path="/home/manjaro/Desktop/diplom/project/audio") 
    with open(r'/home/manjaro/Desktop/diplom/project/audio/mod_2.wav', 'rb') as f:
        files = {'file': f.read()}
    r = requests.post(url, files=files)
    text = r.text
    text = text.replace("[", "")
    text = text.replace("]", "")
    return text


def save_srt(txt):
    file1 = pysrt.SubRipFile()
    file2 = pysrt.SubRipFile()

    sub_1 = pysrt.SubRipItem(1, start='00:00:10,000', end='00:00:20,000', text=txt[0:30])
    file1.append(sub_1)
    file1.save('/home/manjaro/Desktop/diplom/project/subtitles/_2_1.srt')

    sub_2 = pysrt.SubRipItem(2, start='00:00:20,000', end='00:00:35,000', text=txt[30:60])
    file2.append(sub_2)
    file2.save('/home/manjaro/Desktop/diplom/project/subtitles/_2_2.srt')

    sub_3 = pysrt.SubRipItem(3, start='00:00:35,000', end='00:00:40,000', text=txt[60:90])
    file2.append(sub_3)
    file2.save('/home/manjaro/Desktop/diplom/project/subtitles/_2_3.srt')

    sub_4 = pysrt.SubRipItem(4, start='00:00:40,000', end='00:00:55,000', text=txt[90:120])
    file2.append(sub_4)
    file2.save('/home/manjaro/Desktop/diplom/project/subtitles/_2_4.srt')


def merge_srt():
    os.chdir(r'/home/manjaro/Desktop/diplom/project/subtitles')
    ls = [i for i in os.listdir('/home/manjaro/Desktop/diplom/project/subtitles') if i.endswith('.srt')]
    ls.sort()
    with open('2.srt','w') as f:
        for j in ls:
            s = open(j).read()
            f.write(s)
            f.write('\n')

    os.chdir(r'/home/manjaro/Desktop/diplom/project')


def remove_trash_files():
    from pathlib import Path
    path = Path('/home/manjaro/Desktop/diplom/project/subtitles')
    for file_name in path.glob('_*.srt'):
        file_name.unlink()


def srt_to_video():
    subprocess.check_call("ffmpeg -i /home/manjaro/Desktop/diplom/project/subtitles/2.srt /home/manjaro/Desktop/diplom/project/subtitles/2.ass", shell=True)
    subprocess.check_call("ffmpeg -i /home/manjaro/Desktop/diplom/project/media/video/22/2.mp4 -vf ass=/home/manjaro/Desktop/diplom/project/subtitles/2.ass /home/manjaro/Desktop/diplom/project/media/video/22/2_mod.mp4", shell=True)

