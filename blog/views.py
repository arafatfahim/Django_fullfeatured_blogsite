import firebase as firebase
from django.shortcuts import render, HttpResponse, get_object_or_404
import pyrebase
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.

config={
    'apiKey': "AIzaSyB2dp75-oHjZFcqNlcHg9VHtFdC1l5pk2A",
    'authDomain': "blogtalk-37e4a.firebaseapp.com",
    'databaseURL': "https://blogtalk-37e4a-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "blogtalk-37e4a",
    'storageBucket': "blogtalk-37e4a.appspot.com",
    'messagingSenderId': "1004743626254",
    'appId': "1:1004743626254:web:a79603148dcf54b748f65f",
    'measurementId': "G-F45SD24NTT"
}

firbase= pyrebase.initialize_app(config)
# storage = firebase.storage()
authe = firbase.auth()
database = firbase.database()
# firebase = pyrebase.initialize_app(config)



def Home(request):
    return render(request, 'blog/home.html')


def Blogpost(request):
    allPosts = Post.objects.all()
    print(allPosts)
    context = {'allPosts': allPosts}

    return render(request, 'blog/blogpost.html', context)


def uPost(request, slug):
    return render(request, 'blog/post.html')


def About(request):
    return render(request, 'blog/about.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/blogpost.html'
    context_object_name = 'allPosts'
    ordering = ['-date']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/userpost.html'
    context_object_name = 'allPosts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'thumbnail_url', 'category']
    template_name = 'blog/postcr.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'thumbnail_url', 'category']
    template_name = 'blog/postup.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/postdl.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





