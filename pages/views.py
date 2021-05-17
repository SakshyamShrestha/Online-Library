from django.shortcuts import render, redirect
#imports template view
from django.views.generic import TemplateView
# imports list view 
from django.views.generic import ListView

# imports all tables from models.py
from .models import *


# from django.http import HttpResponse

# Create your views here.

#class based view for home page
class HomePageView(ListView):
    model = Books
    template_name = 'pages/index.html'
    context_object_name = 'all_pages_list'

#function based view for categories
def categories(request):
    categories = Categories.objects.all() 
    return render(request, 'pages/categories.html', {'categories':categories})

#function based view for request book page
def BookreqView(request):
    return render(request, 'pages/bookreq.html')

#function based view for book requests
def new_bookreq(request):
    full_name = request.POST.get('full_name')
    book_name = request.POST.get('book_name')
    email = request.POST.get('email')
    date = request.POST.get('date')
    bookreq_details = BookRequest(full_name=full_name, book_name=book_name, email=email, date=date)
    bookreq_details.save()
    return render(request, 'pages/bookreq.html')

#class based view for faqs
class FaqView(TemplateView):
    model = Contact
    template_name = 'pages/faq.html'

#function based view for contact page
def ContactView(request):
    return render(request, 'pages/contact.html')

#function based view for contacts
def new_contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    contact_details = Contact(name=name, email=email, message=message)
    contact_details.save()
    return render(request, 'pages/contact.html')