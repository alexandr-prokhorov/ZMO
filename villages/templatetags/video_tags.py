from django import template
import re

register = template.Library()


@register.filter
def get_video_embed_url(url):
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
