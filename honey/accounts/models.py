from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    userdescribe = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    number = models.CharField(max_length=5)

# class Userdetil(models.Model):



    #passwordconfirm = models.CharField(max_length= 50)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'name', 'userdescribe', 'address', 'number')
admin.site.register(User, UserAdmin)
    # def __unicode__(self):
    #     return self.username