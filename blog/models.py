from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.TextField()
    date = models.DateTimeField()
