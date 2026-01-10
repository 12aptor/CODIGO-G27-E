from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostView.as_view()),
    path('posts/<int:pk>/', views.ManagePostView.as_view()),

    path('comments/', views.CommentView.as_view()),
    path('comments/<int:pk>/', views.ManageCommentView.as_view()),
]