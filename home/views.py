from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Init

# Create your views here.
def index(request):
    title = "home app title var"
    return render(request, 'home/index.html', {'title': title})

