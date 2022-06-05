from email import message
from functools import reduce
from multiprocessing import AuthenticationError
from select import select
from telnetlib import LOGOUT
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import DocumentForm, ProfileForm
from .models import Document
# Create your views here.


def loginAccount(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            fname = user.first_name
            login(request, user, fname)
            return redirect('profile')

        else:
            messages.error(request,'Wrong Credentials !')
            return redirect('login') 


    return render(request , "index.html")
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists')
            return redirect('login')
        
        else:

            if pass1 == pass2:
                user = User.objects.create_user(username,email,pass1)
                user.save()
                messages.success(request, "Your Account has been created.")
                return redirect('login')
            else:
                messages.error(request, "Passwords do not match.")
                return redirect('login')

    return render(request, "index.html")

def signout(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login')
def view_resume(request):
    documents = Document.objects.all()
    user = User.objects.all()
    return render(request, 'view_resume.html', {
        'documents':documents,
        'users': user,
    })

@login_required(login_url='login')
def help(request):
    return render(request, 'help.html')


@login_required(login_url='login')
def settings(request):
      
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        profile_form = ProfileForm(instance=request.user.profile)  
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user ;
            obj.save()
            messages.success(request, 'Resume Successfully Uploaded')
            # form = DocumentForm()
            # return redirect('settings')
        if profile_form.is_valid():
            profile_form.save()
    else:
        form = DocumentForm()
        profile_form = ProfileForm()
    return render(request, 'settings.html', {
        'form':form,
        'profile_form':profile_form,
    })