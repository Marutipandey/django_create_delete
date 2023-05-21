from django import forms

from enroll.models import simpleform


class loginform(forms.ModelForm):
    class Meta:
        model= simpleform
        fields=['name','email','phone_number']