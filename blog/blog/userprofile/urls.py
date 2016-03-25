from django.conf.urls import include, url
from django.contrib import admin
from userprofile import views

urlpatterns = [
	url(r'^$',views.userprof_view, name='home'),
	url(r'^add_userprofile/$', views.adduserprof_view, name='adddetails'),
	url(r'^updateprofiles/$', views.updateprofile_view, name='updateprofile'),
	url(r'^register/$',views.register, name='register'),
	]
	