from django.db import models

from users.models import NULLABLE


class Partners(models.Model):
    """Модель для хранения информации о партнерах компании.

    Attributes:
        name (CharField): Название компании-партнера
        image (ImageField): Логотип партнера
        registration (PositiveIntegerField): Услуги по оформлению
        reservation (PositiveIntegerField): Услуги по платной брони
        address (TextField): Полный адрес партнера
        yandex_map (TextField): Код или ссылка для встраивания Яндекс.Карт

    Meta:
        verbose_name (str): Имя модели в единственном числе
        verbose_name_plural (str): Имя модели во множественном числе
    """
    name = models.CharField(max_length=250, verbose_name='Название компании')
    image = models.ImageField(upload_to='partners/', **NULLABLE, verbose_name='Логотип партнера')
    registration = models.PositiveIntegerField(**NULLABLE, verbose_name='Оформление')
    reservation = models.PositiveIntegerField(**NULLABLE, verbose_name='Платная бронь')
    address = models.TextField(**NULLABLE, verbose_name='Адрес')
    yandex_map = models.TextField(**NULLABLE, verbose_name='яндекс карта')

    def __str__(self):
        """Строковое представление объекта.

        Returns:
            str: Имя файла логотипа или пустая строка
        """
        return self.image.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
