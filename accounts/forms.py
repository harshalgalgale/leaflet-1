from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import TextInput, PasswordInput

class RegistrationForm(forms.Form):
	username  = forms.CharField()
	email     = forms.EmailField()
	password  = forms.CharField(widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('That user name already exists.')

	def clean_password(self):
		password  = self.cleaned_data.get('password', None)
		password1 = self.cleaned_data.get('password', None)
		if password and password1 and password != password1:
			raise forms.ValidationError('The passwords due not match.')
		return password

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
	password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder':'password'}))