from django.db import models
from django.contrib.auth import get_user_model

class public(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    file = models.ImageField(upload_to='uploads')
