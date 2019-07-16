from django.db import models
from ckeditor.fields import RichTextField
class Type(models.Model):
    name = models.CharField(max_length=32)
    desctiption = RichTextField()
    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    desctiption = RichTextField()
    content = RichTextField()
    time = models.DateField()
    picture = models.ImageField(upload_to="images")

    tui = models.IntegerField() #0 代表不推荐 1代表推荐
    click = models.IntegerField() #点击+1
    types = models.ForeignKey(to=Type,on_delete=True) #外键

class Picture(models.Model):
    image = models.ImageField(upload_to="images")
    label = models.CharField(max_length=32)
    desctiption = RichTextField()

# Create your models here.
