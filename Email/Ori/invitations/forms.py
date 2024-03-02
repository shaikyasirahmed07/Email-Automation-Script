# invitations/forms.py
from django import forms

class EmailForm(forms.Form):
    email_list = forms.CharField(widget=forms.Textarea)
