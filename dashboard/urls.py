from django.urls import path
from . import views
from assets.models import Asset
from records.models import Record

app_name = "dashboard"
urlpatterns = [
    path('', views.index, name='index' ),
    path('asset', views.asset, name='asset'),

]