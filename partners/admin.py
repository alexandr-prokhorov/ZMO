from django.contrib import admin
from partners.models import Partners
from django.utils.html import format_html
from django.utils.safestring import mark_safe


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Partners.

    Настройки отображения и управления партнерами в админ-панели с поддержкой SVG изображений
    и специальными методами отображения данных.

    Attributes:
         list_display (tuple): Поля для отображения в списке:
            - name: Название партнера
            - display_svg_image: Логотип (форматированное отображение)
            - registration: Регистрация
            - reservation: Бронирование
            - short_address: Укороченный адрес
            - yandex_map_link: Ссылка на Яндекс.Карту
        list_filter (tuple): Фильтры для списка ('registration', 'reservation')
        search_fields (tuple): Поля для поиска ('name', 'address')
        ordering (tuple): Сортировка по имени ('name')
        list_per_page (int): Количество элементов на странице (20)
        readonly_fields (tuple): Только для чтения ('display_svg_preview')
    """
    list_display = ('name', 'display_svg_image', 'registration', 'reservation', 'short_address', 'yandex_map_link')
    list_filter = ('registration', 'reservation')
    search_fields = ('name', 'address')
    ordering = ('name',)
    list_per_page = 20
    readonly_fields = ('display_svg_preview',)

    def display_svg_image(self, obj):
        """Отображает логотип партнера (50x50px) с поддержкой SVG.

        Args:
            obj (Partners): Объект партнера

        Returns:
             str: HTML-код для отображения изображения или "-" если нет изображения
        """
        if obj.image:
            if obj.image.name.lower().endswith('.svg'):
                return format_html(
                    '<div style="width: 50px; height: 50px;">{}</div>',
                    mark_safe(open(obj.image.path).read())
                )
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"

    display_svg_image.short_description = 'Логотип'

    def display_svg_preview(self, obj):
        """Отображает превью логотипа (200px) с поддержкой SVG.

        Args:
             obj (Partners): Объект партнера

        Returns:
             str: HTML-код для отображения превью или "Нет изображения"
        """
        if obj.image and obj.image.name.lower().endswith('.svg'):
            return format_html(
                '<div style="width: 200px; height: 200px;">{}</div>',
                mark_safe(open(obj.image.path).read())
            )
        elif obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        return "Нет изображения"

    display_svg_preview.short_description = 'Превью логотипа'

    def short_address(self, obj):
        """Возвращает укороченную версию адреса (максимум 50 символов).

        Args:
            obj (Partners): Объект партнера

        Returns:
            str: Укороченный адрес или "-" если адрес отсутствует
        """
        if obj.address:
            return f"{obj.address[:50]}..." if len(obj.address) > 50 else obj.address
        return "-"

    short_address.short_description = 'Адрес'

    def yandex_map_link(self, obj):
        """Генерирует кликабельную ссылку на Яндекс.Карту.

        Args:
            obj (Partners): Объект партнера

        Returns:
            str: HTML-ссылка или "-" если ссылка отсутствует
        """
        if obj.yandex_map:
            return format_html('<a href="{}" target="_blank">Открыть карту</a>', obj.yandex_map)
        return "-"

    yandex_map_link.short_description = 'Яндекс Карта'
