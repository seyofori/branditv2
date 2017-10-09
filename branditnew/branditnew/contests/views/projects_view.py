from branditnew.contests.models import forms
from branditnew.contests.models.projects import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, reverse, get_object_or_404
from branditnew.contests.views.payment_views import process_invoice, verify_payment
from django.http import HttpResponse, HttpResponseRedirect
import requests, json, pprint



@login_required(login_url="login")
def create_project(request):
    form = forms.Create_Project_Form()
    category_prices = Category.objects.values()

    if request.method == "POST":
        form = forms.Create_Project_Form(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            category_cost = Category.objects.get(name=form.cleaned_data.get('category')) 
            cost = category_cost.prize_lower_limit
            project.cost = cost
            project.is_draft = False
            project.save()

            #hubtel payment goes here.
            data = process_invoice(request, project)
            return redirect(data['response_text'], data['token'])

    context = {
        'form':form,
        'category_prices': json.dumps(list(category_prices))
    }
    return render(request, "contests/create_project.html", context)

@csrf_exempt
def save_as_draft(request):
    if request.method == 'POST':
        client = request.user
        if request.POST['title'] is not '':
            title = request.POST["title"]
        else:
            title = 'draft'
        
        #fetching category instance using id from POST array. if no category has been set, use the 'draft' category, else django won't let you save.
        category_id = request.POST['category']
        if category_id is not '':
            category = Category.objects.filter(pk=category_id)
        else:
            category = Category.objects.get(name="draft")

        desc = request.POST['description']
        
        #files = request.POST.FILES['files'] yet to figure out how to handle the files upload part.

        end_date = request.POST['end_date']
        
        draft = Project.objects.create(client=client, title=title, category=category, description=desc, end_date=end_date)
        
        return HttpResponse('success')


def edit_project(request):
    if request.method == 'POST':
        return
    
    return 

        