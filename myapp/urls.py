from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('chat/', views.chat, name='chat'),         # Страница чата
    path('chat-api/', views.chat, name='chat_api'), # API для AJAX-запросов
]
