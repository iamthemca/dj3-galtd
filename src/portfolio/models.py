from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Category(models.Model):
    title= models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Author(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    def __str__(self):
        return self.user.username
class Portfolio(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)


    def __str__(self):
        return self.title
