from rest_framework import serializers
from .models import TestModel01

class TestModel01Serializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel01
        fields = '__all__'