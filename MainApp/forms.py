from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Ex: Jone Hasi'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Ex: example@gmail.com'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Ex: +8801977042737'}),
            'subject': forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}),
            'message': forms.Textarea(attrs={'class':'form-control','placeholder':'Write A Message'}),
        }
