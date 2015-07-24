from django.shortcuts import render
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from admision_seleccion.models.Modalidad import Modalidad
# Serializers define the API representation.

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework import permissions
from .PostulanteView import PostulanteSerializer


class ModalidadSerializer(serializers.ModelSerializer):

    postulante_set = PostulanteSerializer(many=True, read_only=True)

    class Meta:
        model = Modalidad
        # fields = ('id', 'nombre', 'codigo')


class ModalidadViewSet(viewsets.ModelViewSet):
    queryset = Modalidad.objects.all()
    serializer_class = ModalidadSerializer
    # required_scopes = ['groups']
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
