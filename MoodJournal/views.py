from django.shortcuts import render
from django.http import HttpResponse
from .models import Journal

# Create your views here.

def index(request):
    return render(request, "Journal/index.html", {
        "journals": Journal.objects.all()
    })

def v1(response):
    return HttpResponse("<h1>View 1!</h1>")