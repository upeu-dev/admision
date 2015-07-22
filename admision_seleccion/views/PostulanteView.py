from django.shortcuts import render
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from admision_seleccion.models.Postulante import Postulante
# Serializers define the API representation.

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework import permissions


class ApiEndpoint(ProtectedResourceView):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


class PostulanteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Postulante
        fields = ('id', 'nombre', 'codigo')


class MiPermission(permissions.BasePermission):

    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        #ip_addr = request.META['REMOTE_ADDR']
        #blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        if request.user.has_perms(('configs.add_escuela',)):
            return True
        return False
# ViewSets define the view behavior.


class PostulanteViewSet(viewsets.ModelViewSet):
    queryset = Postulante.objects.all()
    serializer_class = PostulanteSerializer
    #required_scopes = ['groups']
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    #permission_classes = [permissions.IsAuthenticated, MiPermission]
