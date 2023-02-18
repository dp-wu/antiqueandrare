# from django.contrib.auth.models import User
from django.db import models

class AgeGroupCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta: 
        ordering = ('name',)
        verbose_name_plural = 'Age Group Categories'


    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    age_group = models.CharField(max_length=255)    
    image = models.ImageField(upload_to='book_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner_user_id = models.ForeignKey('account.CustomUser', related_name='books', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title