from django.urls import path
from houses.views import HouseListView, HouseDetailView, ContactsView, InfoView, IndexView

urlpatterns = [
    path('', HouseListView.as_view(), name='house-list'),
    path('<int:pk>/', HouseDetailView.as_view(), name='house-detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('info/', InfoView.as_view(), name='info_company'),
    path('index/', IndexView.as_view(), name='index'),
]
