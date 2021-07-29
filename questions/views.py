from django.shortcuts import render, redirect, reverse
from questions.forms import QuestionForm

from django.views import View

class LoginView(View):

    def get(self, request):
        bound_form = QuestionForm()
        return render(request, 'blogs/index.html', context={'login_form': bound_form})

    def post(self, request):
        bound_form = QuestionForm(request.POST)
        return render(request, 'blogs/index.html', context={'login_form': bound_form})
