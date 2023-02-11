from django.shortcuts import render
# Create your views here.
from users.constants import USER_TYPE_CHOICES as user_constants
from users.models import User
from records.models import Record
from pyexpat.errors import messages
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate

@login_required
def add_user(request):
    if request.user.user_type != user_constants.SUPERUSER:
        raise PermissionDenied
    if request.method == 'POST':
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        user = User.objects.create(
            email=email,
            user_type=user_type,
        )
        return redirect('accounts')
    return render(request, 'registration/add_user.html')

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
            return render("registration/login.html",{}, context)
    else:
        #the login is a GET request, so just show the user thee login form
        return render('registration/login.html', {}, context)

def dashboard(request):
    records = Record.objects.all()
    return render(request, 'dashboard.html', {'records':records})

def logout_view(request):
    print("Logout view called")
    logout(request)
    return render(request, 'registration/logged_out.html')

def show_records(request, assigned_to_id):
    records = Record.objects.filter(assigned_to_id=assigned_to_id)
    return render(request, 'dashboard.html', {'records': records})

def search_records(request):
    q = request.GET.get('q')
    if q:
        assigned_to = User.objects.filter(email__icontains=q)
        records = Record.objects.filter(assigned_to__in=assigned_to)
    else:
        records = Record.objects.all()
    return render(request, 'dashboard.html', {'records': records})

def accounts(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users':users})

def accounts(request):
    search_query = request.GET.get('search_query', '')
    users = User.objects.filter(email__icontains=search_query)
    return render(request, 'users.html', {'users': users})