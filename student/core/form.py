from django import forms
from .models import student

class addstudentform(forms.ModelForm):
    class Meta:
        model=student
        fields=("name","college","city")
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'college':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'})
        }
