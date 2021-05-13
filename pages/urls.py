from django.urls import path
from .views import HomePageView, CategoriesView, ContactView, BookreqView, FaqView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    # path('<slug:slug>/', Categorie ).
    path('contact/', ContactView.as_view(), name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('bookreq/', BookreqView.as_view(), name='bookreq'),
    

]
