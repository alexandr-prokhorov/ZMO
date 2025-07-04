from django.contrib import admin

from houses.models import House, HousePlan, HouseImage


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели House.

    Настройки отображения и управления домами в админ-панели.

    Attributes:
        list_display (tuple): Поля для отображения в списке:
            - name: Название дома
            - price: Цена
            - size: Габариты
            - floor: Количество этажей
            - bedroom: Количество спален
            - bathroom: Количество санузлов
        ordering (tuple): Поле для сортировки ('name')
    """
    list_display = ('name', 'price', 'size', 'floor', 'bedroom', 'bathroom')
    ordering = ('name',)


@admin.register(HousePlan)
class HousePlanAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели HousePlan.

    Настройки отображения и управления планами домов в админ-панели.

    Attributes:
        list_display (tuple): Поля для отображения в списке:
            - plan: Связанный дом
            - order: Порядок сортировки
        ordering (tuple): Сортировка по первичному ключу ('pk')
    """
    list_display = ('plan', 'order')
    ordering = ('pk',)


@admin.register(HouseImage)
class HouseImageAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели HouseImage.

    Настройки отображения и управления изображениями домов в админ-панели.

    Attributes:
        list_display (tuple): Поля для отображения в списке:
            - image: Изображение дома
             - order: Порядок сортировки
        ordering (tuple): Сортировка по первичному ключу ('pk')
    """
    list_display = ('image', 'order')
    ordering = ('pk',)
