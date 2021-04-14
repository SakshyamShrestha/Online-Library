from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/index.html'

class CategoriesView(TemplateView):
    template_name = 'pages/categories.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'
