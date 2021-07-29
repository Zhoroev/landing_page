from django import forms
from questions.models import Question


class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput())
    contact = forms.CharField(widget=forms.TextInput())
