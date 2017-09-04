from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.template import loader

from branditnew.contests.models import forms
from branditnew.contests.models.contest import Contest

# Create your views here.

def index(request):
    contests_list = Contest.objects.all()
    print(contests_list)
    template = loader.get_template('contests/index.html')
    context = {
        'contests_list': contests_list,
    }
    return HttpResponse(template.render(context, request))



def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db() #load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.user_name=user.username
            print(user.profile.user_name)
            raw_password = form.cleaned_data.get('password1')
            # user.save()
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, "contests/dashboard.html")

    else:
        form = forms.SignUpForm()
    return render(request, "contests/signup.html", {'form': form})



def dashboard(request):
    return render(request, "contests/dashboard.html")



def create_contest(request):
    if request.method == 'POST':
        form = forms.CreateContestForm(request.POST)
        
        if form.is_valid():
            print('form is valid')
            contest = form.save()
            print(contest)
            return HttpResponse('Form is valid and saved')
    else:
        form = forms.CreateContestForm()
        return render(request, "contests/create-contest.html", {'form': form})


def submit_entry(request, contest_id):
    if request.method == "POST":
        form = forms.ContestEntryForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "contests/dashboard.html")

    else:
        form = forms.ContestEntryForm(initial={'contest': contest_id, 'brandlancer': request.user.id})
        return render(request, "contests/submit_contest_entry.html", {'form': form})



def contest_details(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    return render(request, 'contests/contest_details.html', {'contest': contest})