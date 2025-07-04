from django.shortcuts import render
from .models import Partners


def partners_list(request):
    partners = Partners.objects.all()
    return render(request, 'partners/partners_list.html', {'partners': partners})
