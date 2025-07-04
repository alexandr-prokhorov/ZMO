from django.contrib import admin

from villages.models import Village

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели Village (Поселок).

    Настройки отображения списка поселков в админ-панели Django.
    Позволяет управлять и просматривать поселки с возможностью сортировки и фильтрации.
    """
    list_display = ('name', 'price', 'distance_mkad', 'communications')
    ordering = ('name',)
