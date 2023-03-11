from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insertar_persona/', views.insertar_persona, name='insertar_persona'),
    path('insertar_auto/', views.insertar_auto, name='insertar_auto'),
    path('insertar_ciudad/', views.insertar_ciudad, name='insertar_ciudad'),
    path('buscar_persona/', views.buscar_persona, name='buscar_persona'),
    path('buscar_auto/', views.buscar_auto, name='buscar_auto'),
    path('buscar_ciudad/', views.buscar_ciudad, name='buscar_ciudad'),
]

