# -*- coding: utf-8 -*-
from django.http import HttpResponse
from west.models import Character
from django.shortcuts import render
from django.template.context_processors import csrf
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required(login_url='/users/login/')
def user_only(request):
    return HttpResponse("<p>This message is for logged in user only.</p>")

def name_check(user):
    print 'username !'
    print user.get_username()
    return user.get_username() == 'vamei'

@user_passes_test(name_check, login_url='/users/login/')
def specific_user(request):
    return HttpResponse("<p>for Vamei only</p>")

# Create your views here.
def first_page(request):
    return HttpResponse("<p>西餐</p>")

def staff(request):
    staff_list = Character.objects.all()
    return user_only(request)
    # return render(request, 'templay.html', {'staffs': staff_list})

def templay(request):
    return specific_user(request)
    # context          = {}
    # context['label'] = 'Hello World!'
    # return render(request, 'templay.html', context)

def form(request):
    return render(request, 'form.html')

class CharacterForm(forms.Form):
    name = forms.CharField(max_length = 200)
    
def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted  = form.cleaned_data['name']
            new_record = Character(name = submitted)
            new_record.save()

    form = CharacterForm()
    ctx ={}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form']  = form
    return render(request, "investigate.html", ctx)
