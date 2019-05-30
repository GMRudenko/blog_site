from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

class MainPostManager(models.Manager):
    def create_mainpost(self, title, text, author, time):
        post=self.create(title=title, text=text, author=author, time=time)
        return post

class MainPost(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time=models.DateTimeField(default=datetime(2019, 5, 29, 22, 0, 0, 0))
    objects=MainPostManager()


    def __str__(self):
        return "{0}:{1}".format(self.author, self.title)
    
    def get_absolute_url(self):
        return reverse('mainpost-detail', args=[str(self.id)])

class CommentManager(models.Manager):
    def create_comment(self, text, author, post, time):
        comment=self.create(text=text, author=author,main_post=post, time=time)
        return comment

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    main_post=models.ForeignKey('MainPost', on_delete=models.SET_NULL, null=True)
    time=models.DateTimeField(default=datetime(2019, 5, 29, 22, 0, 0, 0))
    objects=CommentManager()
    
    def __str__(self):
        return "{0},{1}".format(self.id, self.author)


