from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, UserPostListView
from .import views

urlpatterns = [
    path('', views.Home, name="Home" ),
    path('about', views.About, name="About" ),
    path('blogpost', PostListView.as_view(), name="Blogpost" ),
    path('user/<str:username>', UserPostListView.as_view(), name="Userpost" ),
    path('blogpost/<int:pk>', PostDetailView.as_view(), name="Postdetails"),
    path('blogpost/<int:pk>/update', PostUpdateView.as_view(), name="Postupdate"),
    path('blogpost/<int:pk>/delete', PostDeleteView.as_view(), name="Postdelete"),
    path('blogpost/new/', PostCreateView.as_view(), name="Postcreate"),
    path('blogpost/<int:pk>', PostDetailView.as_view(), name="Postdetails"),
    
]