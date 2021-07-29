from django.urls import path
from news.views import posts_list_view, post_detail_view

urlpatterns = [
    path('', posts_list_view, name='posts_list_url'),
    path('<int:id>/', post_detail_view, name='post_detail_url'),
]