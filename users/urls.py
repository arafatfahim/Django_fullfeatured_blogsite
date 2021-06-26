from django.urls import path, include
from .import views

urlpatterns = [
    path('login', views.user_login, name="Login"),    
    path('logout', views.user_logout, name="Logout"),    
   # path('forgotpassword', views.user_resetpass, name="Resetpass"), 
   # path('resetpassconf', views.user_resetpassconf, name="Resetpassconf"), 
    path('signup', views.handlesignup, name="Signup"),
    path('contact', views.contact, name="Contact"),
    path('profile', views.profile, name="Profile"),
    
]