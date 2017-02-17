#coding:utf-8
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from accounts.models import User


# Create your views here.
from django.shortcuts import render

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, '../../templates/../accounts/templates/../templates/../templates/login.html')

