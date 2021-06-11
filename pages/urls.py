from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('survey', views.survey, name="survey"),
    path("thank-you", views.thank_you, name="thank-you"),
]