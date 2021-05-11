# pages/urls.py

from django.urls import path
from .views import HomePageView, CategoriesView, ContactView, BookreqView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('bookreq/', BookreqView.as_view(), name='bookreq'),

]
