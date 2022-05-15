import email
from rest_framework import serializers
from accounts import models as accounts_models


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts_models.Location
        fields = '__all__'
