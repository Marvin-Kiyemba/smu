from django.shortcuts import render
# Create your views here.
from users.constants import USER_TYPE_CHOICES as user_constants
from users.models import User, UserProfile
from records.models import Record
from assets.models import Asset
from django.contrib import messages
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from .forms import SignUpForm, AssetForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def add_user(request):
    if request.user.user_type != User.SUPER_USER:
        raise PermissionDenied("You do not have permission to add user")
    
    if request.method == 'POST':
        form = SignUpForm()
        if form.is_valid():
            user = form.save(commit=False)
            if not user.user_type:
                user.user_type = User.STAFF
            user.save()
            messages.success(request,'User added Successfully')
            return redirect('accounts')
    else:
        form = SignUpForm()
    return render(request, 'registration/add_user.html', {'form':form})

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('dashboard')
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


def login(request):
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
    
@login_required
def dashboard(request): 
    user = request.user
    if user.is_superuser:
        records = Record.objects.all()
    else:
       records = Record.objects.filter(assigned_to__user_profile__user__department=user.department)
    return render(request, 'dashboard.html', {'records': records})


def logout_view(request):
    print("Logout view called")
    logout(request)
    return render(request, 'registration/logged_out.html')

def show_records(request, assigned_to_id):
    records = Record.objects.filter(assigned_to_id=assigned_to_id)
    return render(request, 'dashboard.html', {'records': records})

def search_records(request, email):
    email = request.GET.get('assigned_to')
    user = User.objects.get(email=email)
    records = Record.objects.filter(assigned_to=user.id)
    context = {'records': records}
    return render(request, 'dashboard.html', context)

def accounts(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users':users})

def accounts(request):
    search_query = request.GET.get('search_query', '')
    users = User.objects.filter(email__icontains=search_query)
    return render(request, 'users.html', {'users': users})

def assets(request):
    assets = Asset.objects.all()
    return render(request, 'assets.html', {'assets': assets})

def search_assets(request):
    query = request.GET.get('q')
    if query:
        assets = Asset.objects.filter(asset_type__icontains=query) | Asset.objects.filter(asset_code__icontains=query)
    else:
        assets = Asset.objects.all()
    return render(request, 'assets.html', {'assets': assets})

def user_profile(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    context = {'user_profile': user_profile}
    return render(request, 'user_profile.html', context)

@login_required
def add_asset(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AssetForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            asset = form.save(commit=False)
            asset.added_by = request.user
            asset.save()
            messages.success(request, 'Asset added successfully.')
            return redirect('assets')
    else:
            form = AssetForm()
    return render(request, 'add_asset.html', {'form': form})