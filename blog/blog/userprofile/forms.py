from django import forms
from userprofile.models import userprof, profilepic

class userprofForm(forms.ModelForm):
	class Meta:
		model = userprof
		fields = ('fname','lname','mobileno','gender','emailid')

class profilepicForm(forms.ModelForm):
	class Meta:
		model = profilepic
		fields = ('picture')