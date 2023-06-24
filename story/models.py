from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

        