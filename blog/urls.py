from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', post_list_view.as_view(), name='blog-home'),
    path('user/<str:username>', user_post_list_view.as_view(), name='user-posts'),
    path('profile/<str:username>', views.get_user_profile, name='user-profile'),
    # path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/', views.detail, name='post-detail'),
    path('update/<slug:slug>', views.updatePost, name="update"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('delete/<slug:slug>', views.deletePost, name="delete"),
    path('about/', views.about, name='blog-about'),
    path("newpost/", views.NewPost, name='newpost'),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
    path('comment/<slug:slug>', views.addComment, name="comment"),

]
