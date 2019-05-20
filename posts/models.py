from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')
    description = models.TextField(null='True')


    def __str__(self):


        return '{} {} '.format(self.title, self.description)

