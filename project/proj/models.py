from django.db import models
import requests
import os, re
from .funcs import fix_command, get_text, save_srt, remove_trash_files, srt_to_video

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
    category = models.ForeignKey(Category, name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    #image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s' % (self.category.slug, self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    #pk = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=100)
    #slug = models.SlugField(max_length=50, unique=True, default="post")


    text = get_text()
    text_lst = text.split(' ')
    text_mod = []
    print(text_lst)
    for i in text_lst:
        text_mod.append(fix_command(i))
    
    txt = " ".join(map(str, text_mod))

    save_srt(txt)

    srt_to_video()

    remove_trash_files()
    txt = get_text()

    #subprocess.check_call('ffmpeg -i /home/manjaro/Desktop/diplom/project/media/video/22/2_mod.mp4 -vf "setpts=0.20*PTS" /home/manjaro/Desktop/diplom/project/media/video/22/2_mod_fast_5.mp4', shell=True)

    #video = models.FileField(upload_to="video/%y", filename=f"{i}.mp4")
    video = models.FileField(upload_to="video/%y")
    
    text = models.TextField(max_length=1000, default=txt)


    def __str__(self):
        return self.caption
