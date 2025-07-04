from django.db import models

from users.models import NULLABLE


class House(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    preview_image = models.ImageField(upload_to='house_cards/', **NULLABLE, verbose_name='Превью дома')
    price = models.CharField(max_length=100, verbose_name='Цена')
    size = models.CharField(max_length=250, **NULLABLE, verbose_name='Габариты')
    photo_house = models.ImageField(upload_to='houses/', **NULLABLE, verbose_name='Фото дома')
    floor = models.PositiveIntegerField(**NULLABLE, verbose_name='Количество этажей')
    total_area = models.CharField(max_length=250, **NULLABLE, verbose_name='Строительная площадь')
    bedroom = models.PositiveIntegerField(**NULLABLE, verbose_name='Спальни')
    bathroom = models.PositiveIntegerField(**NULLABLE, verbose_name='Санузел')
    living_room_area = models.CharField(max_length=100, **NULLABLE, verbose_name='Площадь гостиной')
    terrace_count = models.PositiveIntegerField(**NULLABLE, verbose_name='Террасы и балконы')
    description = models.TextField(**NULLABLE, verbose_name='Подробное описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'house'
        verbose_name_plural = 'houses'


class HousePlan(models.Model):
    plan = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name='План дома и фасадов')
    plan_image = models.ImageField(upload_to='house_plans/', **NULLABLE, verbose_name='План дома и фасадов')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')

    class Meta:
        verbose_name = 'house_plan'
        verbose_name_plural = 'house_plans'
        ordering = ['order']

    def __str__(self):
        return f"План {self.plan.name} (#{self.order})"


class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name='Дом')
    image = models.ImageField(upload_to='house_images/', **NULLABLE, verbose_name='Изображение')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')

    class Meta:
        verbose_name = 'house_image'
        verbose_name_plural = 'house_images'
        ordering = ['order']

    def __str__(self):
        return f'Фото {self.image.name} (#{self.order})'
