from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from houses.models import House, HousePlan, HouseImage
from django.views import View
from django.shortcuts import render
from villages.models import Village


class PaginatedPlansMixin:
    """Миксин для пагинации планов домов.

        Предоставляет метод для разбиения планов дома на страницы с возможностью
        кастомного количества элементов на странице.

    Attributes:
        paginate_plans_by (int): Количество планов на одной странице. По умолчанию 1.
        Может быть переопределено в дочерних классах.
    """
    paginate_plans_by = 1

    def get_plans_context(self, house):
        plans = HousePlan.objects.filter(plan=house).order_by('order')
        paginator = Paginator(plans, self.paginate_plans_by)
        page_number = self.request.GET.get('plans_page', 1)
        return {
            'plans_page_obj': paginator.get_page(page_number),
            'plans_pagination_param': 'plans_page'
        }


class HouseListView(ListView):
    """Стандартное представление для отображения списка домов.

        Наследует функциональность Django ListView для отображения объектов модели House.
        Использует шаблон 'houses/house_list.html' и передает список домов в контексте
        под именем 'houses'.

    Attributes:
        model (Model): Модель House, используемая для получения данных
        template_name (str): Путь к шаблону для рендеринга
        context_object_name (str): Имя переменной контекста для списка домов
    """
    model = House
    template_name = 'houses/house_list.html'
    context_object_name = 'houses'


class HouseDetailView(PaginatedPlansMixin, DetailView):
    """Детальное представление дома с пагинацией планов.

        Наследует функциональность Django DetailView для отображения отдельного дома
        и добавляет пагинацию для связанных планов через PaginatedPlansMixin.

    Attributes:
        model (Model): Модель House для отображения
        template_name (str): Путь к шаблону 'houses/house_detail.html'
        context_object_name (str): Имя переменной контекста для объекта дома
    """
    model = House
    template_name = 'houses/house_detail.html'
    context_object_name = 'house'

    def get_context_data(self, **kwargs):
        """Добавляет в контекст данные пагинации планов дома.

        Returns:
            dict: Контекст с:
                - house: объект дома (основной контекст)
                - plans_page_obj: объект страницы с планами
                - plans_pagination_param: параметр пагинации для планов
        """
        context = super().get_context_data(**kwargs)
        plans_context = self.get_plans_context(self.object)
        context.update(plans_context)
        return context

    def render_to_response(self, context, **response_kwargs):
        """Обрабатывает AJAX-запросы для пагинации планов.

            Для обычных запросов работает стандартный механизм рендеринга.
            Для AJAX-запросов возвращает JSON с HTML планов и данными пагинации.

        Returns:
            HttpResponse | JsonResponse:
                - JsonResponse для AJAX-запросов с данными планов
                - HttpResponse для обычных запросов
        """
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if 'plans_page_obj' not in context:
                return JsonResponse({'error': 'Plans not found'}, status=400)

            plans_html = render_to_string(
                'houses/_plans_partial.html',
                {'plans_page_obj': context['plans_page_obj']}
            )
            return JsonResponse({
                'html': plans_html,
                'has_previous': context['plans_page_obj'].has_previous(),
                'has_next': context['plans_page_obj'].has_next(),
                'current_page': context['plans_page_obj'].number,
                'num_pages': context['plans_page_obj'].paginator.num_pages
            })
        return super().render_to_response(context, **response_kwargs)


class HousePlanListView(ListView):
    """Представление для отображения списка планов домов с пагинацией.

        Отображает все объекты HousePlan, отсортированные по полю 'order'.
        Поддерживает пагинацию по 10 элементов на странице.

    Attributes:
        model (Model): Модель HousePlan для отображения
        template_name (str): Путь к шаблону 'houses/house_plan_list.html'
        context_object_name (str): Имя переменной контекста ('plans')
        paginate_by (int): Количество элементов на странице (10)
        ordering (list): Поле для сортировки (['order'])
    """
    model = HousePlan
    template_name = 'houses/house_plan_list.html'
    context_object_name = 'plans'
    paginate_by = 10
    ordering = ['order']


class HouseImageView(ListView):
    """Представление для отображения списка изображений домов с пагинацией.

        Отображает все объекты HouseImage, отсортированные по полю 'order'.
        Поддерживает пагинацию по 10 элементов на странице.

    Attributes:
        model (Model): Модель HouseImage для отображения
        template_name (str): Путь к шаблону 'houses/house_image_list.html'
        context_object_name (str): Имя переменной контекста ('images')
        paginate_by (int): Количество элементов на странице (10)
        ordering (list): Поле для сортировки (['order'])
    """
    model = HouseImage
    template_name = 'houses/house_image_list.html'
    context_object_name = 'images'
    paginate_by = 10
    ordering = ['order']


class ContactsView(View):
    """Обработчик страницы контактов компании.

        Отображает статическую страницу с контактной информацией.
        Поддерживает только GET-запросы.

    Attributes:
        template_name (str): Путь к шаблону 'houses/contacts.html'
    """
    template_name = 'houses/contacts.html'

    def get(self, request):
        """Обрабатывает GET-запрос для страницы контактов.

        Args:
            request (HttpRequest): Объект запроса

        Returns:
            HttpResponse: Рендер шаблона с контактной информацией
        """
        return render(request, self.template_name)


class InfoView(View):
    """Обработчик страницы информации о компании.

        Отображает статическую страницу с информацией о компании.
        Поддерживает только GET-запросы.

    Attributes:
        template_name (str): Путь к шаблону 'houses/info_company.html'
    """
    template_name = 'houses/info_company.html'

    def get(self, request):
        """Обрабатывает GET-запрос для страницы информации о компании.

        Args:
            request (HttpRequest): Объект запроса

        Returns:
            HttpResponse: Рендер шаблона с информацией о компании
        """
        return render(request, self.template_name)


class IndexView(View):
    """Обработчик главной страницы сайта.

        Отображает главную страницу со списком поселков.
        Поддерживает только GET-запросы.

    Attributes:
        template_name (str): Путь к шаблону 'houses/index.html'
    """
    template_name = 'houses/index.html'

    def get(self, request):
        """Обрабатывает GET-запрос для главной страницы.

        Args:
            request (HttpRequest): Объект запроса

        Returns:
            HttpResponse: Рендер шаблона с контекстом:
                - villages (QuerySet): Список всех поселков
        """
        villages = Village.objects.all()
        context = {
            'villages': villages,
        }
        return render(request, self.template_name, context)
