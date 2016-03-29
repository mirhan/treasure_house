# -*- coding: utf-8 -*-
from django.http import HttpResponse
from west.models import Character
from django.shortcuts import render
from django.core.context_processors import csrf
from django import forms


def first_page(request):
    return HttpResponse("<p>西餐</p>")

def staff(request):
    staff_list = Character.objects.all()
    return render(request, 'templay.html', {'staffs': staff_list})
# Create your views here.

def templay(request):
    context          = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)

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
