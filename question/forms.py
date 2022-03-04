from django import forms

class Quest(forms.Form):
    quest = forms.CharField(max_length=255)
    form = forms.CharField(initial='somth', widget=forms.HiddenInput)