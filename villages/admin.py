from django.contrib import admin

from villages.models import Village


@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'distance_mkad', 'communications')
    ordering = ('name',)
