from django.shortcuts import render,redirect #type: ignore
from django.http import HttpResponse #type: ignore
import random
# Create your views here.
def index(request):
    return render(request,'short/index.html')

def randomval():
    salphs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    nums = [1,2,3,4,5,6,7,8,9,0]
    p = salphs+list(map(str,nums))
    random.shuffle(p)
    random_pattern = random.choice(salphs)+random.choice(p)+random.choice(p)+random.choice(p)+random.choice(p)+random.choice(p)
    print(random_pattern)
    return random_pattern

def generate(request):
    if request.method == 'POST':
        main_url = request.POST.get('url')
        return render(request,'short/index.html',{'main_url':main_url})
    return render(request,'short/index.html')




