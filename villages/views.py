from django.views.generic import ListView, DetailView

from villages.models import Village


class VillageListView(ListView):
    """
    Представление для отображения списка всех поселков.

    Наследуется от Django ListView и предоставляет:
    - Пагинацию (если требуется)
    - Фильтрацию (может быть добавлена)
    - Сортировку по умолчанию (определяется в модели)
    """
    model = Village
    template_name = 'villages/village_list.html'
    context_object_name = 'villages'


class VillageDetailView(DetailView):
    """
    Представление для детального просмотра конкретного поселка.

    Наследуется от Django DetailView и предоставляет:
    - Полную информацию о поселке
    - Доступ к связанным объектам (если есть)
    - Дополнительный медиа-контент
    """
    model = Village
    template_name = 'villages/village_detail.html'
    context_object_name = 'village'
