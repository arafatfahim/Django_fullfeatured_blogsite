from django.urls import path
from .views import PostApiView, UserApiView, PostApiDetailView, PostApiNewView


urlpatterns = [
    path('post/', PostApiView.as_view()),
    path('user/', UserApiView.as_view()),
    path('post/<int:pk>', PostApiDetailView.as_view()),
    path('post/new', PostApiNewView.as_view()),
    
]
