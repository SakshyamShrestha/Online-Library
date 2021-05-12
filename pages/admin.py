from django.contrib import admin
from .models import Categories
from .models import Books
from .models import Contact

# Register your models here.

admin.site.register(Categories)
admin.site.register(Books)

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
