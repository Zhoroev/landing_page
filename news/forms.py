from django import forms
from news.models import News


class PostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body', ]