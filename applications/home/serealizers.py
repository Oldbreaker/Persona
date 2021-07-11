from django.db.models import fields
from rest_framework import serializers
from .models import PersonaFisica


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaFisica
        fields = ('__all__')
