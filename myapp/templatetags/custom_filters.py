from django import template

register = template.Library()

@register.filter
def filter_category(menu_items, category_name):
    """Фильтрует элементы меню по категории"""
    return [item for item in menu_items if item.category == category_name]

@register.filter
def split(value, delimiter):
    """Разделяет строку по разделителю (аналог str.split())"""
    return value.split(delimiter)