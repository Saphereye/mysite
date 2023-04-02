from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('egg', views.easter_egg, name='easter_egg'),
]