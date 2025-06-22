from django.db import models
from django.conf import settings

from users.models import NULLABLE

class Partners(models.Model):

    name = models.CharField(max_length=250, verbose_name='Название компании')
    image = models.ImageField(upload_to='partners/', **NULLABLE, verbose_name='Логотип партнера')
    registration = models.PositiveIntegerField(**NULLABLE, verbose_name='Оформление')
    reservation = models.PositiveIntegerField(**NULLABLE, verbose_name='Платная бронь')
    address = models.TextField(**NULLABLE, verbose_name='Адрес')
    yandex_map = models.TextField(**NULLABLE, verbose_name='яндекс карта')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'