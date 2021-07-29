from django.shortcuts import render, get_object_or_404
from news.models import News


def posts_list_view(request):
    posts = News.objects.all()
    return render(request, 'news/index.html', context={'posts': posts})


def post_detail_view(request, id):
    post = get_object_or_404(News, id=id)
    return render(request, 'news/news_detail.html', context={'post': post})
