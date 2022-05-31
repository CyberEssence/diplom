""" 

    Author: Solovov N. G. (CyberEssence)
    
"""

from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse
from proj.models import Post

# создание views приложения core

# рендер главной страницы
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/frontpage.html', {'posts': posts})

# рендер страницы с about
def about(request):
    return render(request, 'core/about.html')


# файл robots.txt с настройками
def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
