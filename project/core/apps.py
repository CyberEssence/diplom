""" 

    Author: Solovov N. G. (CyberEssence)
    
"""

from django.apps import AppConfig


# иницилизация приложения с конфигом движка сайта

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
