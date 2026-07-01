"""
Comprehensive tests for the plantas application.

Covers models, views, filters, authentication, and edge cases.
"""

from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Planta, Favorito


# =============================================================================
# Model Tests — Planta
# =============================================================================

class PlantaModelTests(TestCase):
    """Tests for the Planta model creation, constraints, and validation."""

    @classmethod
    def setUpTestData(cls):
        cls.plant = Planta.objects.create(
            nombre_comun="Boldo",
            nombre_cientifico="Peumus boldus",
            familia_botanica="Monimiaceae",
            origen="NATIVA",
            zona_macro="CENTRO",
            regiones="Metropolitana, O'Higgins",
            habitat="Bosques esclerófilos",
            descripcion_hoja="Hojas ovaladas, opuestas, coriáceas",
            descripcion_tallo="Tronco corto y ramificado",
            descripcion_flor="Flores pequeñas, dioicas",
            foto_real="https://example.com/boldo.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Hepático",
            receta_preparacion="Infusión de hojas",
            advertencias="No usar durante el embarazo",
        )

    def test_planta_creation_with_all_fields(self):
        """A Planta instance is created with all required fields populated."""
        plant = Planta.objects.get(nombre_cientifico="Peumus boldus")
        self.assertEqual(plant.nombre_comun, "Boldo")
        self.assertEqual(plant.nombre_cientifico, "Peumus boldus")
        self.assertEqual(plant.familia_botanica, "Monimiaceae")
        self.assertEqual(plant.origen, "NATIVA")
        self.assertEqual(plant.zona_macro, "CENTRO")
        self.assertEqual(plant.regiones, "Metropolitana, O'Higgins")
        self.assertEqual(plant.habitat, "Bosques esclerófilos")
        self.assertEqual(plant.descripcion_hoja, "Hojas ovaladas, opuestas, coriáceas")
        self.assertEqual(plant.descripcion_tallo, "Tronco corto y ramificado")
        self.assertEqual(plant.descripcion_flor, "Flores pequeñas, dioicas")
        self.assertEqual(plant.foto_real, "https://example.com/boldo.jpg")
        self.assertEqual(plant.uso_principal, "Medicinal")
        self.assertEqual(plant.efecto_terapeutico, "Hepático")
        self.assertEqual(plant.receta_preparacion, "Infusión de hojas")
        self.assertEqual(plant.advertencias, "No usar durante el embarazo")

    def test_planta_string_representation(self):
        """The string representation includes common and scientific name."""
        plant = Planta.objects.get(nombre_cientifico="Peumus boldus")
        expected = "Boldo (Peumus boldus)"
        self.assertEqual(str(plant), expected)

    def test_nombre_cientifico_unique_constraint(self):
        """Duplicate scientific names raise an IntegrityError."""
        with self.assertRaises(Exception):
            Planta.objects.create(
                nombre_comun="Boldo duplicado",
                nombre_cientifico="Peumus boldus",  # same as existing
                familia_botanica="Monimiaceae",
                origen="NATIVA",
                zona_macro="CENTRO",
                regiones="Metropolitana",
                habitat="Bosques",
                descripcion_hoja="Hojas ovaladas",
                descripcion_tallo="Tronco corto",
                descripcion_flor="Flores pequeñas",
                foto_real="https://example.com/boldo2.jpg",
                uso_principal="Medicinal",
                efecto_terapeutico="Hepático",
                receta_preparacion="Infusión",
                advertencias="Ninguna",
            )

    def test_origen_choices_valid_values(self):
        """Origen field accepts NATIVA and ASILVESTRADA with correct display."""
        nativa = Planta.objects.create(
            nombre_comun="Matico",
            nombre_cientifico="Buddleja globosa",
            familia_botanica="Scrophulariaceae",
            origen="NATIVA",
            zona_macro="SUR",
            regiones="La Araucanía",
            habitat="Riberas",
            descripcion_hoja="Hojas lanceoladas",
            descripcion_tallo="Arbusto",
            descripcion_flor="Flores globosas",
            foto_real="https://example.com/matico.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Cicatrizante",
            receta_preparacion="Hervir",
            advertencias="Ninguna",
        )
        self.assertEqual(nativa.origen, "NATIVA")
        self.assertEqual(nativa.get_origen_display(), "Nativa de Chile")

        asilvestrada = Planta.objects.create(
            nombre_comun="Zanahoria silvestre",
            nombre_cientifico="Daucus carota",
            familia_botanica="Apiaceae",
            origen="ASILVESTRADA",
            zona_macro="CENTRO",
            regiones="Metropolitana",
            habitat="Terrenos alterados",
            descripcion_hoja="Hojas compuestas",
            descripcion_tallo="Tallo erecto",
            descripcion_flor="Flores blancas",
            foto_real="https://example.com/zanahoria.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Digestivo",
            receta_preparacion="Infusión",
            advertencias="Sin conocidas",
        )
        self.assertEqual(asilvestrada.origen, "ASILVESTRADA")
        self.assertEqual(
            asilvestrada.get_origen_display(), "Asilvestrada de Uso Tradicional"
        )

    def test_zona_choices_valid_values(self):
        """Zona_macro field accepts NORTE, CENTRO, SUR, PATAGONIA."""
        norte = Planta.objects.create(
            nombre_comun="Cactus",
            nombre_cientifico="Echinopsis chiloensis",
            familia_botanica="Cactaceae",
            origen="NATIVA",
            zona_macro="NORTE",
            regiones="Atacama",
            habitat="Desierto",
            descripcion_hoja="Espinas",
            descripcion_tallo="Suculento",
            descripcion_flor="Flores grandes",
            foto_real="https://example.com/cactus.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Digestivo",
            receta_preparacion="Maceración",
            advertencias="Ninguna",
        )
        self.assertEqual(norte.zona_macro, "NORTE")
        self.assertEqual(norte.get_zona_macro_display(), "Norte")


