from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from accounts import models as accounts_models
from api import serializers
from rest_framework.parsers import JSONParser


# List of all urls
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Create Simple Researcher': '/createResearcherUser/',
    }
    return Response(api_urls)


@api_view(['GET'])
def Locationslist(request):
    researchers = accounts_models.Location.objects.all()
    serializer = serializers.LocationSerializer(researchers, many=True)
    return Response(serializer.data)


#  Post


@api_view(['POST'])
@csrf_exempt
def LocationsCreate(request):
    serializer = serializers.LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
