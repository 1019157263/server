from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json

# Create your views here.
def index(request):
       if request.method=='GET':           
           dict={ 'msg':'GET方法','status':'访问成功',}
           return HttpResponse(str(dict))
       if request.method=='POST':
           username=request.POST['xxx']
           email=request.POST['ooo']
           dict={
               'msg':{
                   'username':username,
                   'email':email,
               }
           }
           return HttpResponse(str(dict))