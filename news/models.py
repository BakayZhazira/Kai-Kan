from django.db import models

class MenuItem(models.Model):
    name = models.CharField('Название блюда', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    category = models.CharField('Категория', max_length=50)
    image = models.ImageField('Фото блюда', upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Меню'
