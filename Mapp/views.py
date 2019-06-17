from django.shortcuts import render, HttpResponse
import time

from .forms import Sform, Mform, Mteacher

def Mfunction(request):
    obj = Sform()
    d = {"name" : "Ram",'time':time.ctime(),'form':obj}

    return render(request,'index.html',d)


def Mstudent(request):
    if request.method == "POST":
        form = Mform(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank You")
    else:
        form = Mform()
    return render(request,'student.html',{'form':form})


def Fteacher(request):
    if request.method == "POST":
        form = Mteacher(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank You")
    else:
        form = Mteacher()
    return render(request,'teacher.html',{'form':form})


# Create your views here.
