from django.contrib import admin

from .models import Favorito, Planta


@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_comun",
        "nombre_cientifico",
        "familia_botanica",
        "origen",
        "zona_macro",
    )
    list_filter = ("origen", "zona_macro", "uso_principal")
    search_fields = ("nombre_comun", "nombre_cientifico", "familia_botanica")


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "planta", "creado_en")
    list_filter = ("creado_en",)
    search_fields = ("usuario__username", "planta__nombre_comun")
