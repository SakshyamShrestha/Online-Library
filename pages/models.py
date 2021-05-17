from django.db import models

# Create your models here.

# models for categories
class Categories(models.Model):
    # text row for title 
    text = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.text


#model for contact form
class Contact(models.Model):

    # fields for user's name, email and message respectively 
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    # return's user's name
    def __str__(self):
        return self.name

#model for books
class Books(models.Model):
    # fields for book's name, image and category respectively 
    title = models.CharField(unique=True, max_length=200)
    image = models.ImageField(upload_to = "images/", default= 'test')
    category = models.CharField(max_length = 200, default= "miscellaneous")

    # return's book's name
    def __str__(self):
        return self.title

#model for book requests
class BookRequest(models.Model):
     # fields for user's name, book's name. email and return date respectively 
    full_name = models.CharField(max_length=200, default= '', null='true')
    book_name = models.CharField(max_length=200, default= '', null='true')
    email = models.EmailField()
    date = models.DateField()

    # return's user's name
    def __str__(self):
        return self.full_name
