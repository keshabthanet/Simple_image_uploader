from django import forms 
from django.forms import ModelForm 
from .models import GeeksModel

# class GeeksForm(forms.Form): 
# 	name = forms.CharField() 
# 	geeks_field = forms.ImageField() 
class GeeksForm(ModelForm):
    
    class Meta:
        model = GeeksModel
        fields = ("title","img")

