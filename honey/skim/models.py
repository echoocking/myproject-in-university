from django.db import models
from django.contrib import admin

# Create your models here.
class Imfromation(models.Model):
    bookname = models.CharField(max_length=1000)
    classify = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    discribe = models.CharField(max_length=10000000)
    username = models.CharField(max_length=100)
    booknumber = models.CharField(max_length=10)
    picturename = models.FileField(upload_to='./uplodeimages/', default='image/no-img.jpg')
    # def __unicode__(self):
    #     return self.classify

class INFORAdmin(admin.ModelAdmin):
    list_display = ('id','username','bookname', 'classify', 'price', 'discribe','picturename','booknumber')
# admin.site.
# def __unicode__(self):
#         return self.username
admin.site.register(Imfromation, INFORAdmin)

# class ExampleModel(models.Model):
#     model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')