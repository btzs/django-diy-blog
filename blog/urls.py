from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.BlogListView.as_view(), name='posts'),
    path('author/<int:pk>', views.BlogListbyAuthorView.as_view(), name='posts-by-author'),
    # path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('post/<slug:slug>', views.BlogDetailView.as_view(), name='post-detail'),
    path('authors/', views.BloggerListView.as_view(), name='authors'),
    path('post/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='post_comment'),
]