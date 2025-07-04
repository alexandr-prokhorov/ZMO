from django.views.generic import ListView, DetailView

from villages.models import Village


class VillageListView(ListView):
    model = Village
    template_name = 'villages/village_list.html'
    context_object_name = 'villages'


class VillageDetailView(DetailView):
    model = Village
    template_name = 'villages/village_detail.html'
    context_object_name = 'village'
