from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from users.views import logout_view
from users.views import assets
from .views import show_records, add_user
from .views import search_records
from .views import search_assets

urlpatterns = [
    path("", TemplateView.as_view(template_name='home.html'), name="home"),
    path('records/<int:assigned_to_id>/', show_records, name='show_records'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/", views.accounts, name="accounts"),
    path('add_user/', add_user, name='add_user'),
    path('assets/', assets, name='assets'),
    path('search/', search_assets, name='search-assets'),
    path('search_records/', search_records, name='search_records'),
    
]
