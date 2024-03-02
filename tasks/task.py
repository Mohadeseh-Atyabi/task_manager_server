from django import forms


class Task(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    duration = forms.TimeField()
    start_date = forms.DateField()
