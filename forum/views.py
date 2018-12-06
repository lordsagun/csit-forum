from django.http import HttpResponse
from django.shortcuts import render
from myaccount.models import Myuser
from theory.models import Semester,Syllabus

def home(request):
    context={

    }
    return render(request,'index.html')


def dashboard(request):
    context={
    # 'user': Myuser.objects.get(Myuser_id=request.user.id)
    }
    return render(request,'dashboard.html',context)

def question(request):
    return render(request,'question.html')


def syllabus(request):
    context={
    'sem':Semester.objects.all()
    }
    return render(request,'syllabus.html',context)


def syllabus_detail(request,id):
    sem:Semester.objects.get(semester_id=id)
    context={
    'sy': Syllabus.objects.filter(sem_id=sem.id)
    }
    return render(request,'sy_detail')
