from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status 
from .models import Record
from .serializers import RecordSerializer
from rest_framework.response import Response

@api_view(['GET','POST'])
def record_list(request):
    if request.method == 'GET':
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def record_detail(request, pk):
    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': 
        serializer = RecordSerializer(record, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecordSerializer(record, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)