from django.contrib import admin
from partners.models import Partners
from django.utils.html import format_html
from django.utils.safestring import mark_safe

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_svg_image', 'registration', 'reservation', 'short_address', 'yandex_map_link')
    list_filter = ('registration', 'reservation')
    search_fields = ('name', 'address')
    ordering = ('name',)
    list_per_page = 20
    readonly_fields = ('display_svg_preview',)  # Для страницы редактирования

    def display_svg_image(self, obj):
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
        if obj.address:
            return f"{obj.address[:50]}..." if len(obj.address) > 50 else obj.address
        return "-"
    short_address.short_description = 'Адрес'

    def yandex_map_link(self, obj):
        if obj.yandex_map:
            return format_html('<a href="{}" target="_blank">Открыть карту</a>', obj.yandex_map)
        return "-"
    yandex_map_link.short_description = 'Яндекс Карта'

