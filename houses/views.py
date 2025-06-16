from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from houses.models import House

class HouseListView(ListView):
    model = House
    template_name = 'houses/house_list.html'
    context_object_name = 'houses'

class HouseDetailView(DetailView):
    model = House
    template_name = 'houses/house_detail.html'
    context_object_name = 'house'
