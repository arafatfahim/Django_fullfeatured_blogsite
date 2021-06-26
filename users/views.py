from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Contact, Profile
from django.conf import settings
from django.core.mail import send_mail
import pyrebase

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
auth = firbase.auth()
database = firbase.database()

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if not username.isalnum():
            messages.error(request,"Username must be Alphanumeric")
            return redirect ("/signup")
        if pass1 != pass2:
            messages.error(request,"Your Password is not Same")
            return redirect ("/signup")
        myuser =  User.objects.create_user(username=username, email=email, password=pass1, first_name=first_name, last_name=last_name)
        myuser.save()
        messages.success(request,f'Account Created for {username}!')
        subject = 'Welcome to BLOGTALK'
        message = f'Hi {myuser.username}, thank you for registering in BLOGTALK.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [myuser.email, ]
        send_mail( subject, message, email_from, recipient_list )

       
        return redirect('/login')
    else:
        #messages.error(request,f'Please Enter Valid Info' )
        return render(request,'users/signup.html')
        
    #return render(request, 'users/signup.html')
       

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You Are Successfully Logged In ")
            return redirect ("/")
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")

    #return HttpResponse('404 Not Found')
    return render(request, 'users/login.html')  

@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'You are successfully logout')
    return redirect ("/")


def contact(request):
    #showing Warning/success msg
    #messages.success(request, 'Welcome To Contact')
    #set the parameter
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        country = request.POST['country']
        msg = request.POST['msg']
        print('name','email', 'msg')
        # creating Arguement for saving the data in the database
        contact = Contact(name=name, email=email, phone=phone, country=country, msg=msg)
        #save data
        contact.save()
        messages.success(request, 'Thanks For Contacting, We will get back to you soon! 💖')
    return render(request, 'users/contact.html')

@login_required
def profile(request):
    context = {}
    data = Profile.objects.get(user__id=request.user.id)
    context['data'] = data
    if request.method=='POST':
        print(request.POST)
        #pic= request.POST['image']
        fn= request.POST['firstname']
        ln= request.POST['lastname']
        em= request.POST['email']
        bi= request.POST['bio']
        gn= request.POST['gender']
        cn= request.POST['country']
        ci= request.POST['city']
        ph= request.POST['phone']

        usr = User.objects.get(id=request.user.id)
        usr.email = em
        usr.first_name = fn
        usr.last_name = ln
        usr.save()

        data.bio = bi
        data.gender = gn
        data.country = cn
        data.city = ci
        data.phone = ph
        data.save()

        if 'image' in request.FILES:
            img = request.FILES['image']
            data.image =img
            data.save()
            
        context['status'] = "Changes Saved"

    return render(request, 'users/profile.html', context)
    