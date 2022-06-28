from rest_framework import serializers
from core import models


class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projeto
        fields = '__all__'
