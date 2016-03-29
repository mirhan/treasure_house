# -*- coding: utf-8 -*-
from django.http import HttpResponse
from west.models import Character
from django.shortcuts import render


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

def investigate(request):
    rlt = request.GET['staff']
    return HttpResponse(rlt)
