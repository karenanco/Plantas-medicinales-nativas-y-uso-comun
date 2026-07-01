from django.db import models
from django.contrib.auth.models import User


class Planta(models.Model):
    ORIGEN_CHOICES = [
        ("NATIVA", "Nativa de Chile"),
        ("ASILVESTRADA", "Asilvestrada de Uso Tradicional"),
    ]

    ZONA_CHOICES = [
        ("NORTE", "Norte"),
        ("CENTRO", "Centro"),
        ("SUR", "Sur"),
        ("PATAGONIA", "Patagonia"),
    ]

    nombre_comun = models.CharField(max_length=150)
    nombre_cientifico = models.CharField(max_length=200, unique=True)
    familia_botanica = models.CharField(max_length=150)
    origen = models.CharField(max_length=25, choices=ORIGEN_CHOICES)

    # Geolocalización
    zona_macro = models.CharField(max_length=15, choices=ZONA_CHOICES)
    regiones = models.TextField(help_text="Lista de regiones separadas por comas")
    habitat = models.TextField()

    # Identificación Morfológica Detallada
    descripcion_hoja = models.TextField()
    descripcion_tallo = models.TextField()
    descripcion_flor = models.TextField()
    foto_real = models.URLField(help_text="URL de imagen real referencial o Pl@ntNet")

    # Clasificación de Usos e Interfaz Terapéutica
    uso_principal = models.CharField(
        max_length=100, help_text="Ej: Medicinal, Comestible, Venenosa"
    )
    efecto_terapeutico = models.CharField(
        max_length=150, help_text="Ej: Hepático, cicatrizante, ansiolítico"
    )
    receta_preparacion = models.TextField()
    advertencias = models.TextField()

    class Meta:
        verbose_name_plural = "Plantas"

    def __str__(self) -> str:
        return f"{self.nombre_comun} ({self.nombre_cientifico})"


class Favorito(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favoritos"
    )
    planta = models.ForeignKey(
        Planta, on_delete=models.CASCADE, related_name="favoritos"
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Favoritos"
        unique_together = ("usuario", "planta")

    def __str__(self) -> str:
        return f"{self.usuario} - {self.planta}"
