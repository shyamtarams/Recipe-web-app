from django.db import models

# Create your models here.

from django.db import models

from posts.models import Post
'''class Comment(models.Model):

    comment = models.TextField(null='True')
    user_id = models.ForeignKey(Post, on_delete=models.CASCADE),
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE),
    #ForeignKey(Reporter, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment'''
