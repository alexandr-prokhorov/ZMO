from django.urls import path
from houses.views import HouseListView, HouseDetailView

urlpatterns = [
    path('houses/', HouseListView.as_view(), name='house-list'),
    path('houses/<int:pk>/', HouseDetailView.as_view(), name='house-detail'),
    ]