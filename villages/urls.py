from django.urls import path
from .views import VillageListView, VillageDetailView

urlpatterns = [
    path('', VillageListView.as_view(), name='village_list'),
    path('<int:pk>/', VillageDetailView.as_view(), name='village-detail'),
]