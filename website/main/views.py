from django.views.generic import ListView
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from .models import Courses
from .tables import CourseTable
import pandas as pd
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.
#def FCQloginpage(request):
#    return render(request, 'main/FCQloginpage.html')

def course(request):
    table = CourseTable(Courses.objects.filter(crse="3170"))

    subject = Courses.objects.values("subject").distinct()
    if request.method == 'POST':
        challenge = request.POST['challenge']
        workload = request.POST['workload']
    return render(request, 'main/course.html', {'course':table})


#to pull create account page
#def createAccount(request):
#    return render(request, 'main/createAccount.html')
	
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form':form})


def root(request):
    if request.user.is_authenticated:
        return render(request, 'fcq_Natnael_noDjango.html')
    else:
        return redirect('login/')

