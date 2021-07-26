from rest_framework import serializers
from .models import ApiCall


class ApiCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiCall
        fields = ('id', 'name', 'favorite')