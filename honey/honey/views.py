#coding:utf-8
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# rejgister
def index(request):
    return HttpResponse('''<a href="{}">Register</a> | <a href="{}">Login in</a>
        '''.format(reverse('registration_register'), reverse('auth_login')))
        #render_to_response('honey/templates/index.html',)



    #HttpResponse('''<a href="{}">Register</a> | <a href="{}">Login in</a>
        #'''.format(reverse('registration_register'), reverse('auth_login')))
#a href="{}">Register| <a href="{}">Login in</a>跳转的链接