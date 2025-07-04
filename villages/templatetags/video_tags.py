from django import template
import re

register = template.Library()


@register.filter
def get_video_embed_url(url):
    """
    Шаблонный фильтр для преобразования URL видео в embed-версию.

    Поддерживает платформы:
    - YouTube (youtube.com, youtu.be)
    - RuTube (rutube.ru)

    Параметры:
        url (str): Исходный URL видео

    Возвращает:
        str: URL для встраивания через iframe или исходный URL, если платформа не распознана

    Примеры использования:
        {{ video_url|get_video_embed_url }}
        {% if video_url|get_video_embed_url != video_url %}
            <iframe src="{{ video_url|get_video_embed_url }}"></iframe>
        {% endif %}
    """
    # Для YouTube
    youtube_match = re.match(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?([a-zA-Z0-9_-]+)',
                             url)
    if youtube_match:
        video_id = youtube_match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"

    # Для Rutube
    rutube_match = re.match(r'(?:https?:\/\/)?(?:www\.)?rutube\.ru\/video\/([a-zA-Z0-9_-]+)', url)
    if rutube_match:
        video_id = rutube_match.group(1)
        return f"https://rutube.ru/play/embed/{video_id}"

    return url
