from django.db import models
import re

from users.models import NULLABLE


class Village(models.Model):
    """
    Модель, представляющая поселок в системе.

    Содержит информацию о поселке:
    - Основные данные (название, адрес)
    - Медиа-контент (фото, видео)
    - Характеристики (цена, расстояние от МКАД, коммуникации)
    - Геопозиция (встраиваемая карта)
    """
    name = models.CharField(max_length=250, verbose_name='Название')
    preview_image = models.ImageField(upload_to='village_cards/', **NULLABLE, verbose_name='Превью поселка')
    address = models.CharField(max_length=1000, **NULLABLE, verbose_name='Адрес поселка')
    yandex_map_embed = models.TextField('Код iframe Яндекс.Карт', **NULLABLE,
                                        help_text='Полный HTML-код iframe из Яндекс.Карт')
    photo_village = models.ImageField(upload_to='villages/', **NULLABLE, verbose_name='Фото Поселка')
    price = models.PositiveIntegerField(**NULLABLE, verbose_name='цена за сотку')
    distance_mkad = models.PositiveIntegerField(**NULLABLE, verbose_name='Расстояние от МКАД')
    communications = models.CharField(max_length=250, **NULLABLE, verbose_name='Коммуникации')
    video_url = models.URLField(**NULLABLE, verbose_name='Ссылка на видео', help_text='Ссылка на YouTube или RuTube')
    description = models.TextField(**NULLABLE, verbose_name='Подробное описание')

    def __str__(self):
        """Строковое представление объекта (используется название поселка)."""
        return self.name

    class Meta:
        """Мета-настройки модели Village."""
        verbose_name = 'Поселок'
        verbose_name_plural = 'Поселки'

    @property
    def video_platform(self):
        """
        Определяет видеоплатформу по URL.

        Возвращает:
            str: 'youtube', 'rutube' или None, если платформа не распознана
        """
        if not self.video_url:
            return None
        if 'youtube.com' in self.video_url or 'youtu.be' in self.video_url:
            return 'youtube'
        elif 'rutube.ru' in self.video_url:
            return 'rutube'
        return None

    def get_video_id(self):
        """
        Извлекает идентификатор видео из URL.

        Использует регулярные выражения для различных форматов ссылок.

        Возвращает:
            str: ID видео или None, если не удалось извлечь
        """
        if not self.video_url:
            return None

        if self.video_platform == 'youtube':
            patterns = [
                r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
                r'(?:youtube\.com/embed/)([a-zA-Z0-9_-]{11})'
            ]
        elif self.video_platform == 'rutube':
            patterns = [
                r'rutube\.ru/video/([a-zA-Z0-9_-]+)',
                r'rutube\.ru/play/embed/([a-zA-Z0-9_-]+)'
            ]
        else:
            return None

        for pattern in patterns:
            match = re.search(pattern, self.video_url)
            if match:
                return match.group(1)
        return None

    @property
    def embed_url(self):
        """
        Генерирует URL для встраивания видео на основе распознанной платформы.

        Возвращает:
            str: Готовый URL для iframe или None, если не удалось сгенерировать
        """
        if not self.video_url or not self.video_platform:
            return None

        video_id = self.get_video_id()
        if not video_id:
            return None

        if self.video_platform == 'youtube':
            return f'https://www.youtube.com/embed/{video_id}'
        elif self.video_platform == 'rutube':
            return f'https://rutube.ru/play/embed/{video_id}'
        return None
