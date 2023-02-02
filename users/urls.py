from django.urls import path, include
from  . import views 
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name='home.html'), name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard")
]
