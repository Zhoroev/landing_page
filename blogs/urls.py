from django.urls import path
from blogs.views import blogs_list_view

urlpatterns = [
    path('', blogs_list_view, name='blogs_list_url'),
]