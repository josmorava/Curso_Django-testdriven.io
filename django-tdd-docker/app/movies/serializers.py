from dataclasses import field
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
  """Modelo serializador a usar"""
  class Meta:
    model = Movie
    fields= '__all__'
    read_only_fields=('id','created_date', 'updated_date')