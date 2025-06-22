from django.urls import path
from houses.views import HouseListView, HouseDetailView, ContactsView

urlpatterns = [
    path('', HouseListView.as_view(), name='house-list'),
    path('<int:pk>/', HouseDetailView.as_view(), name='house-detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    ]