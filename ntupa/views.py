from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('profile'))

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('profile'))
    else:
        return render(request, 'ntupa/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

def profile(request):
    return render(request, 'ntupa/profile.html', context=locals())