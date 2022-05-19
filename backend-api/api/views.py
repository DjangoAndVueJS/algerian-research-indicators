from __future__ import division
from ast import Div, Return
from tkinter.tix import Tree
from typing import final
from django.http import JsonResponse
from django.shortcuts import render
from requests import request
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from accounts import models as accounts_models
from api import serializers
from rest_framework.parsers import JSONParser
from requests import request
# permission
from rest_framework import generics, permissions


# List of all urls
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        # home
        'Home': '/home/',
        'TESt': '/test/',
        # Location
        'List-wilaya': '/list-location/',
        'Create': '/location-create/',
        'Update': '/location-update/<str:pk>/',
        'Delete': '/location-delete/<str:pk>/',

        # Etablisment
        'List-Eta': '/list-Etablisment/',
        'Create': '/etablisment-create/',
        'Update': '/etablisment-update/<str:pk>/',
        'Delete': '/etablisment-delete/<str:pk>/',

        # Division
        'List-Div': '/list-Etablisment/',
        'Create': '/div-create/',
        'Update': '/div-update/<str:pk>/',
        'Delete': '/div-delete/<str:pk>/',

        # Laboratoire
        'List-Lab': '/labo-list/',
        'List-Lab-div': '/labo-list-div/',
        'List-Lab-eta': '/labo-list-eta/',
        'Create': '/lobo-create/',
        'Update': '/lobo-update/<str:pk>/',
        'Delete': '/lobo-delete/<str:pk>/',

        # Equipe
        'List-Equipe': '/list-Equipe/',
        'List-Equipe-Lab': '/list-Equipe-Lab/',
        'List-Equipe-Lab': '/list-Equipe-div/',
        'List-Equipe-Lab': '/list-Equipe-eta/',
        'Create': '/equipe-create/',
        'Update': '/equipe-update/<str:pk>/',
        'Delete': '/equipe-delete/<str:pk>/',

        # Chercheur
        'List-ch-Equipe': '/list-ch-equipe/<str:pk>/',
        'List-ch-Labo': '/list-ch-labo/<str:pk>/',
        'List-ch-Div': '/list-ch-div/<str:pk>/',
        'List-ch-Eta': '/list-ch-eta/<str:pk>/',
        'Create': '/ch-create/',
        'Update': '/ch-update/<str:pk>/',
        'Delete': '/ch-delete/<str:pk>/',
    }
    return Response(api_urls)


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)  # new
    queryset = accounts_models.Researcher.objects.all()
    serializer_class = serializers.CherSerializer


# Home page

def Home_page(request):
    labos = accounts_models.Laboratoire.objects.all()
    chercheurs = accounts_models.Researcher.objects.all()
    divisions = accounts_models.Division.objects.all()
    etablisments = accounts_models.Etablisment.objects.all()
    # pour affichage
    Total_labo = labos.count() - 1
    Total_chercheur = chercheurs.count() - 1
    Total_etablisment = etablisments.count() - 1
    Total_division = divisions.count() - 1
    context = {
        'Total_labo': Total_labo,
        'Total_chercheur': Total_chercheur,
        'Total_etablisment': Total_etablisment,
        'Total_division': Total_division
    }

    return Response(context.data)


# ----------------------------------------------------------------------------------
# Location
"""List"""


@api_view(['GET'])
def LocationList(request):
    researchers = accounts_models.Location.objects.all()
    serializer = serializers.LocationSerializer(researchers, many=True)
    return Response(serializer.data)


"""Create"""


@api_view(['POST'])
@csrf_exempt
def LocationCreate(request):
    serializer = serializers.LocationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


"""Update"""


