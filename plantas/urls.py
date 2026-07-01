"""
URL configuration for the plantas app.

Defines all URL patterns for the botanical catalog application.
Uses function-based views (FBVs) exclusively as per project requirements.
"""

from django.urls import path

from plantas import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("planta/<int:planta_id>/", views.detalle_planta, name="detalle_planta"),
    path("identificar/", views.identificar, name="identificar"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("favorito/<int:planta_id>/", views.toggle_favorito, name="toggle_favorito"),
]
