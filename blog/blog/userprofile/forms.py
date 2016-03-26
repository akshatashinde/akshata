from django import forms
from userprofile.models import userprof, profilepic, User

class userprofForm(forms.ModelForm):
	class Meta:
		model = userprof
		fields = ('fname','lname','mobileno','gender','emailid')

class profilepicForm(forms.ModelForm):
	class Meta:
		model = profilepic
		fields = ('picture',)

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields = ('username','email','first_name','last_name')		