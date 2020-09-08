from django.shortcuts import render

# Create your views here.
from ieee.forms import infoForm
from ieee import models
from django.http import HttpResponse,HttpResponseRedirect

def HomePage(request):
    return render(request,'ieee/HomePage.html')

def DeletePage(request):
    infoid=request.GET['infoid']
    info=models.info.objects.filter(id=infoid)
    info.delete()
    return HttpResponseRedirect('/ieee/candidate-page/')

def EditPage(request):
    infoid=request.GET['infoid']
    info=models.info.objects.get(id=infoid)
    fields={'name':info.name,'gender':info.gender,'dob':info.dob,'branch':info.branch,'phone':info.phone,'email':info.email}
    form=infoForm(initial=fields)
    return render(request,'ieee/EditPage.html',{'form':form,'info':info})

def Edit(request):
    if request.method=="POST":
        form=infoForm(request.POST)
        info=models.info()
        info.id=request.POST['infoid']
        info.name=form.data['name']
        info.gender=form.data['gender']
        info.dob=form.data['dob']
        info.branch=form.data['branch']
        info.phone=form.data['phone']
        info.email=form.data['email']
    info.save()
    return HttpResponseRedirect("/ieee/candidate-page/")


def RegisterPage(request):
    form=infoForm()
    return render(request,'ieee/RegisterPage.html',{'form':form})

def Add(request):
    if request.method=="POST":
        info=models.info()
        form=infoForm(request.POST)
        info.name=form.data['name']
        info.gender=form.data['gender']
        info.dob=form.data['dob']
        info.branch=form.data['branch']
        info.phone=form.data['phone']
        info.email=form.data['email']
    info.save()
    return HttpResponse("You Are Successfully Registered <br> <a href='/ieee/home-page/'>Click Here</a>")

def InstructionPage(request):
    return render(request,'ieee/InstructionPage.html')

def CandidatePage(request):
    info=models.info.objects.all()
    return render(request,'ieee/CandidatePage.html',{'info':info})
