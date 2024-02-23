from django.shortcuts import render,HttpResponse
from demo.models import sam
from demo.forms import samform
# Create your views here.

def ins(request):
    var=samform()
    if request.method=='POST':
        a=samform(request.POST)
        if a.is_valid():
            a.save()
            return HttpResponse('data stored')
    return render(request,'sam.html',{'var':var})

def up(request,a):
    aaa=sam.objects.get(id=a)
    var=samform(instance=aaa)
    if request.method=='POST':
        a=samform(request.POST,instance=aaa)
        if a.is_valid():
            a.save()
            return HttpResponse('data updated')
    return render(request,'sam.html',{'var':var})

def readall(request):
    var=sam.objects.all()
    return render(request,'devil.html',{'var':var})

def dl(request,a):
    sam.objects.get(id=a).delete()
    return HttpResponse('data deleted')



