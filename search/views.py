import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Searchdata

# Create your views here.
def index(request):
    return render(request,'search/index.html')

def ajaxview(request):
    if request.method=='POST':
        lis = []
        for x in Searchdata.objects.all():
            if((x.string_text).find(request.POST.get('query',''))!=-1):
                lis.append(x.string_text)
        dic = {"result":lis}
        return HttpResponse(
            json.dumps(dic),
            content_type="application/json"
        )
                
