#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import moviepy.editor as mp 
from pydub import AudioSegment
#import torch
import requests
#import nemo.collections.asr as nemo_asr
import os, re


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)



if __name__ == '__main__':
    #rename_video()
    #convert()
    #remove_trash_files()
    #os.chdir(r'/home/manjaro/Desktop/diplom/project/')
    main()
    
