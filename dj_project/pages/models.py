from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    code = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=50, default='General')
    optional_field = models.CharField(max_length=50, null=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    summary = models.TextField(default="No summary available")

class Person_p(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Product_p(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    rating = models.IntegerField(blank=True, null=True)
    price = models.FloatField()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField(unique=True)

class Measurement(models.Model):
    value = models.FloatField(blank=True, null=True)
    percentage = models.FloatField(default=0.0)

class Document(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)

class Event(models.Model):
    name = models.CharField(max_length=100)
    event_time = models.DateTimeField(default=datetime.now)

class OptionalTimestamp(models.Model):
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(blank=True, null=False)

class UserProfile(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)

class Newsletter(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True, max_length=254)
    subscription_date = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default="example@example.com", max_length=254)

#########################################

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True, unique=True)
    author = models.OneToOneField(Author,
                               on_delete= models.CASCADE,
                               related_query_name='post',
                               unique=True)
    rating = models.IntegerField()

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering= ['publication_date']

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    books = models.OneToOneField(Book,on_delete= models.CASCADE,
                               related_query_name='post',
                               unique=True
                                 )

    class Meta:
        verbose_name_plural = "Видавництва"

class Category(models.Model):
    name = models.CharField(max_length=100, unique_for_month='event_date')