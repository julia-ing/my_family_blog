from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class myText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    img_url = models.FileField(null=True)

    category = models.CharField(max_length=200, null=True)

    board_text = RichTextUploadingField(null=True)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    lecture = models.ForeignKey(myText, on_delete=models.CASCADE)
    writer = models.CharField(max_length=200, null=True)
    rate = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True)
    def publish(self):
        self.save()

    def __str__(self):
        return self.comment

