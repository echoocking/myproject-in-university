# coding=utf-8
from django.shortcuts import render
from skim.models import Imfromation
from django.http import HttpResponse, HttpResponseRedirect
from tools.forms import ImforFrom
from accounts.models import User
from django.db import connection, transaction
# Create your views here.


def skim(req):
    return render(req, 'detil.html')

def imfor(req):
    if req.method == 'POST':#当提交表单时
        name = req.COOKIES.get('username')
        result = User.objects.all()
        # try:
        #     reqimg = req.FILES['picfile']
        #     img = Image.open(reqimg)
        #     img.save("images/","png")
        # except Exception,e:
        #     return HttpResponse("Error %s"%e)
        # for login.username in result.username:
        #     user = authenticate(username=result.username, password=result.password)
        form = ImforFrom(req.POST, req.FILES)
        if form.is_valid():#当表单合法
            user = name
            if name == None:
                return HttpResponse("please login!")
            else:
                # picturename = req.FILES.get('picfile')
                picturename = form.cleaned_data['picturename']
                bookname = form.cleaned_data['bookname']
                classify= form.cleaned_data['classify']# 获取表单
                price = form.cleaned_data['price']
                discribe = form.cleaned_data['discribe']
                booknumber = form.cleaned_data['booknumber']
                Imfromation.objects.create(bookname=bookname,
                                           classify=classify,
                                           price=price,
                                           discribe=discribe,
                                           username=user,
                                           picturename=picturename,
                                           booknumber=booknumber)
        else:
            return HttpResponse('CUOLA')
    response = HttpResponseRedirect("/firpage")
    return response

def display(req):
    data = []
    cursor = connection.cursor()
    cursor.execute('select * from Imformation')
    for row in cursor.fetchall():
        print data.append(row[0])
    return HttpResponse()
# 指针(cursor)是一个对象
def up_img(req):
    if req.method == 'POST':
        return HttpResponse('ALLAL')

