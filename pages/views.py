from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import *


# from django.http import HttpResponse

# Create your views here.
class HomePageView(ListView):
    model = Books
    # books = Book.objects.all()
    template_name = 'pages/index.html'
    context_object_name = 'all_pages_list'
    # context_object_name = 'book'
    # queryset = Book.object.all()
    # class CategoriesView(ListView):
    #     model = Categories
    #     template_name = 'pages/categories.html'
    #     context_object_name = 'all_pages_list'

def categories(request):
    categories = Categories.objects.all() 
    return render(request, 'pages/categories.html', {'categories':categories})

# Function based view for slug
def category(request, slug): 
    category = Categories.objects.get(slug=slug)
    return render(request, 'pages/category.html', {'category': category})

def BookreqView(request):
    return render(request, 'pages/bookreq.html')

def new_bookreq(request):
    full_name = request.POST.get('full_name')
    book_name = request.POST.get('book_name')
    email = request.POST.get('email')
    date = request.POST.get('date')
    bookreq_details = BookRequest(full_name=full_name, book_name=book_name, email=email, date=date)
    bookreq_details.save()
    return render(request, 'pages/bookreq.html')

class FaqView(TemplateView):
    model = Contact
    template_name = 'pages/faq.html'

def ContactView(request):
    return render(request, 'pages/contact.html')

def new_contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    contact_details = Contact(name=name, email=email, message=message)
    contact_details.save()
    return render(request, 'pages/contact.html')