# =============================================================================
# Model Tests — Favorito
# =============================================================================

class FavoritoModelTests(TestCase):
    """Tests for the Favorito model creation and constraints."""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", password="TestPass123!"
        )
        cls.plant = Planta.objects.create(
            nombre_comun="Boldo",
            nombre_cientifico="Peumus boldus",
            familia_botanica="Monimiaceae",
            origen="NATIVA",
            zona_macro="CENTRO",
            regiones="Metropolitana",
            habitat="Bosques esclerófilos",
            descripcion_hoja="Hojas ovaladas",
            descripcion_tallo="Tronco corto",
            descripcion_flor="Flores pequeñas",
            foto_real="https://example.com/boldo.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Hepático",
            receta_preparacion="Infusión",
            advertencias="No en embarazo",
        )

    def test_favorito_creation(self):
        """A Favorito instance is created with user and plant."""
        fav = Favorito.objects.create(usuario=self.user, planta=self.plant)
        self.assertEqual(fav.usuario, self.user)
        self.assertEqual(fav.planta, self.plant)
        self.assertIsNotNone(fav.creado_en)
        self.assertEqual(Favorito.objects.count(), 1)

    def test_favorito_unique_together_constraint(self):
        """Duplicate user-plant pairs raise an IntegrityError."""
        Favorito.objects.create(usuario=self.user, planta=self.plant)
        with self.assertRaises(Exception):
            Favorito.objects.create(usuario=self.user, planta=self.plant)

    def test_favorito_string_representation(self):
        """The string representation includes user and plant info."""
        fav = Favorito.objects.create(usuario=self.user, planta=self.plant)
        expected = f"{self.user} - {self.plant}"
        self.assertEqual(str(fav), expected)


# =============================================================================
# Index View Tests
# =============================================================================

