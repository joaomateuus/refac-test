from rest_framework import viewsets
from core import models, serializers


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = models.Projeto.objects.all()
    serializer_class = serializers.ProjetoSerializer
