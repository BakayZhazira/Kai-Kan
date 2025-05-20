from django.contrib import admin
from .models import MenuItem
from django.utils.html import format_html

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Превью'

admin.site.register(MenuItem, MenuItemAdmin)
