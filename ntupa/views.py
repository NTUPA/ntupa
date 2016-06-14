from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from django.views.generic.edit import UpdateView

from extra_views import UpdateWithInlinesView
from . import forms

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('profile'))

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)
    
    redirect_to = request.POST.get('next', request.GET.get('next', reverse('profile')))

    if user is not None and user.is_active:
        auth.login(request, user)
        if not is_safe_url(url=redirect_to, host=request.get_host()):
            redirect_to = reverse('profile')

        return HttpResponseRedirect(redirect_to)
    else:
        return render(request, 'ntupa/login.html', context={'next': redirect_to})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required()
def profile(request):
    context = {
        'request': request
    }
    return render(request, 'ntupa/profile.html', context=context)

@login_required()
def profile_password_done(request):
    context = {
        'request': request
    }
    return render(request, 'ntupa/profile_password_done.html', context=context)

class ProfileUpdateView(LoginRequiredMixin, UpdateWithInlinesView):
    model = User
    inlines = [forms.UserProfileInline]
    fields = ['email']
    template_name = 'ntupa/profile_update.html'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_success_url(self):
        return reverse('profile_update')