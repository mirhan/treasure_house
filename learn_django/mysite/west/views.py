# -*- coding: utf-8 -*-
from django.http import HttpResponse

from west.models import Character


def first_page(request):
    return HttpResponse("<p>西餐</p>")

def staff(request):
    staff_list = Character.objects.all()
    staff_str  = map(str, staff_list)
    return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")
# Create your views here.
