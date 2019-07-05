

from django.db import models


class Upload(models.Model):
    title = models.TextField(null='True')
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title














