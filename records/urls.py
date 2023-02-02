from django.urls import path
from rest_framework import routers
from .views import record_list, record_detail



urlpatterns = [
    path('', record_list),
    path('detail/<int:pk>/',record_detail),
]