class IndexViewTests(TestCase):
    """Tests for the index / landing page view."""

    def test_index_returns_200(self):
        """The index URL returns HTTP 200."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        """The index view uses the index.html template."""
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_index_contains_catalogo_link(self):
        """The index page includes a link to the catalog view."""
        response = self.client.get(reverse("index"))
        self.assertContains(response, reverse("catalogo"))


# =============================================================================
# Catalog View Tests
# =============================================================================

class CatalogoViewTests(TestCase):
    """Tests for the catalog gallery view — rendering, ordering, badges."""

    @classmethod
    def setUpTestData(cls):
        cls.boldo = Planta.objects.create(
            nombre_comun="Boldo",
            nombre_cientifico="Peumus boldus",
            familia_botanica="Monimiaceae",
            origen="NATIVA",
            zona_macro="CENTRO",
            regiones="Metropolitana",
            habitat="Bosques esclerófilos",
            descripcion_hoja="Hojas ovaladas",
            descripcion_tallo="Tronco corto",
            descripcion_flor="Flores pequeñas",
            foto_real="https://example.com/boldo.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Hepático",
            receta_preparacion="Infusión de hojas",
            advertencias="No en embarazo",
        )
        cls.matico = Planta.objects.create(
            nombre_comun="Matico",
            nombre_cientifico="Buddleja globosa",
            familia_botanica="Scrophulariaceae",
            origen="NATIVA",
            zona_macro="SUR",
            regiones="La Araucanía",
            habitat="Riberas",
            descripcion_hoja="Hojas lanceoladas",
            descripcion_tallo="Arbusto",
            descripcion_flor="Flores globosas",
            foto_real="https://example.com/matico.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Cicatrizante",
            receta_preparacion="Hervir las hojas",
            advertencias="Ninguna",
        )
        cls.llanten = Planta.objects.create(
            nombre_comun="Llanten",
            nombre_cientifico="Plantago major",
            familia_botanica="Plantaginaceae",
            origen="ASILVESTRADA",
            zona_macro="CENTRO",
            regiones="Todo Chile",
            habitat="Sitios húmedos",
            descripcion_hoja="Hojas anchas",
            descripcion_tallo="Sin tallo aparente",
            descripcion_flor="Espiga",
            foto_real="https://example.com/llanten.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Antiinflamatorio",
            receta_preparacion="Infusión",
            advertencias="Ninguna",
        )
        cls.ruda = Planta.objects.create(
            nombre_comun="Ruda",
            nombre_cientifico="Ruta graveolens",
            familia_botanica="Rutaceae",
            origen="ASILVESTRADA",
            zona_macro="NORTE",
            regiones="Atacama",
            habitat="Terrenos secos",
            descripcion_hoja="Hojas compuestas",
            descripcion_tallo="Tallo leñoso",
            descripcion_flor="Flores amarillas",
            foto_real="https://example.com/ruda.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Digestivo",
            receta_preparacion="Infusión",
            advertencias="Tóxica en exceso",
        )

    def test_catalogo_returns_200(self):
        """The catalogo URL returns HTTP 200."""
        response = self.client.get(reverse("catalogo"))
        self.assertEqual(response.status_code, 200)

    def test_catalogo_uses_correct_template(self):
        """The catalogo view uses catalogo.html."""
        response = self.client.get(reverse("catalogo"))
        self.assertTemplateUsed(response, "catalogo.html")

    def test_catalogo_shows_all_plants_ordered(self):
        """All plants are displayed ordered alphabetically by nombre_comun."""
        response = self.client.get(reverse("catalogo"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Boldo")
        self.assertContains(response, "Llanten")
        self.assertContains(response, "Matico")
        self.assertContains(response, "Ruda")
        # Verify alphabetical order: Boldo < Llanten < Matico < Ruda
        content = response.content.decode()
        boldo_pos = content.index("Boldo")
        llanten_pos = content.index("Llanten")
        matico_pos = content.index("Matico")
        ruda_pos = content.index("Ruda")
        self.assertLess(boldo_pos, llanten_pos)
        self.assertLess(llanten_pos, matico_pos)
        self.assertLess(matico_pos, ruda_pos)

    def test_catalogo_shows_origen_badges(self):
        """Nativa and Asilvestrada badges render correctly."""
        response = self.client.get(reverse("catalogo"))
        self.assertContains(response, "Nativa")
        self.assertContains(response, "Asilvestrada")

    def test_catalogo_shows_zona_badges(self):
        """Zona macro badges render for Norte, Centro, Sur."""
        response = self.client.get(reverse("catalogo"))
        self.assertContains(response, "Norte")
        self.assertContains(response, "Centro")
        self.assertContains(response, "Sur")

    def test_catalogo_shows_scientific_names(self):
        """Scientific names appear in catalog cards."""
        response = self.client.get(reverse("catalogo"))
        self.assertContains(response, "Peumus boldus")
        self.assertContains(response, "Buddleja globosa")

    def test_catalogo_shows_results_count(self):
        """The catalog shows the number of results found."""
        response = self.client.get(reverse("catalogo"))
        self.assertContains(response, "4 resultado encontrado")


# =============================================================================
# Catalog Filter Tests
# =============================================================================

class CatalogoFilterTests(TestCase):
    """Tests for catalog filter parameters (q, origen, zona, efecto)."""

    @classmethod
    def setUpTestData(cls):
        cls.boldo = Planta.objects.create(
            nombre_comun="Boldo",
            nombre_cientifico="Peumus boldus",
            familia_botanica="Monimiaceae",
            origen="NATIVA",
            zona_macro="CENTRO",
            regiones="Metropolitana",
            habitat="Bosques esclerófilos",
            descripcion_hoja="Hojas ovaladas",
            descripcion_tallo="Tronco corto",
            descripcion_flor="Flores pequeñas",
            foto_real="https://example.com/boldo.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Hepático",
            receta_preparacion="Infusión de hojas",
            advertencias="No en embarazo",
        )
        cls.matico = Planta.objects.create(
            nombre_comun="Matico",
            nombre_cientifico="Buddleja globosa",
            familia_botanica="Scrophulariaceae",
            origen="NATIVA",
            zona_macro="SUR",
            regiones="La Araucanía",
            habitat="Riberas",
            descripcion_hoja="Hojas lanceoladas",
            descripcion_tallo="Arbusto",
            descripcion_flor="Flores globosas",
            foto_real="https://example.com/matico.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Cicatrizante",
            receta_preparacion="Hervir las hojas",
            advertencias="Ninguna",
        )
        cls.llanten = Planta.objects.create(
            nombre_comun="Llanten",
            nombre_cientifico="Plantago major",
            familia_botanica="Plantaginaceae",
            origen="ASILVESTRADA",
            zona_macro="CENTRO",
            regiones="Todo Chile",
            habitat="Sitios húmedos",
            descripcion_hoja="Hojas anchas",
            descripcion_tallo="Sin tallo aparente",
            descripcion_flor="Espiga",
            foto_real="https://example.com/llanten.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Antiinflamatorio",
            receta_preparacion="Infusión",
            advertencias="Ninguna",
        )
        cls.ruda = Planta.objects.create(
            nombre_comun="Ruda",
            nombre_cientifico="Ruta graveolens",
            familia_botanica="Rutaceae",
            origen="ASILVESTRADA",
            zona_macro="NORTE",
            regiones="Atacama",
            habitat="Terrenos secos",
            descripcion_hoja="Hojas compuestas",
            descripcion_tallo="Tallo leñoso",
            descripcion_flor="Flores amarillas",
            foto_real="https://example.com/ruda.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Digestivo",
            receta_preparacion="Infusión",
            advertencias="Tóxica en exceso",
        )

    def test_text_search_by_common_name(self):
        """Filter q matches nombre_comun."""
        response = self.client.get(reverse("catalogo"), {"q": "boldo"})
        self.assertContains(response, "Boldo")
        self.assertNotContains(response, "Matico")
        self.assertNotContains(response, "Ruda")

    def test_text_search_by_scientific_name(self):
        """Filter q matches nombre_cientifico."""
        response = self.client.get(reverse("catalogo"), {"q": "Plantago"})
        self.assertContains(response, "Llanten")
        self.assertNotContains(response, "Boldo")

    def test_text_search_by_family(self):
        """Filter q matches familia_botanica."""
        response = self.client.get(reverse("catalogo"), {"q": "Rutaceae"})
        self.assertContains(response, "Ruda")
        self.assertNotContains(response, "Boldo")

    def test_text_search_case_insensitive(self):
        """Filter q is case-insensitive."""
        response = self.client.get(reverse("catalogo"), {"q": "BOLDO"})
        self.assertContains(response, "Boldo")

    def test_origen_filter_nativa(self):
        """Filter origen=NATIVA returns only native plants."""
        response = self.client.get(reverse("catalogo"), {"origen": "NATIVA"})
        self.assertContains(response, "Boldo")
        self.assertContains(response, "Matico")
        self.assertNotContains(response, "Llanten")
        self.assertNotContains(response, "Ruda")

    def test_origen_filter_asilvestrada(self):
        """Filter origen=ASILVESTRADA returns only naturalized plants."""
        response = self.client.get(reverse("catalogo"), {"origen": "ASILVESTRADA"})
        self.assertContains(response, "Llanten")
        self.assertContains(response, "Ruda")
        self.assertNotContains(response, "Boldo")
        self.assertNotContains(response, "Matico")

    def test_zona_filter_centro(self):
        """Filter zona=CENTRO returns plants from the Central zone."""
        response = self.client.get(reverse("catalogo"), {"zona": "CENTRO"})
        self.assertContains(response, "Boldo")
        self.assertContains(response, "Llanten")
        self.assertNotContains(response, "Matico")
        self.assertNotContains(response, "Ruda")

    def test_zona_filter_sur(self):
        """Filter zona=SUR returns plants from the Southern zone."""
        response = self.client.get(reverse("catalogo"), {"zona": "SUR"})
        self.assertContains(response, "Matico")
        self.assertNotContains(response, "Boldo")
        self.assertNotContains(response, "Llanten")

    def test_efecto_filter_exact(self):
        """Filter efecto matches efecto_terapeutico exactly."""
        response = self.client.get(reverse("catalogo"), {"efecto": "Hepático"})
        self.assertContains(response, "Boldo")
        self.assertNotContains(response, "Matico")
        self.assertNotContains(response, "Ruda")

    def test_efecto_filter_partial_match(self):
        """Filter efecto uses icontains so partial matches work."""
        response = self.client.get(reverse("catalogo"), {"efecto": "anti"})
        self.assertContains(response, "Llanten")  # Antiinflamatorio
        self.assertNotContains(response, "Boldo")  # Hepático

    def test_multiple_filters_combined(self):
        """Multiple filters combine with AND logic."""
        # ASILVESTRADA + CENTRO → only Llanten
        response = self.client.get(
            reverse("catalogo"),
            {"origen": "ASILVESTRADA", "zona": "CENTRO"},
        )
        self.assertContains(response, "Llanten")
        self.assertNotContains(response, "Boldo")  # NATIVA, not ASILVESTRADA
        self.assertNotContains(response, "Ruda")   # ASILVESTRADA but NORTE, not CENTRO

    def test_empty_filters_return_all_plants(self):
        """No filter parameters returns all plants unordered."""
        response = self.client.get(reverse("catalogo"), {})
        self.assertEqual(len(response.context["plantas"]), 4)

    def test_filter_no_results_shows_message(self):
        """A filter matching no plants shows the 'Sin resultados' message."""
        response = self.client.get(reverse("catalogo"), {"q": "xyzzy_nonexistent"})
        self.assertContains(response, "Sin resultados")
        self.assertContains(response, "limpia los filtros")

    def test_filter_active_count_badge(self):
        """The active filter count badge appears when filters are used."""
        response = self.client.get(
            reverse("catalogo"), {"origen": "NATIVA", "zona": "CENTRO"}
        )
        self.assertContains(response, "2 filtros activos")


class CatalogoEmptyViewTests(TestCase):
    """Tests for the catalog when the database has no plants."""

    def test_empty_database_shows_construction_message(self):
        """With no plants and no filters, shows 'Catálogo en construcción'."""
        self.assertEqual(Planta.objects.count(), 0)
        response = self.client.get(reverse("catalogo"))
        self.assertContains(response, "Catálogo en construcción")
        self.assertContains(response, "Catálogo de Plantas")


# =============================================================================
# Detail View Tests
# =============================================================================

class DetallePlantaViewTests(TestCase):
    """Tests for the plant detail / ficha técnica view."""

    @classmethod
    def setUpTestData(cls):
        cls.plant = Planta.objects.create(
            nombre_comun="Boldo",
            nombre_cientifico="Peumus boldus",
            familia_botanica="Monimiaceae",
            origen="NATIVA",
            zona_macro="CENTRO",
            regiones="Metropolitana",
            habitat="Bosques esclerófilos",
            descripcion_hoja="Hojas ovaladas",
            descripcion_tallo="Tronco corto",
            descripcion_flor="Flores pequeñas",
            foto_real="https://example.com/boldo.jpg",
            uso_principal="Medicinal",
            efecto_terapeutico="Hepático",
            receta_preparacion="Infusión de hojas",
            advertencias="No en embarazo",
        )

    def test_detalle_planta_valid_id_returns_200(self):
        """Valid plant ID returns 200 with the correct template."""
        response = self.client.get(reverse("detalle_planta", args=[self.plant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "detalle_planta.html")

    def test_detalle_planta_shows_plant_data(self):
        """Detail page displays the plant's key information."""
        response = self.client.get(reverse("detalle_planta", args=[self.plant.id]))
        self.assertContains(response, "Boldo")
        self.assertContains(response, "Peumus boldus")
        self.assertContains(response, "Monimiaceae")
        self.assertContains(response, "Nativa de Chile")
        self.assertContains(response, "Hepático")
        self.assertContains(response, "Infusión de hojas")
        self.assertContains(response, "No en embarazo")

    def test_detalle_planta_invalid_id_returns_404(self):
        """Invalid (non-existent) plant ID returns 404."""
        invalid_id = 99999
        response = self.client.get(reverse("detalle_planta", args=[invalid_id]))
        self.assertEqual(response.status_code, 404)


