from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    CATEGORY_CHOICES = [
        ('Суши', 'Суши'),
        ('Роллы', 'Роллы'),
        ('Сашими', 'Сашими'),
        ('Супы', 'Супы'),
        ('Гарниры', 'Гарниры'),
        ('Напитки', 'Напитки'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_bot = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'Bot' if self.is_bot else self.user.username}: {self.message}"
