from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Кастомная модель пользователя, где вместо username используется email.
    Наследуется от стандартной AbstractUser и расширяется дополнительными полями.
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Эл.Почта')
    phone = models.CharField(max_length=35, verbose_name='Номер Телефона', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Телеграм', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """Строковое представление пользователя (используется email)."""
        return f'{self.email}'

    class Meta:
        """Мета-настройки модели пользователя."""
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
