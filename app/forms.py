# app/forms.py
from django import forms

class MyForm(forms.Form):
    field1 = forms.CharField(max_length=100)
    field2 = forms.CharField(max_length=100)
    field3 = forms.CharField(max_length=100)
    field4 = forms.CharField(max_length=100)
    field5 = forms.CharField(max_length=100)
    field6 = forms.CharField(max_length=100)

def rData(obj1):
    return [obj1.field1,obj1.field2,obj1.field3,obj1.field4,obj1.field5,obj1.field6]
