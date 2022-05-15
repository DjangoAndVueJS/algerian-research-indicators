from django.urls import path
from . import views

urlpatterns = [
    path('apiUrls/', views.apiOverView, name='listApiUrls'),
    path('location-list/', views.Locationslist, name='location-list'),
    path('location-create/', views.LocationsCreate,
         name='create-researchers'),
]
