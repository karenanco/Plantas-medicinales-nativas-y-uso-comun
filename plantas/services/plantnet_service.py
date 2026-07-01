"""
Pl@ntNet API integration service.

Provides a function to send plant images to the Pl@ntNet v2 API
and retrieve identification results (scientific name, common names, score).
"""

import logging
from typing import Any, Optional

import requests
from django.conf import settings

logger = logging.getLogger(__name__)

PLANTNET_API_URL: str = "https://my-api.plantnet.org/v2/identify/all"
REQUEST_TIMEOUT: int = 30  # seconds


class PlantNetError(Exception):
    """Custom exception for Pl@ntNet API errors."""


def _mock_plantnet_response() -> dict:
    """
    Return mock identification results for demonstration in DEBUG mode.

    Uses realistic Chilean medicinal plant data so the UI can be tested
    without a live API key.
    """
    return {
        "results": [
            {
                "score": 0.942,
                "species": {
                    "scientificName": "Peumus boldus",
                    "commonNames": ["Boldo", "Boldo chileno"],
                    "family": {
                        "scientificName": "Monimiaceae",
                    },
                },
            },
            {
                "score": 0.035,
                "species": {
                    "scientificName": "Litsea glabrata",
                    "commonNames": ["Añil", "Laurel"],
                    "family": {
                        "scientificName": "Lauraceae",
                    },
                },
            },
            {
                "score": 0.011,
                "species": {
                    "scientificName": "Cryptocarya alba",
                    "commonNames": ["Peumo", "Peumo macho"],
                    "family": {
                        "scientificName": "Lauraceae",
                    },
                },
            },
            {
                "score": 0.007,
                "species": {
                    "scientificName": "Ugni molinae",
                    "commonNames": ["Murtilla", "Uñi", "Murta"],
                    "family": {
                        "scientificName": "Myrtaceae",
                    },
                },
            },
        ],
    }


def identificar_planta(
    imagen_bytes: bytes,
    organs: Optional[list[str]] = None,
) -> dict[str, Any]:
    """
    Send an image to the Pl@ntNet API v2 for plant identification.

    Args:
        imagen_bytes: Raw bytes of the image to identify.
        organs: Optional list of organs present in the image
                (e.g. ``["leaf"]``, ``["flower"]``, ``["fruit"]``).
                When omitted the API auto-detects the organ.

    Returns:
        Parsed JSON response from the Pl@ntNet API containing a ``results``
        list with ``score`` and ``species`` information.

    Raises:
        PlantNetError: If the API key is missing, the request fails,
                       or the API returns an error.
    """
    api_key: str = settings.PLANTNET_API_KEY

    # --- No API key ------------------------------------------------
    if not api_key:
        if settings.DEBUG:
            logger.info("PLANTNET_API_KEY not set — returning mock results (DEBUG mode).")
            return _mock_plantnet_response()
        raise PlantNetError(
            "Pl@ntNet API key no configurada. "
            "Define la variable de entorno PLANTNET_API_KEY."
        )

    url: str = f"{PLANTNET_API_URL}?api-key={api_key}"

    # Build multipart request
    files: dict[str, tuple[str, bytes, str]] = {
        "images": ("image.jpg", imagen_bytes, "image/jpeg"),
    }
    data: dict[str, list[str]] = {}
    if organs:
        data["organs"] = organs

    try:
        logger.info("Sending request to Pl@ntNet API (size=%d bytes).", len(imagen_bytes))
        response = requests.post(
            url, files=files, data=data, timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()
        result: dict[str, Any] = response.json()
        logger.info(
            "Pl@ntNet API responded with %d results.",
            len(result.get("results", [])),
        )
        return result

    except requests.exceptions.Timeout as exc:
        logger.error("Pl@ntNet request timed out after %ds.", REQUEST_TIMEOUT)
        raise PlantNetError(
            "La solicitud a Pl@ntNet excedió el tiempo de espera. "
            "Intenta con una imagen más pequeña o vuelve a intentarlo."
        ) from exc

    except requests.exceptions.HTTPError as exc:
        status_code: int = exc.response.status_code if exc.response is not None else 0
        if status_code == 401:
            logger.error("Pl@ntNet returned 401 — invalid API key.")
            raise PlantNetError(
                "La API key de Pl@ntNet es inválida. "
                "Verifica la variable de entorno PLANTNET_API_KEY."
            ) from exc
        if status_code == 404:
            logger.error("Pl@ntNet returned 404 — endpoint not found.")
            raise PlantNetError(
                "El endpoint de Pl@ntNet no está disponible. "
                "Verifica la URL en la configuración."
            ) from exc
        detail: str = exc.response.text[:300] if exc.response is not None else ""
        logger.error("Pl@ntNet HTTP %d: %s", status_code, detail)
        raise PlantNetError(
            f"Error HTTP {status_code} al comunicarse con Pl@ntNet."
        ) from exc

    except requests.exceptions.RequestException as exc:
        logger.error("Pl@ntNet connection error: %s", exc)
        raise PlantNetError(
            "No se pudo conectar con el servicio de Pl@ntNet. "
            "Verifica tu conexión a internet."
        ) from exc
