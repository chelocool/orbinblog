from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('<slug:slug>/', detallePost, name= 'detalle_post'),
    path('post', post, name='post'),
    path('contacto', contacto , name="contacto"),

  
]