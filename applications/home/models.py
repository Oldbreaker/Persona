from django.db import models


class Persona(models.Model):
    Entidad_Federativa = models.CharField(max_length=35)
    Municipio = models.CharField(max_length=35)

    class Meta:
        abstract = True


class PersonaFisica(Persona):
    Nombre = models.CharField(max_length=20)
