from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Categories
from .models import Contact
from .models import Books
from django.views.generic import ListView


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


class FaqView(TemplateView):
    model = Contact
    template_name = 'pages/faq.html'

def ContactView(request):
    return render(request, 'pages/contact.html')
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse ("<h2>Thanks for contacting us</h2>")
    return render(request, 'pages/contact.html')