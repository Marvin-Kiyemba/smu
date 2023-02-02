from django.urls import path, include
from . import views
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
   path('', TemplateView.as_view(template_name="home.html"),name="home"),
   path('index', views.index, name="index"),
   path('list', views.AssetListView, name='list'),
   path('accounts', include('django.contrib.auth.urls')),
]