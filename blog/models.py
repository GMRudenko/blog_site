from django.db import models
from django.contrib.auth.models import User

class MainBlog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title



class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    main_blog=models.ForeignKey('MainBlog')
    
    def __str__(self):
        return str(self.title)+str(self.main_blog.field['author'])
