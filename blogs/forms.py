from django import forms
from blogs.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['first_name', 'last_name', 'position', 'birthdate', 'phone', ]
