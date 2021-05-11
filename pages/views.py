from django.views.generic import TemplateView
from .models import Categories
from .models import Contact
from django.views.generic import ListView


# from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/index.html'


class CategoriesView(ListView):
    model = Categories
    template_name = 'pages/categories.html'
    context_object_name = 'all_pages_list'

class BookreqView(TemplateView):
    template_name = 'pages/bookreq.html'

class ContactView(TemplateView):
    model = Contact
    template_name = 'pages/contact.html'


# def contact(request):
#     if request.method == "POST":
#         contact = Contact()
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         contact.name = name
#         contact.email = email
#         contact.message = message
#         contact.save()
#         return HttpResponse ("<h2>Thanks for contacting us</h2>")
#     return render(request, 'pages/contact.html')

# def post(self, request):
#     form = HomeForm(request.POST)
#     if form.is_valid():
#         text = form.cleaned_data('post')
