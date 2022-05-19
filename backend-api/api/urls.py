from django.urls import path

from accounts import views
from .views import *
urlpatterns = [
    #  path('apiUrls/', apiOverView, name='listApiUrls'),
    #Home
    path('home/', Home_page, name='home'),
    path('test/', PostList.as_view(), name='test'),

    #Location
    path('location-list/', LocationList, name='location-list'),
    path('location-create/', LocationCreate,name='location-create'),
    path('location-update/<str:pk>/', LocationUpdate,name='location-update'),
    path('location-delete/<str:pk>/', LocationDelete,name='location-delete'),
    
    # Etablisment
    path('etablisment-list/', EtablismentList, name='etablisment-list'),
    path('etablisment-create/', EtablismentCreate,name='etablisment-create'),
    path('etablisment-update/<str:pk>/', EtablismentUpdate,name='etablisment-update'),
    path('etablisment-delete/<str:pk>/', EtablismentDelete,name='etablisment-delete'),
    
    # Division
    path('div-list/', DivisionList, name='div-list'),
    path('div-create/', DivisionCreate,name='div-create'),
    path('div-update/<str:pk>/', DivisionUpdate,name='div-update'),
    path('div-delete/<str:pk>/', DivisionDelete,name='div-delete'),
    
    # Laboratoire
    path('labo-list/', LaboratoireList, name='labo-list'),
    path('labo-list-div/', LaboratoireList_Div, name='labo-list-div'),
    path('labo-list-eta/<str:pk>/', LaboratoireList_Eta, name='labo-list-eta'),
    path('labo-create/<str:pk>/', LaboratoireCreate,name='labo-create'),
    path('labo-update/<str:pk>/', LaboratoireUpdate,name='labo-update'),
    path('labo-delete/<str:pk>/', LaboratoireDelete,name='labo-delete'),
    
    # Equipe
    path('equipe-list/', EquipeList, name='equipe-list'),
    path('equipe-list-lab/<str:pk>/', EquipeList_Lab, name='equipe-list-lab'),
    path('equipe-list-div/<str:pk>/', EquipeList_Div, name='equipe-list-div'),
    path('equipe-list-eta/<str:pk>/', EquipeList_Eta, name='equipe-list-eta'),
    path('equipe-create/', EquipeCreate,name='equipe-create'),
    path('equipe-update/<str:pk>/', EquipeUpdate,name='equipe-update'),
    path('equipe-delete/<str:pk>/', EquipeDelete,name='equipe-delete'),
    
    #Chercheur
    path('ch-list-equipe/<str:pk>/', CherList_equipe, name='ch-list-equipe'),
    path('ch-list-labo/<str:pk>/',CherList_labo, name='ch-list-labo'),
    path('ch-list-div/<str:pk>/', CherList_div, name='ch-list-div'),
    path('ch-list-eta/<str:pk>/', CherList_eta, name='ch-list-eta'),
    path('ch-create/', CherCreate,name='ch-create'),
    path('ch-update/<str:pk>/', CherUpdate,name='ch-update'),
    path('ch-delete/<str:pk>/', CherDelete,name='ch-delete'),
]
