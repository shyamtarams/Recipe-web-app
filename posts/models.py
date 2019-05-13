from django.db import models

# Create your models here.]
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')
    title2 = models.TextField()

    def __str__(self):
        # return self.title, self.title2
       # return self.title2
        return '{} {} '.format(self.title, self.title2)

