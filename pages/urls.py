from django.urls import path
from .views import HomePageView, ContactView, BookreqView, FaqView
from . import views 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:slug>/', views.category, name='category'), 
    path('contact/', views.ContactView, name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('bookreq/', views.BookreqView, name='bookreq'),
]
