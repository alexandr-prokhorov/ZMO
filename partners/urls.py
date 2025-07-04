from django.urls import path
from .views import partners_list

urlpatterns = [
    path('partners/', partners_list, name='partners_list'),
]
