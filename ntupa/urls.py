"""ntupa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin, auth

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/update/$', views.ProfileUpdateView.as_view(), name='profile_update'),
    url(r'^profile/password/$', auth.views.password_change, {'template_name': 'ntupa/profile_password.html', 'post_change_redirect': 'profile_password_done'}, name='profile_password'),
    url(r'^profile/password/done/$', views.profile_password_done, name='profile_password_done'),
    url(r'^equip/', include('equip.urls')),
    url(r'^admin/', admin.site.urls),
]
