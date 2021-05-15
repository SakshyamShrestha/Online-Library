from django.urls import path
from .views import HomePageView, ContactView, BookreqView, FaqView, new_contact, new_bookreq
from . import views 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categories/', views.categories, name='categories'),
    path('contact/', views.ContactView, name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('bookreq/', views.BookreqView, name='bookreq'),
    path('new_contact/', views.new_contact, name='new_contact'),
    path('new_bookreq/', views.new_bookreq, name='new_bookreq'),
]
