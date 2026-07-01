"""
Views for the plantas application.

All views are function-based views (FBVs) as specified in the project
architecture requirements. Each view includes docstrings for clarity.
"""

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Favorito, Planta

from plantas.services.plantnet_service import PlantNetError, identificar_planta


def index(request):
    """
    Landing page view for FloraMed Chile.

    Renders the home page with hero section, project description,
    and call-to-action button linking to the catalog.
    """
    return render(request, "index.html")


def register(request):
    """
    User registration view.

    On GET: renders the registration form (UserCreationForm).
    On POST with valid data: creates the user, authenticates them,
    logs them in, and redirects to the homepage with a success message.
    On POST with invalid data: re-renders the form with validation errors.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-login after registration
            raw_password = form.cleaned_data.get("password1")
            authenticated_user = authenticate(
                username=user.username, password=raw_password
            )
            if authenticated_user is not None:
                login(request, authenticated_user)
            messages.success(
                request,
                f"¡Bienvenido, {user.username}! Tu cuenta ha sido creada exitosamente.",
            )
            return redirect("index")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    """
    User profile view (login required).

    Displays the authenticated user's account information:
    username, email, date joined, and last login.
    """
    return render(request, "registration/profile.html", {"profile_user": request.user})


def catalogo(request):
    """
    Catalog gallery view displaying all plants in a responsive grid.

    Supports filtering via GET parameters:
      - q       : text search across nombre_comun, nombre_cientifico,
                  familia_botanica (__icontains)
      - origen  : exact match on the origen field
      - zona    : exact match on the zona_macro field
      - efecto  : icontains search on the efecto_terapeutico field

    Passes the current filter values back to the template so the form
    can preserve selections. Handles empty queryset gracefully by
    rendering a friendly placeholder message.
    """
    # Read and strip filter parameters from the GET query string
    q: str = request.GET.get("q", "").strip()
    origen: str = request.GET.get("origen", "").strip()
    zona: str = request.GET.get("zona", "").strip()
    efecto: str = request.GET.get("efecto", "").strip()

    plantas = Planta.objects.all().order_by("nombre_comun")

    # Apply filters only when a non-empty value is provided
    if q:
        plantas = plantas.filter(
            Q(nombre_comun__icontains=q)
            | Q(nombre_cientifico__icontains=q)
            | Q(familia_botanica__icontains=q)
        )
    if origen:
        plantas = plantas.filter(origen=origen)
    if zona:
        plantas = plantas.filter(zona_macro=zona)
    if efecto:
        plantas = plantas.filter(efecto_terapeutico__icontains=efecto)

    # Count how many filters are active (for UI badge)
    active_filters: int = sum(1 for f in [q, origen, zona, efecto] if f)

    context: dict = {
        "plantas": plantas,
        "filter_q": q,
        "filter_origen": origen,
        "filter_zona": zona,
        "filter_efecto": efecto,
        "active_filters": active_filters,
    }
    return render(request, "catalogo.html", context)


def detalle_planta(request, planta_id: int):
    """
    Ficha Técnica detail view for a single plant.

    Retrieves the Planta object by primary key or returns a 404 response.
    Renders the full technical detail sheet with classification,
    geolocation, morphology, therapeutic uses, recipe, and warnings.
    """
    planta: Planta = get_object_or_404(Planta, pk=planta_id)
    return render(request, "detalle_planta.html", {"planta": planta})


@login_required
def identificar(request):
    """
    Plant identification view powered by the Pl@ntNet API.

    **GET** — Renders the image upload form.

    **POST** — Accepts an uploaded image, sends it to the Pl@ntNet API,
    and displays identification results (scientific name, common name,
    score). Handles the following error conditions gracefully:

    - No image file selected.
    - Uploaded file is not a valid image type.
    - Pl@ntNet API key not configured (shows mock data in DEBUG mode).
    - API request failure (timeout, auth error, network error).
    - API returns no results.
    """
    error: str | None = None
    resultados: dict | None = None
    api_key_set: bool = bool(settings.PLANTNET_API_KEY)

    MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB

    if request.method == "POST":
        if "imagen" not in request.FILES:
            error = "Debes seleccionar una imagen para identificar."
        else:
            imagen = request.FILES["imagen"]
            if not imagen.content_type.startswith("image/"):
                error = "El archivo seleccionado no es una imagen válida."
            elif imagen.size > MAX_IMAGE_SIZE:
                error = "La imagen excede el tamaño máximo permitido de 10 MB."
            else:
                try:
                    resultados = identificar_planta(imagen.read())
                    # Check if API returned results
                    if resultados and not resultados.get("results"):
                        error = (
                            "Pl@ntNet no pudo identificar la planta. "
                            "Prueba con otra imagen o desde otro ángulo."
                        )
                except PlantNetError as exc:
                    error = str(exc)

    return render(
        request,
        "identificar.html",
        {
            "resultados": resultados,
            "error": error,
            "api_key_set": api_key_set,
        },
    )


@login_required
def toggle_favorito(request, planta_id: int):
    """
    Toggle favorite status for a plant (login required).
    
    Adds the plant to user's favorites if not already added,
    removes it if it was already favorited. Redirects back to
    the plant detail page.
    """
    planta = get_object_or_404(Planta, pk=planta_id)
    favorito, created = Favorito.objects.get_or_create(
        usuario=request.user,
        planta=planta,
    )
    if not created:
        favorito.delete()
        messages.info(request, f"'{planta.nombre_comun}' eliminado de favoritos.")
    else:
        messages.success(request, f"'{planta.nombre_comun}' agregado a favoritos.")
    
    return redirect("detalle_planta", planta_id=planta_id)
