from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Categories)
admin.site.register(Books)

@admin.register(BookRequest)
class BookRequest(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'book_name', 'email', 'date')

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
