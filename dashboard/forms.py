#!/usr/bin/env python
from django import forms

class CountryStatusForm(forms.Form):
    country = forms.CharField()    
    year = forms.IntegerField()
    population = forms.IntegerField()
    
    
