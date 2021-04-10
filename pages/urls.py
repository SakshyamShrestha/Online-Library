# pages/urls.py

from django.urls import path
from .views import HomePageView, RegFormView, LoginPageView, CategoriesView, ContactView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('registration/', RegFormView.as_view(), name='regform'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('contact/', ContactView.as_view(), name='contact'),
]
