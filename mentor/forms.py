# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['yourname', 'email', 'subject', 'phone', 'message']
        widgets = {
            'yourname': forms.TextInput(attrs={
                'name':'name',
                'type':'text',
                'placeholder': 'Your name',
                'data-error': 'Name is required.',
                'required': 'required',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'name':'email',
                'type':'email',
                'placeholder': 'Email',
                'data-error': 'Valid email is required.',
                'required': 'required',
                'class': 'form-control'
            }),
            'subject': forms.TextInput(attrs={
                'name':'subject',
                'type':'text',
                'placeholder': 'Subject',
                'data-error': 'Subject is required.',
                'required': 'required',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'name':'phone',
                'type':'text',
                'placeholder': 'Phone',
                'data-error': 'Phone is required.',
                'required': 'required',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'name':'messege',
                'placeholder': 'Message',
                'data-error': 'Please, leave us a message.',
                'required': 'required',
                'class': 'form-control'
            }),
        }
