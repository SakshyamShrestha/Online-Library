from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Page
from django.views.generic import ListView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/index.html'

class CategoriesView(ListView):
    model = Page
    template_name = 'pages/categories.html'
    context_object_name = 'all_pages_list'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'
