from collections import Counter
from applications.home.models import PersonaFisica
from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serealizers import PersonSerializer


class ObtenerMasRepetido(CreateAPIView):
    serializer_class = PersonSerializer
    queryset = PersonaFisica.objects.all()

    def post(self, request, ):
        serealizer = self.get_serializer(data=request.data, many=True)
        serealizer.is_valid(raise_exception=True)
        self.perform_create(serealizer)
        name = serealizer.data
        counter = Counter(item["Nombre"] for item in name)
        repetido = counter.most_common(1)
        return Response(repetido)
