from django.shortcuts import render, get_object_or_404, redirect, reverse
from blogs.models import Blog
from django.views import View
from questions.forms import QuestionForm


def blogs_list_view(request):
    blogs = Blog.objects.all()
    bound_form = QuestionForm(request.POST)
    return render(request, 'blogs/index.html', context={'blogs': blogs,
                                                        'question_form': bound_form})



