from django.shortcuts import render, render_to_response

# Create your views here.
from skim.models import Imfromation


def get_buy(request):
    id = request.GET.get('buy_info', 'error')
    class_all = Imfromation.objects.filter(id=id)
    dic = {'class_all': class_all}
    return render_to_response('buy.html', dic)