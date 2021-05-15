from django.db import models

# Create your models here.
class Categories(models.Model):
    text = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.text


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(unique=True, max_length=200)
    image = models.ImageField(upload_to = "images/", default= 'test')
    category = models.CharField(max_length = 200, default= "miscellaneous")

    def __str__(self):
        return self.title

class BookRequest(models.Model):
    full_name = models.CharField(max_length=200, default= '', null='true')
    book_name = models.CharField(max_length=200, default= '', null='true')
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return self.full_name