# =============================================================================
# Authentication Tests — Register
# =============================================================================

class RegisterViewTests(TestCase):
    """Tests for the user registration view."""

    def test_register_get_renders_form(self):
        """GET request renders the registration form."""
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
        self.assertContains(response, "Crear Cuenta")

    @override_settings(AUTH_PASSWORD_VALIDATORS=[])
    def test_register_post_creates_user_and_redirects(self):
        """POST with valid data creates a user and redirects to index."""
        data = {
            "username": "newuser",
            "password1": "testpass123",
            "password2": "testpass123",
        }
        response = self.client.post(reverse("register"), data)
        self.assertRedirects(response, reverse("index"))
        self.assertTrue(User.objects.filter(username="newuser").exists())

    @override_settings(AUTH_PASSWORD_VALIDATORS=[])
    def test_register_auto_login(self):
        """After successful registration, the new user is logged in."""
        data = {
            "username": "autologinuser",
            "password1": "testpass123",
            "password2": "testpass123",
        }
        response = self.client.post(reverse("register"), data, follow=True)
        self.assertTrue(response.context["user"].is_authenticated)

    def test_register_duplicate_username_fails(self):
        """POST with an existing username re-renders the form with errors."""
        User.objects.create_user(username="existinguser", password="Password123!")
        data = {
            "username": "existinguser",
            "password1": "Password123!",
            "password2": "Password123!",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
        self.assertIn("form", response.context)
        self.assertTrue(response.context["form"].errors)

    def test_register_password_mismatch_fails(self):
        """POST with mismatched passwords re-renders the form with errors."""
        data = {
            "username": "anotheruser",
            "password1": "Password123!",
            "password2": "DifferentPass456!",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
        self.assertIn("form", response.context)
        self.assertTrue(response.context["form"].errors)


# =============================================================================
# Authentication Tests — Login
# =============================================================================

class LoginViewTests(TestCase):
    """Tests for the login view (django.contrib.auth.urls)."""

    def test_login_renders_correctly(self):
        """Login page renders successfully with the login template."""
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        self.assertContains(response, "Iniciar Sesión")


# =============================================================================
# Authentication Tests — Profile
# =============================================================================

class ProfileViewTests(TestCase):
    """Tests for the user profile view (@login_required)."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="TestPass123!"
        )

    def test_profile_requires_login_redirects(self):
        """Unauthenticated access to profile redirects to the login page."""
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_profile_works_when_authenticated(self):
        """Authenticated user can access their profile page."""
        self.client.login(username="testuser", password="TestPass123!")
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/profile.html")
        self.assertContains(response, "testuser")
        self.assertContains(response, "Mi Perfil")
