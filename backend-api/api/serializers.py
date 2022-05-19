import email
from rest_framework import serializers
from accounts import models as accounts_models


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts_models.Location
        fields = '__all__'

class CherSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts_models.Researcher
        fields = '__all__'


class EtaSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts_models.Etablisment
        fields = '__all__'
        

class DivSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts_models.Division
        fields = '__all__'   
        
        
class LaboSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts_models.Laboratoire
        fields = '__all__'
        
class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts_models.Equipe
        fields = '__all__'        