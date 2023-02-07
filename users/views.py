from django.shortcuts import render
# Create your views here.

from pyexpat.errors import messages
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from users.managers import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

def signup(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User Created'
            return redirect('login')
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html')

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('dashboard/')
        #messages.info(request,'Account not found')
        if request.method == 'POST':
                email = request.POST.get('email')
                password = request.POST.get('password')
                user_obj = User.objects.filter(email = email)
                if not user_obj.exists():
                    messages.info(request, 'Account not Found')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                user_obj = authenticate(email =email, password = password)

                if user_obj and user_obj.is_superuser:
                    login(request, user_obj)
                    return redirect('dashboard/')

                messages.info(request, 'Invalid password')
                return redirect('/')
        return render(request, 'login.html')
    except Exception as e:
        print(e)


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate( email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #redirects to index page.
                return HttpResponseRedirect("home.html")
            else:
                #Returns a 'disabled account' error message
                return HttpResponseRedirect("Your account has been disabled.")
        else:
            #Return an 'invalid login' error message.
            #print "invalid login details" + email + "" + password
            return render("login.html",{}, context)
    else:
        #the login is a GET request, so just show the user thee login form
        return render('login.html', {}, context)

def dashboard(request):
    return render(request, 'base.html')

def logout(request):
    return render(request, 'base.html')