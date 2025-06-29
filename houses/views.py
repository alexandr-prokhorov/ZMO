from symtable import Class

from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from houses.models import House, HousePlan, HouseImage
from django.views import View
from django.shortcuts import render
from villages.models import Village


class PaginatedPlansMixin:
    paginate_plans_by = 1

    def get_plans_context(self, house):
        plans = HousePlan.objects.filter(plan=house).order_by('order')
        paginator = Paginator(plans, self.paginate_plans_by)
        page_number = self.request.GET.get('plans_page', 1)
        return {
            'plans_page_obj': paginator.get_page(page_number),
            'plans_pagination_param': 'plans_page'
        }


class HouseListView(ListView):
    model = House
    template_name = 'houses/house_list.html'
    context_object_name = 'houses'


class HouseDetailView(PaginatedPlansMixin, DetailView):
    model = House
    template_name = 'houses/house_detail.html'
    context_object_name = 'house'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plans_context = self.get_plans_context(self.object)
        context.update(plans_context)
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if 'plans_page_obj' not in context:
                return JsonResponse({'error': 'Plans not found'}, status=400)

            plans_html = render_to_string(
                'houses/_plans_partial.html',
                {'plans_page_obj': context['plans_page_obj']}
            )
            return JsonResponse({
                'html': plans_html,
                'has_previous': context['plans_page_obj'].has_previous(),
                'has_next': context['plans_page_obj'].has_next(),
                'current_page': context['plans_page_obj'].number,
                'num_pages': context['plans_page_obj'].paginator.num_pages
            })
        return super().render_to_response(context, **response_kwargs)


class HousePlanListView(ListView):
    model = HousePlan
    template_name = 'houses/house_plan_list.html'
    context_object_name = 'plans'
    paginate_by = 10
    ordering = ['order']

class HouseImageView(ListView):
    model = HouseImage
    template_name = 'houses/house_image_list.html'
    context_object_name = 'images'
    paginate_by = 10
    ordering = ['order']

class ContactsView(View):
    template_name = 'houses/contacts.html'
    def get(self, request):
        return render(request, self.template_name)

class InfoView(View):
    template_name = 'houses/info_company.html'
    def get(self, request):
        return render(request, self.template_name)


class IndexView(View):
    template_name = 'houses/index.html'

    def get(self, request):
        villages = Village.objects.all()
        context = {
            'villages': villages,
            # другие переменные если нужно
        }
        return render(request, self.template_name, context)