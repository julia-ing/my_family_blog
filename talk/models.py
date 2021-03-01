from django.db import models

# Create your models here.
class Talk(models.Model):
    content = models.CharField(max_length=300)
    writer = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=20, default=None, null=True)


class Comment(models.Model):
    content = models.CharField(max_length=500)
    writer = models.CharField(max_length=200, null=True)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
