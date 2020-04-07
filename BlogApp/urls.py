from django.urls import path
from .views import (
    create_blog_view,
    detail_blog_view,
    update_blog_view,
)

app_name = 'BlogApp'

urlpatterns = [
    path('create/', create_blog_view, name='create'),
    path('<slug>/', detail_blog_view, name='detail'),
    path('<slug>/edit', update_blog_view, name='edit'),
]
