from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostCategory(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)
    # author = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, blank=True, null=True)
    cover = models.ImageField(upload_to='images', blank=True, null=True)
    

    def __str__(self):
        return self.title

    @property
    def get_photo_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url
        else:
            return "/static/images/1.jpg"
