from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^event/$', views.EventListView.as_view(), name='event'),
    url(r'^event/create$', views.event_create, name='event_create'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.event_update, name='event_update'),
    url(r'^event/(?P<pk>\d+)/print/$', views.EventPrintView.as_view(), name='event_print'),
    url(r'^print/$', views.PrintView.as_view(), name='print'),
]