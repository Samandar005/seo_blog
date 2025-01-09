from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('author/list/', views.author_list, name='author_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('author/update/<int:pk>/', views.author_update, name='author_update'),
    path('author/delete/<int:pk>/', views.author_delete, name='author_delete'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.blog_detail, name='detail'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('comment/create/<int:pk>/', views.comment_create, name='comment_create'),
    path('success/commented/<int:pk>/', views.success_commented, name='success_commented'),
]
