from django.db import models
import datetime
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')
    description = models.TextField(null='True')
    author = models.ForeignKey(User,  on_delete=models.CASCADE, null='True')
    publish_date = models.DateField(null='True')



    def __str__(self):


        return ' {} {}  {} '.format(self.title, self.description,self.publish_date)

