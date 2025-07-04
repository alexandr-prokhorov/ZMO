from django.db import models

from users.models import NULLABLE


class House(models.Model):
    """Модель дома/коттеджа с основными характеристиками.

    Attributes:
        name (str): Название дома.
        preview_image (ImageField): Превью-изображение для карточки.
        price (str): Цена дома (строка, чтобы можно было добавить валюту или доп. условия).
        size (str): Габариты дома (например, '10x15м').
        photo_house (ImageField): Основное фото дома.
        floor (int): Количество этажей.
        total_area (str): Общая строительная площадь (например, '150 кв.м').
        bedroom (int): Количество спален.
        bathroom (int): Количество санузлов.
        living_room_area (str): Площадь гостиной.
        terrace_count (int): Количество террас/балконов.
        description (str): Подробное описание дома.
    """
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
        """Строковое представление объекта (название дома)."""
        return self.name

    class Meta:
        """Мета-класс для настроек модели."""
        verbose_name = 'house'
        verbose_name_plural = 'houses'


class HousePlan(models.Model):
    """Модель плана дома (планировки и фасадов), связанная с основным домом.

    Attributes:
        plan (ForeignKey): Связь с основной моделью дома (House).
        plan_image (ImageField): Изображение плана дома/фасадов.
        order (int): Порядок сортировки планов (для отображения в нужной последовательности).
    """
    plan = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name='План дома и фасадов')
    plan_image = models.ImageField(upload_to='house_plans/', **NULLABLE, verbose_name='План дома и фасадов')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')

    class Meta:
        """Мета-класс для дополнительных настроек модели."""
        verbose_name = 'house_plan'
        verbose_name_plural = 'house_plans'
        ordering = ['order']

    def __str__(self):
        """Строковое представление объекта в формате: 'План {название_дома} (#{порядковый_номер})'."""
        return f"План {self.plan.name} (#{self.order})"


class HouseImage(models.Model):
    """Модель для хранения изображений, связанных с домом.

    Позволяет хранить несколько фотографий для одного дома с возможностью сортировки.

    Attributes:
        house (ForeignKey): Связь с основным объектом дома. При удалении дома все связанные изображения
            будут удалены каскадно.
        image (ImageField): Файл изображения дома. Загружается в папку 'house_images/'.
            Поддерживает форматы: JPEG, PNG, WEBP.
        order (PositiveIntegerField): Порядковый номер для сортировки изображений. По умолчанию 0.
            Используется для определения последовательности отображения фотографий.
    """
    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name='Дом')
    image = models.ImageField(upload_to='house_images/', **NULLABLE, verbose_name='Изображение')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')

    class Meta:
        """Мета-настройки модели HouseImage."""
        verbose_name = 'house_image'
        verbose_name_plural = 'house_images'
        ordering = ['order']

    def __str__(self):
        """Строковое представление объекта.

        Returns:
            str: Строка в формате 'Фото {имя_файла} (#{порядковый_номер})'
        """
        return f'Фото {self.image.name} (#{self.order})'
