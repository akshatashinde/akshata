from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from userprofile.models import userprof, profilepic
from userprofile.forms import userprofForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def userprof_view(request):
	return HttpResponse("testing blog")


def adduserprof_view(request):	
	if request.method == 'POST':
		form = userprofForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.INFO,'user added details!')
			# return HttpResponse("user submit details successfully")
	else:
		form= userprofForm()

	return render(request,'userprofile/userdetails.html',{'form':form})	

def updateprofile_view(request):
	id = request.GET.get('id', None)
	if id is not None:
		userid = get_object_or_404(userprof,id=id)
	else:
		userid = None

	if request.method == 'POST':
		form = userprofForm(request.POST, instance=userid)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.INFO,'user added details!')
			# return HttpResponse("user submit details successfully")
	else:
		form= userprofForm(instance=userid)

	return render(request,'userprofile/updateprofile.html',{'form':form,'userid':userid})	

def register(request):
	if request.method == 'POST':
		profile_form = profilepicForm(data=request.POST)
		if profile_form.is_valid():
			profile = profile_form.save(commit=False)
			
			if 'picture' in request.FILES:
				profile.picture=request.FILES['picture']

				profile.save()	
			else:
				print profile_form.errors

	else:
		profile_form = profilepicForm()

	return render(request,'rango/register.html', {'profile_form':profile_form})	