from django.shortcuts import render
from rest_framework import generics, serializers, permissions
from blog.models import Post
from users.models import Profile 
from .serializers import PostSerializer
from .serializers import UserSerializer
# Create your views here.
class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserApiView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset= Profile.objects.all()
    serializer_class = UserSerializer


class PostApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostApiNewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all().order_by('-pid')[:1]
    serializer_class = PostSerializer