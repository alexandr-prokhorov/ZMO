from django.contrib import admin

from houses.models import House, HousePlan

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'floor', 'bedroom', 'bathroom')
    ordering = ('name',)


@admin.register(HousePlan)
class HousePlanAdmin(admin.ModelAdmin):
    list_display = ('plan', 'order')
    ordering = ('pk',)
