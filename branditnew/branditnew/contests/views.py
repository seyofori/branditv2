from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, reverse

from branditnew.contests.models import forms

# Create your views here.

def index(request):
    return render(request, "contests/index.html")



def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db() #load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            raw_password = form.cleaned_data.get('password1')
            user.save()
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, "contests/dashboard.html")

    else:
        form = forms.SignUpForm()
    return render(request, "contests/signup.html", {'form': form})



def dashboard(request):
    return render(request, "contests/dashboard.html")



def create_contest(request):
    if request.method == request.POST:
        form = forms.CreateContestForm(request.POST)
        if form.is_valid():
            contest = form.save()
            return redirect('')
    else:
        form = forms.CreateContestForm()
        return redirect("http://0:8080/contests/dashboard.html")
    return render(request, "contests/create-contest.html")