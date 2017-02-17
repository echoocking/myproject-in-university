#coding:utf-8
from django.shortcuts import render_to_response
from skim.models import Imfromation
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def show_info(request):
    kind = request.GET.get('kind', '')
    if kind == '':
        kind = "大学"
    class_all = Imfromation.objects.filter(classify=kind)
    dic = {'class_all': class_all, 'kind': kind}
    return render_to_response('detil.html', dic)
# 把需要传递的信息 做成一个字典 通过render_to_response 把字典传入html页面

def search(req):
    search_for = req.GET.get('q', '')
    class_all = Imfromation.objects.filter(bookname__contains=search_for)
    dic = {'class_all': class_all,'kind': search_for}
    return render_to_response('detil.html', dic)





