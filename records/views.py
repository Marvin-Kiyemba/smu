from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import RecordSerializer, AssetSerializer
from .models import Record
from assets.models import Asset

class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    

class AssetView(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer 