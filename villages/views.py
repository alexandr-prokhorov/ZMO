from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from villages.models import Village
from django.views import View
from django.shortcuts import render

class VillageListView(ListView):
    model = Village
    template_name = 'villages/village_list.html'
    context_object_name = 'villages'

class VillageDetailView(DetailView):
    model = Village
    template_name = 'villages/village_detail.html'
    context_object_name = 'village'