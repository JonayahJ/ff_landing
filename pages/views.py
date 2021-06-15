from pages.models import Expert
from django.shortcuts import render
from .models import Expert, Advisor

# Create your views here.

def home(request):
    experts = Expert.objects.all().order_by("name")
    advisors = Advisor.objects.all().order_by("name")
    data = {
        'experts': experts,
        'advisors': advisors
    }
    return render(request, "pages/home.html", data)

def survey(request):
    return render(request, "pages/survey.html")

def thank_you(request):
    return render(request, "pages/thank_you.html")