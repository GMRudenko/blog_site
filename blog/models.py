from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class MainPost(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{0}:{1}".format(self.author, self.title)
    
    def get_absolute_url(self):
        return reverse('mainpost-detail', args=[str(self.id)])

class CommentManager(models.Manager):
    def create_comment(self, text, author, post):
        comment=self.create(text=text, author=author,main_post=post)
        return comment

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    main_post=models.ForeignKey('MainPost', on_delete=models.SET_NULL, null=True)
    objects=CommentManager()
    
    def __str__(self):
        return "{0},{1}".format(self.id, self.author)


