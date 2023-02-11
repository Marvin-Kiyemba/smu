from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from users.views import logout_view

from .views import show_records, add_user

urlpatterns = [
    path("", TemplateView.as_view(template_name='home.html'), name="home"),
    path('records/<int:assigned_to_id>/', show_records, name='show_records'),
    path("login/", views.user_login, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/", views.accounts, name="accounts"),
    path('add_user/', add_user, name='add_user'),
]
