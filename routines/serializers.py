# routines/serializers.py
from rest_framework import serializers
from .models import Routine

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ["id", "user", "name", "created_at"]
        read_only_fields = ["id", "user", "created_at"]
