from django.shortcuts import render,HttpResponseRedirect
from form.forms import StudentRegistration
from form.models import User
# Create your views here.

def add_show(request):
  
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save()
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud1=User.objects.all()      
    return render(request,'form/addandshow.html',{'form':fm,'stu':stud1})

def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid:
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    return render(request,'form/updatestudent.html',{'form':fm})

def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')  
