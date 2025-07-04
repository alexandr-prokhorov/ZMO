from django.shortcuts import render
from .models import Partners


def partners_list(request):
    """Обрабатывает запрос на отображение списка партнеров.

    Возвращает страницу со всеми активными партнерами компании,
    отсортированными по названию компании.

    Args:
       request (HttpRequest): Объект HTTP-запроса

    Returns:
        HttpResponse: Отрендеренный шаблон с контекстом:
         - partners (QuerySet): Список всех партнеров,
            отсортированный по названию компании

    Template:
       partners/partners_list.html
    """
    partners = Partners.objects.all()
    return render(request, 'partners/partners_list.html', {'partners': partners})
