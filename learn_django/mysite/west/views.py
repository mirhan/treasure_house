# -*- coding: utf-8 -*-
from django.http import HttpResponse
from west.models import Character
from django.shortcuts import render


def first_page(request):
    return HttpResponse("<p>西餐</p>")

def staff(request):
    staff_list = Character.objects.all()
    staff_str  = map(str, staff_list)
    context   = {'label': ' '.join(staff_str)}
    return render(request, 'templay.html', context)
# Create your views here.

def templay(request):
    context          = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)
