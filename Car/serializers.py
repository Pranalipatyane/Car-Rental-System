from rest_framework import serializers
from .models import Addcar

class AddcarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addcar
        fields = '__all__'










