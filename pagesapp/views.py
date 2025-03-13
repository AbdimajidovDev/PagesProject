from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePageViews(TemplateView):
    template_name = 'home.html'



class AboutPageViews(TemplateView):
    template_name = 'about.html'
