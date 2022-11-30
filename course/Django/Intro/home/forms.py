from django import forms
from .models import Todo
from django.forms import ModelForm


class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField(label="date and time created".capitalize(), required=False)


class TodoUpdateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body', 'created']
    # or fields = "__all__"
