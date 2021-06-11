from pages.models import Expert
from django.shortcuts import render
from .models import Expert

# Create your views here.

def home(request):
    experts = Expert.objects.all()
    data = {
        'experts': experts
    }
    return render(request, "pages/home.html", data)

def survey(request):
    return render(request, "pages/survey.html")

def thank_you(request):
    return render(request, "pages/thank_you.html")