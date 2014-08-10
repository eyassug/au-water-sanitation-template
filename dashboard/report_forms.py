from django import forms
from dashboard import models


class TechnologyGapByPriorityArea(forms.Form):
    technology = forms.ModelChoiceField(queryset=models.Technology.objects.all(), widget=forms.Select())
    start_year = forms.IntegerField()
    end_year = forms.IntegerField()