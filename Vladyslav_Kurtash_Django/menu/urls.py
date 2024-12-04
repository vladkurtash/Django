from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('secondPage', views.second_page, name='secondPage'),
    path('create/', views.create_post, name='create_post'),
]