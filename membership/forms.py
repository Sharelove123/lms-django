from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control mb-4'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control mb-4'}))
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control mb-4'
		self.fields['password1'].widget.attrs['class'] = 'form-control mb-4'
		self.fields['password2'].widget.attrs['class'] = 'form-control mb-4'