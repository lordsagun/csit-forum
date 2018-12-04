from django.shortcuts import render,redirect
from django.contrib.auth.forms  import UserCreationForm
from myaccount.forms import SignupForm


def home(request):
    context={

    }
    return render(request,'index.html')


def signup(request):
    if request.method=='GET':
        context={
        'form': SignupForm(),
        }
        return render(request,'signup.html',context)
    else:
        form=SignupForm(request.POST)
        if form.is_valid():
            try:
                password= request.POST.get('password')
                re_password = request.POST.get('re_password')
                if password==re_password:
                    form.save()
                    return redirect('login')
                else:
                    return render(request,'signup.html',{'form':form,'errmsg':'Password field didnt match.'})

            except:
                return render(request,'signup.html',{'form':form})
        else:
            return render(request,'signup.html',{'form':form,'errmsg':'Something went worng'})
