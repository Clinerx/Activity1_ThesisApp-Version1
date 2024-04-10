from .models import Thesis
from django.shortcuts import render
from django.http import HttpResponse

def thesis_list(request):
    theses = Thesis.objects.all()
    return render(request, 'thesis_list.html', {'theses': theses})

def thesis_detail(request, thesis_id):
    thesis = Thesis.objects.get(id=thesis_id)
    return render(request, 'thesis_detail.html', {'thesis': thesis})
