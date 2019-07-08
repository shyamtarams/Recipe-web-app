from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')
    description = models.TextField(null='True')
    likes = models.ManyToManyField(User, related_name='likes', blank='True')
    author = models.ForeignKey(User,  on_delete=models.CASCADE, null='True')
    publish_date = models.DateField(null='True')
    #a =models.ManyToManyField(User,related_name='add', blank='True')

    def __str__(self):
        return' {} {} {} '.format(self.title, self.description, self.publish_date)

    def total_likes(self):
        return self.likes.count()
    '''def likes_name(self):
        return self.likes.username'''


'''class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models)
    user = models.ForeignKey(User, on_delete=models)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{} {}'.format(self.post.title, str(self.user.username))'''
