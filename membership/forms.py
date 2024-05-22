from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control font-extrabold mb-4'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control font-extrabold  mb-4'}))
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control mb-0 pb-0'
		self.fields['username'].help_text = '<div class="form-text text-muted mt-0 pt-0 mb-6">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</div>'
		self.fields['password1'].widget.attrs['class'] = 'form-control mb-0 pb-0 mt-2 font-extrabold'
		self.fields['password1'].help_text = (
            '<ul class="form-text text-muted mt-0 pt-0 mb-10 pb-5">'
            '<li>Your password can’t be too similar to your other personal information.</li>'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password can’t be a commonly used password.</li>'
            '<li>Your password can’t be entirely numeric.</li>'
            '</ul>'
        )
		self.fields['password2'].widget.attrs['class'] = 'form-control mb-0 pb-0 font-extrabold'
		self.fields['password2'].help_text = '<div class="form-text text-muted mb-5 pb-5">Enter the same password as before, for verification.</div>'