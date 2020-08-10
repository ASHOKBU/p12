from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_demo(request):
    name= request.GET.get('name')
    return render(request,'get_demo.html',{'name':name})
def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse('<h1>Thanks for submission Mr./Ms. {}</h1>'.format(name))
    return render(request,"post_demo.html")