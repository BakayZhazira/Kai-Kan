from django.shortcuts import render
from .models import MenuItem  # Убедитесь, что у вас модель называется MenuItem, а не Menu

def news_home(request):
    menu_items = MenuItem.objects.all().order_by('category', 'name')  # Правильный запрос
    return render(request, 'news/news.html', {'menu': menu_items})  # Передаем данные в шаблон