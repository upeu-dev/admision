from django.contrib import admin
from admision_seleccion.models.Modalidad import Modalidad

from admision_seleccion.models.Postulante import Postulante
# Register your models here.


class ModalidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo")
    search_fields = ("nombre",  "codigo")


admin.site.register(Modalidad, ModalidadAdmin)


class PostulanteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo")
    search_fields = ("nombre",  "codigo")


admin.site.register(Postulante, PostulanteAdmin)
