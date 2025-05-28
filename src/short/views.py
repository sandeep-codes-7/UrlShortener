from django.shortcuts import render,redirect #type: ignore
from django.http import HttpResponse #type: ignore
import random
from .models import UrlData #type: ignore


def index(request):
    return render(request,'short/index.html')

def randomval():
    salphs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    nums = [1,2,3,4,5,6,7,8,9,0]
    p = salphs+list(map(str,nums))
    random.shuffle(p)
    random_pattern = random.choice(salphs)+random.choice(p)+random.choice(p)+random.choice(p)+random.choice(p)
    #print(random_pattern)
    return random_pattern

def result(request):
    if request.method == 'POST':
        main_url = request.POST.get('main_url')
        if not UrlData.objects.filter(original_url=main_url).exists():
            UrlData.objects.create(original_url=main_url,short_url=randomval())
            res = UrlData.objects.get(original_url=main_url).short_url
        else:
            res = UrlData.objects.get(original_url=main_url).short_url
            return render(request,'short/error.html',{'result':res})
        
    return render(request,'short/result.html',{'result':res})



def redirect_url(request,redir):
    #print(UrlData.objects.get(short_url=redir).original_url)
    #res=UrlData.objects.get(short_url=redir).original_url
    try:
        if redir!=None:
            return redirect(UrlData.objects.get(short_url=redir).original_url)
        else:
            pass
    except Exception as e:
        pass