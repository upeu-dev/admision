# _*_ coding: utf-8 _*_
from django.db import models


class Postulante(models.Model):

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    #jerarquia_acad = models.ForeignKey(JerarquiaAcad, null=True, blank=True)

    class Meta:
        verbose_name = "Postulante"
        verbose_name_plural = "Postulantes"

    def __str__(self):
        return self.nombre
