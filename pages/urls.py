from django.urls import path
# imports specific views from views.py
from .views import HomePageView, ContactView, BookreqView, FaqView, new_contact, new_bookreq
# imports all views from views.py
from . import views 

#url patterns for the pages
urlpatterns = [
    
    # urls for class as well as function based views 
    path('', HomePageView.as_view(), name='home'),
    path('categories/', views.categories, name='categories'),
    path('contact/', views.ContactView, name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('bookreq/', views.BookreqView, name='bookreq'),
    path('new_contact/', views.new_contact, name='new_contact'),
    path('new_bookreq/', views.new_bookreq, name='new_bookreq'),
]
