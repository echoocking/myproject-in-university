# coding=utf-8
from django.shortcuts import render
from tools.forms import UserForm
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import User
from tools.forms import Form, userdetilForm
from django.contrib.auth.models import make_password
from django.contrib.auth.models import check_password

def index(request):
    return render(request, '../templates/login.html')

def orig(request):
    return render(request, '../../templates/templates/regsucc.html')
# if request.method == 'POST':
#         uf = UserForm(request.POST)
#         if uf.is_valid():
#             #获取表单用户密码
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             #获取的表单数据与数据库进行比较
#             user = User.objects.filter(username__exact = username,password__exact = password)
#             if user:
#                 return render_to_response('success.html',{'username':username})
#             else:
#                 return HttpResponseRedirect('/login/')
#     else:
#         uf = UserForm()
#     return render_to_response('login.html',{'uf':uf})
# if user:
#                 #比较成功，跳转index
#                 response = HttpResponseRedirect('/online/index/')
#                 #将username写入浏览器cookie,失效时间为3600
#                 response.set_cookie('username',username,3600)
#                 return response
#             else:
#                 #比较失败，还在login
#                 return HttpResponseRedirect('/online/login/')
def login(request):
    if request.method == 'POST':#当提交表单时
        form = UserForm(request.POST)
        if form.is_valid():#当表单合法
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']# 获取表单
            # mk = make_password(password)
            # ck = check_password(password, mk)
           # User.objects.create(username= username,password=password)
            usr1 = User.objects.filter(email=email)
            if usr1:
                usr = User.objects.get(email=email)
            else: usr = 0
            if usr:
                ck = check_password(password, usr.password)
                response = HttpResponseRedirect('/firpage')
                response.set_cookie('username', usr.username, 3600)
                response.set_cookie('id', usr.id, 3600)
                return response
            else:
                return HttpResponse("NO USER")
            # return render(request, 'test.html')
        else:
            # print form.username
            return HttpResponse("FORM IS NOT VALID")
    # elif request.method == 'GET':
    #         return render_to_response(request, 'regsucc.html')
    else:
        return render_to_response(request, 'test.html')

def register(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['password'], None, 'pbkdf2_sha256')
            email = form.cleaned_data['email']
            User.objects.create(username=username, password=password, email=email)
            response = HttpResponseRedirect("")
            response.set_cookie('username', username, 3600)
            return response
        # repassword = form.cleaned_data['repassword']
           # User.objects.create(username=username, password=password)
        else:
            return HttpResponse("wrong form")
    else:
        return HttpResponseRedirect('/accounts/login')

def logout(req):
    response = HttpResponseRedirect('/firpage')
    response.delete_cookie('username')
    return response

def showimfor(req):
    id = req.GET.get('id_info', 'error')
    class_all = User.objects.get(id = id)
    dic = {'class_all': class_all}
    return render_to_response('userdetil.html', dic)


def userimfordetil(req):
     id = req.GET.get('id_info', "")
     # id = 21
     class_all = User.objects.get(id=id)
     dic = {'class_all': class_all}
     # if req.method == 'POST' or req.method == 'GET':
     key = req.COOKIES.get('username')
     form = userdetilForm(req.POST)
     if req.method == "POST":
         if key == class_all.username:
             # username = uf.cleaned_data['username']
             if form.is_valid():
                 name = form.cleaned_data['name']
                 userdescribe = form.cleaned_data['message']
                 number = form.cleaned_data['number']
                 address = form.cleaned_data['address']

                 class_all.name = name
                 class_all.userdescribe = userdescribe
                 class_all.number = number
                 class_all.address = address
                 class_all.save()
             # dic1 = {'class_all': class_all}
                 response = HttpResponseRedirect("/firpage")
                 return response
         # else:
         #    return render_to_response('userdetil.html', dic)
             # , context_instance=RequestContext(req)
         else:
             return HttpResponse("请不要瞎改别人的东西")
     else:
         return HttpResponse("nopost")
