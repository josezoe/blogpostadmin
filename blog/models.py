from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)

    def _str_(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def _str_(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=30,unique=True) 


    def _str_(self):
        return self.name
    

class Post(models.Model):
    title=models.CharField(max_length=255)    
    content=models.TextField()
    published_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='post')
    categories=models.ManyToManyField(Category,related_name='post')
    tags=models.ManyToManyField(Tag,related_name='post')

    def _str_(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # One-to-Many
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'