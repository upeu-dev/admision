# _*_ coding: utf-8 _*_
from django.db import models
import uuid


class Modalidad(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    #jerarquia_acad = models.ForeignKey(JerarquiaAcad, null=True, blank=True)

    class Meta:

        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"

    def __str__(self):
        return self.nombre
