from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='books/')
    thumbnail = models.ImageField(upload_to='books/thumbnails/', blank=True)