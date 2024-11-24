from django.shortcuts import render
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'
class AboutPgeView(TemplateView):
    template_name = 'about.html'
class ContactPageView(TemplateView):
    template_name = 'contact.html'