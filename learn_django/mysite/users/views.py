from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def user_login(request):
    '''
    login
    '''
    print '0'
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username = request.POST['username'], password=request.POST['password'])
            if user is not None and user.is_active:
                login(request, user)
                return redirect('/')

    form = AuthenticationForm()
    ctx = {}
    ctx.update(csrf(request))
    ctx['form'] = form
    return render(request, 'login.html',ctx)

def user_logout(request):
    '''
    logout
    URL: /users/logout
    '''
    logout(request)
    return redirect('/')