from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    email =  models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=200)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)