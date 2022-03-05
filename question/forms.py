from django import forms


class Quest(forms.Form):
    quest = forms.CharField(max_length=255, required=False, )
    form = forms.CharField(initial='somth', widget=forms.HiddenInput)

class Add(forms.Form):
    add = forms.IntegerField(initial=1, widget=forms.HiddenInput)