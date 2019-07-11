from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class':'form-control'
        }
        self.fields['email'].widget.attrs = {
            'class':'form-control'
        }
        self.fields['message'].widget.attrs = {
            'class':'form-control'
        }
    def clean_email(self):
        print("fsfsd")
        # import pdb; pdb.set_trace()
        original_email = self.cleaned_data.get('email')

        email = original_email.split('@')[1]
        if email != "dhina":
            return forms.ValidationError('School not found, check your email') 
        return original_email
