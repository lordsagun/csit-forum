from django.http import HttpResponse
from django.shortcuts import render
from myaccount.models import Myuser
from theory.models import Semester,Syllabus,OldQuestion,Year,Note,Solution

def home(request):
    context={
    'sem':Semester.objects.all(),
    }
    return render(request,'index.html',context)


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
    context={
    'sem':Semester.objects.all(),
    's': Semester.objects.get(pk=id),
    'sy': Syllabus.objects.filter(sem_id=id)
    }
    return render(request,'sy_detail.html',context)



def old_questions(request):
    context={
    'sem':Semester.objects.all()
    }
    return render(request,'oldquestions.html',context)

def oldquestions_detail(request,id):
    context={
    'sem':Semester.objects.all(),
    's': Semester.objects.get(pk=id),
    'year':Year.objects.all()
    }
    return render(request,'sy_detail.html',context)


def oldquestions_sub(request,id):
    context={
    'sem':Semester.objects.all(),
    'old': OldQuestion.objects.filter(year_id=id),
    'y':Year.objects.get(pk=id)
    }
    return render(request,'sy_detail.html',context)



def notes(request):
    context={
    'sem':Semester.objects.all()
    }
    return render(request,'notes.html',context)


def notes_details(request,id):
    context={
    'sem':Semester.objects.all(),
    's': Semester.objects.get(pk=id),
    'note':Note.objects.filter(sem_id=id),
    }
    return render(request,'sy_detail.html',context)


def solutions(request):
    context={
    'sem':Semester.objects.all()
    }
    return render(request,'solution.html',context)

def solutions_detail(request,id):
    context={
    'sem':Semester.objects.all(),
    's': Semester.objects.get(pk=id),
    'yr':Year.objects.all()
    }
    return render(request,'sy_detail.html',context)

def solutions_sub(request,id):
    context={
    'sem':Semester.objects.all(),
    'sol': Solution.objects.filter(year_id=id),
    'y':Year.objects.get(pk=id),
    's': Semester.objects.get(pk=id)
    }
    return render(request,'sy_detail.html',context)