@api_view(['POST'])
@csrf_exempt
def LocationUpdate(request, pk):
    location = accounts_models.Location.objects.get(id=pk)
    serializer = serializers.LocationSerializer(
        instance=location, date=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


"""Delete"""


@api_view(['DELETE'])
def LocationDelete(request, pk):
    location = accounts_models.Location.objects.get(id=pk)
    location.delete()

    return Response(" Wilaya supprime avec succes")


# ===================================
# Etablisment
"""List"""


@api_view(['GET'])
def EtablismentList(request):
    researchers = accounts_models.Etablisment.objects.all()
    serializer = serializers.EtaSerializer(researchers, many=True)
    return Response(serializer.data)


"""Create"""


@api_view(['POST'])
@csrf_exempt
def EtablismentCreate(request):
    serializer = serializers.EtaSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


"""Update"""


@api_view(['POST'])
@csrf_exempt
def EtablismentUpdate(request, pk):
    location = accounts_models.Location.objects.get(id=pk)
    serializer = serializers.EtaSerializer(
        instance=location, date=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


"""Delete"""


@api_view(['DELETE'])
def EtablismentDelete(request, pk):
    location = accounts_models.Etablisment.objects.get(id=pk)
    location.delete()

    return Response(" Wilaya supprime avec succes")


# ===================================
# Division
"""List"""


@api_view(['GET'])
def DivisionList(request):
    researchers = accounts_models.Division.objects.all()
    serializer = serializers.DivSerializer(researchers, many=True)
    return Response(serializer.data)


"""Create"""


@api_view(['POST'])
@csrf_exempt
def DivisionCreate(request):
    serializer = serializers.DivSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


"""Update"""


@api_view(['POST'])
@csrf_exempt
def DivisionUpdate(request, pk):
    location = accounts_models.Division.objects.get(id=pk)
    serializer = serializers.DivSerializer(
        instance=location, date=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


"""Delete"""


@api_view(['DELETE'])
def DivisionDelete(request, pk):
    location = accounts_models.Division.objects.get(id=pk)
    location.delete()

    return Response(" Wilaya supprime avec succes")


# ===================================
# Equipe
"""List"""


@api_view(['GET'])
def EquipeList(request):
    researchers = accounts_models.Equipe.objects.all()
    serializer = serializers.EquipeSerializer(researchers, many=True)
    return Response(serializer.data)

# les equipe d'un labo


@api_view(['GET'])
def EquipeList_Lab(request, pk):
    researchers = accounts_models.Researcher.objects.filter(laboratoire=pk)
    serializer = serializers.EquipeSerializer(researchers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def EquipeList_Div(request, pk):  # pk est l'id de devision
    inter = accounts_models.Laboratoire.objects.filter(division=pk)
    researchers = accounts_models.Equipe.objects.none()
    inter2 = []
    for i in inter:
        researchers = accounts_models.Equipe.objects.filter(laboratoire=i.id)
        inter2 += researchers

    serializer = serializers.EquipeSerializer(inter2, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def EquipeList_Eta(request, pk):
    inter = accounts_models.Division.objects.filter(etablisment=pk)
    researchers = accounts_models.Laboratoire.objects.none()
    inter3 = []

    for i in inter:
        researchers = accounts_models.Laboratoire.objects.filter(division=i.id)
        inter3 += researchers
    inter2 = []
    for i in inter:
        researchers = accounts_models.Equipe.objects.filter(laboratoire=i.id)
        inter2 += researchers

    serializer = serializers.EquipeSerializer(inter2, many=True)
    return Response(serializer.data)


"""Create"""


@api_view(['POST'])
@csrf_exempt
def EquipeCreate(request):
    serializer = serializers.EquipeSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


"""Update"""


@api_view(['POST'])
@csrf_exempt
def EquipeUpdate(request, pk):
    location = accounts_models.LocatioEquipe.objects.get(id=pk)
    serializer = serializers.EquipeSerializer(
        instance=location, date=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


"""Delete"""


@api_view(['DELETE'])
def EquipeDelete(request, pk):
    location = accounts_models.Equipe.objects.get(id=pk)
    location.delete()

    return Response(" Wilaya supprime avec succes")


# ===================================
# Laboratoire
"""List"""


@api_view(['GET'])
def LaboratoireList(request):
    researchers = accounts_models.Laboratoire.objects.all()
    serializer = serializers.LaboSerializer(researchers, many=True)
    return Response(serializer.data)

# les laboratoire d'un division


def LaboratoireList_Div(request, pk):
    researchers = accounts_models.Laboratoire.objects.filter(division=pk)
    serializer = serializers.LaboSerializer(researchers, many=True)
    return Response(serializer.data)

# les laboratoire d'un eta


def LaboratoireList_Eta(request, pk):
    inter = accounts_models.Division.objects.filter(etablisment=pk)
    researcher = accounts_models.Laboratoire.objects.none()

    inter2 = []
    for i in inter:
        researcher = accounts_models.Laboratoire.objects.filter(division=i.id)
        inter2 += researcher

    serializer = serializers.LaboSerializer(inter2, many=True)
    return Response(serializer.data)


"""Create"""


@api_view(['POST'])
@csrf_exempt
def LaboratoireCreate(request):
    serializer = serializers.LaboSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


"""Update"""


@api_view(['POST'])
@csrf_exempt
def LaboratoireUpdate(request, pk):
    location = accounts_models.Laboratoire.objects.get(id=pk)
    serializer = serializers.EtaSerializer(
        instance=location, date=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


"""Delete"""


@api_view(['DELETE'])
def LaboratoireDelete(request, pk):
    location = accounts_models.Laboratoire.objects.get(id=pk)
    location.delete()

    return Response(" Wilaya supprime avec succes")


# ===================================
# Chercheur
@api_view(['POST'])
@csrf_exempt
def CherCreate(request):
    serializer = serializers.LaboSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


"""List"""  # liste avec les privilege (equipe , labo )
# affiche les chercheur d'un equipe


@api_view(['GET'])
def CherList_equipe(request, pk):  # pk represent l'id de l'equipe (rest a test)
    researchers = accounts_models.Researcher.objects.filter(
        equipe_researchers=pk)
    serializer = serializers.CherSerializer(researchers, many=True)
    return Response(serializer.data)

# afficher les chercheur d'un laboratoire


@api_view(['GET'])
def CherList_labo(request, pk):

    inter = accounts_models.Equipe.objects.filter(laboratoire=pk)
    researchers = accounts_models.Researcher.objects.none()
    inter2 = []
    for i in inter:
        researchers = accounts_models.Researcher.objects.filter(
            equipe_researchers=i.id)
        inter2 += researchers

    serializer = serializers.CherSerializer(inter2, many=True)
    return Response(serializer.data)

# afficher les chercheur d'un division


@api_view(['GET'])
def CherList_div(request, pk):
    inter = accounts_models.Laboratoire.objects.filter(division=pk)
    interEquipe = accounts_models.Equipe.objects.none()
    inter2 = []
    for i in inter:
        interEquipe = accounts_models.Equipe.objects.filter(laboratoire=i.id)
        inter2 += interEquipe

    final = []
    for i in inter2:
        researchers = accounts_models.Researcher.objects.filter(
            equipe_researchers=i.id)
        final += researchers

    serializer = serializers.CherSerializer(final, many=True)
    return Response(serializer.data)

# afficher les chercheur d'un  Etablisment


@api_view(['GET'])
def CherList_eta(request, pk):
    inter = accounts_models.Division.objects.filter(etablisment=pk)
    interLaboratoire = accounts_models.Equipe.objects.none()
    inter3 = []
    # recuperation des Laboratoire
    for i in inter:
        interLaboratoire = accounts_models.Laboratoire.objects.filter(
            division=i.id)
        inter3 += interLaboratoire
    # recuperation des Equipe
    inter2 = []
    for i in inter3:
        interEquipe = accounts_models.Equipe.objects.filter(laboratoire=i.id)
        inter2 += interEquipe
    # recuperation des chercheur
    final = []
    for i in inter2:
        researchers = accounts_models.Researcher.objects.filter(
            equipe_researchers=i.id)
        final += researchers

    serializer = serializers.CherSerializer(final, many=True)
    return Response(serializer.data)


"""Update"""


@api_view(['POST'])
@csrf_exempt
def CherUpdate(request, pk):
    location = accounts_models.Laboratoire.objects.get(id=pk)
    serializer = serializers.EtaSerializer(
        instance=location, date=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""Delete"""


@api_view(['DELETE'])
def CherDelete(request, pk):
    location = accounts_models.Laboratoire.objects.get(id=pk)
    location.delete()
    return Response(" Wilaya supprime avec succes")


# class CherList_labo(generics.RetrieveUpdateDestroyAPIView):
#     inter=[]
#     def cc(inter,pk):
#        inter = accounts_models.Equipe.objects.filter(laboratoire = pk)
#        researchers = accounts_models.Researcher.objects.none()
#        inter2 =[]
#        for i in inter:
#           researchers = accounts_models.Researcher.objects.filter(equipe_researchers = i.id)
#           inter2 +=researchers
#        return inter2
#     inter=cc(inter,1)
#     queryset = inter
#     serializer_class = serializers.CherSerializer
