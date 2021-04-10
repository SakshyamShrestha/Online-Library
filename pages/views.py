from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class RegFormView(TemplateView):
    template_name = 'regform.html'

class CategoriesView(TemplateView):
    template_name = 'categories.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
