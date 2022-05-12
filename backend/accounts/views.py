from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Researcher


# A view to list all api endpoints
@api_view(['GET'])
def apiEndpointsView(request):
    api_urls = {
        'list_researchers': '/list_researchers/',
        'index': '/index/'
    }
    return Response(api_urls)
