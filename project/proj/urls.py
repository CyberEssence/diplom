from django.urls import path

""" 

    Author: Solovov N. G. (CyberEssence)
    
"""

from .models import Video

from . import views
from . import funcs

urlpatterns = [
    path('search/', views.search, name='search'),
    path('video/', views.video, name="video")
    #path('', views.index)
]