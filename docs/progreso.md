# Progreso del Proyecto — FloraMed Chile

## Hito 1: Scaffolding y Configuración Inicial (Completado)

- [x] Instalación de Django 6.0
- [x] Creación del proyecto `core`
- [x] Creación de la aplicación `plantas`
- [x] Configuración de `core/settings.py`:
  - `plantas` en `INSTALLED_APPS`
  - SQLite como base de datos
  - `STATIC_URL`, `MEDIA_URL` y `MEDIA_ROOT`
  - `LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL`
  - `TEMPLATES.DIRS` apuntando a `plantas/templates/`
  - Variables de entorno vía `os.environ` para `SECRET_KEY`, `DEBUG`, `PLANTNET_API_KEY`
  - Idioma español chileno (`es-cl`) y zona horaria `America/Santiago`
- [x] Configuración de `core/urls.py` con inclusión de `plantas.urls` y `auth.urls`
- [x] Creación de `plantas/urls.py` con enrutamiento inicial
- [x] Creación de vista `index` basada en función (FBV)
- [x] Template base `base.html` con:
  - Tailwind CSS vía CDN
  - Google Fonts (Playfair Display + JetBrains Mono)
  - Paleta Sage & Clay (verde salvia/terracota)
  - Barra de navegación responsiva con menú móvil
  - Footer informativo
- [x] Template `index.html` con sección Hero, tarjetas informativas y CTA
- [x] Template `registration/login.html` para autenticación
- [x] Creación de `requirements.txt`
- [x] Migraciones iniciales aplicadas
- [x] Directorios `docs/`, `static/`, `media/` creados

---

## Hito 2: Modelos, Seed Data y Autenticación (Completado)

- [x] Definición del modelo `Planta` con campos:
  - Clasificación: nombre común, científico, familia botánica, origen (NATIVA/ASILVESTRADA)
  - Geolocalización: zona macro (NORTE/CENTRO/SUR/PATAGONIA), regiones, hábitat
  - Morfología: descripción de hoja, tallo, flor
  - Uso terapéutico: uso principal, efecto terapéutico, receta, advertencias
  - Imagen referencial: `foto_real` (URL)
- [x] Definición del modelo `Favorito` (relación usuario-planta con unique_together)
- [x] Registro de modelos en `admin.py` con `list_display`, `list_filter`, `search_fields`
- [x] Seed data completa con 85 especies en `plantas/data/plantas_data.py`
- [x] Comando `load_plantas` con flag `--force` para recarga
- [x] Sistema de autenticación completo:
  - Registro de usuarios con auto-login post-registro
  - Inicio/cierre de sesión (vía `django.contrib.auth.urls`)
  - Vista de perfil protegida (`@login_required`)
  - Mensajes flash de éxito en registro
- [x] Templates de autenticación:
  - `registration/register.html`
  - `registration/login.html`
  - `registration/profile.html`

---

## Hito 3: Catálogo, Filtros y Fichas Técnicas (Completado)

- [x] Vista `catalogo` con filtros combinados vía GET:
  - `q`: búsqueda textual por nombre común, científico o familia
  - `origen`: nativa / asilvestrada
  - `zona`: norte, centro, sur, patagonia
  - `efecto`: efecto terapéutico (icontains)
- [x] Template `catalogo.html` con:
  - Panel de filtros con selects y búsqueda
  - Cuadrícula responsiva de tarjetas
  - Badges de origen y zona macro con colores distintivos
  - Placeholder SVG para imágenes faltantes
  - Contador de resultados y filtros activos
  - Estado vacío con mensaje amigable
  - Manejo de error en carga de imágenes (`onerror` → fallback SVG)
- [x] Vista `detalle_planta` con ficha técnica completa
- [x] Template `detalle_planta.html` con:
  - Encabezado con nombre común y científico
  - Tarjetas de clasificación, geolocalización, morfología
  - Sección de usos terapéuticos con badge de efecto
  - Receta de preparación con botón **"Copiar Receta"** (clipboard API)
  - Advertencias y precauciones (destacado en ámbar)
  - Botón "Agregar a Favoritos" (solo usuarios autenticados)

---

## Hito 4: Identificación por Imagen (Pl@ntNet) (Completado)

- [x] Servicio `plantas/services/plantnet_service.py`:
  - Función `identificar_planta()` con request multipart a Pl@ntNet v2
  - Manejo de errores: timeout, HTTP 401, 404, errores de red
  - Mock de datos de demostración cuando no hay API key en DEBUG
  - Logging estructurado
  - Excepción personalizada `PlantNetError`
- [x] Vista `identificar` con:
  - Validación de tipo de archivo (solo imágenes)
  - Mensajes de error específicos por cada tipo de fallo
  - Indicador visual de API configurada/no configurada
- [x] Template `identificar.html` con:
  - Dropzone drag & drop con vista previa
  - Indicador de carga (spinner) durante la identificación
  - Resultados con score, nombre científico, nombres comunes
  - Badge "MEJOR MATCH" para la coincidencia principal
  - Barra de progreso por coincidencia
  - Enlace "Buscar en catálogo" por cada resultado
  - Estados vacío y de error

---

## Hito 5: Tests Unitarios (Completado)

- [x] Tests para vista `index`:
  - Verifica código 200
  - Verifica template usado
  - Verifica enlace al catálogo
- [x] Tests para vista `catalogo`:
  - Verifica código 200 por URL y por nombre
  - Verifica template usado
  - Verifica renderizado con queryset vacío
  - Verifica orden alfabético de especies
  - Verifica renderizado de badges de origen y zona
  - Verifica estado vacío con mensaje "Catálogo en construcción"
- [x] Tests ejecutándose correctamente con `python manage.py test plantas`

---

## Hito 6: Documentación y Cierre de Ciclo (Completado — Julio 2026)

- [x] README.md completo con:
  - Descripción del proyecto, stack, características
  - Instrucciones de instalación y configuración
  - Estructura del proyecto
  - Guía de uso y despliegue en Render
- [x] `docs/progreso.md` actualizado con todos los hitos
- [x] `docs/futuras_impl.md` con hoja de ruta actualizada
- [x] Sincronización con Obsidian vault

---

## Decisiones Técnicas (ADRs)

### FBV sobre CBV
Todas las vistas son Function-Based Views (FBVs) por simplicidad y facilidad de
lectura, alineado con el alcance del proyecto.

### SQLite en desarrollo
Se utiliza SQLite como base de datos embebida para facilitar la configuración
local. En producción puede migrarse a PostgreSQL sin cambios significativos en
el modelo.

### Tailwind CDN (sin build step)
Tailwind se carga vía CDN para evitar la configuración de Node.js y build tools.
Adecuado para el alcance del proyecto; para producción puede reemplazarse con
Tailwind compilado.

### Pl@ntNet API v2
Se usa la API `v2/identify/all` que permite identificar cualquier órgano de la
planta (hoja, flor, fruto, corteza). La imagen se envía como multipart/form-data
con un timeout de 30 segundos.

### Variables de entorno con os.environ
Se usa `os.environ.get()` directamente (no `python-decouple`) para mantener
cero dependencias adicionales. `python-decouple` está en requirements.txt como
alternativa opcional.

### Paleta Sage & Clay
Esquema de colores basado en verde salvia (emerald) y terracota (amber/stone)
que evoca la conexión con la tierra y la naturaleza chilena.

### Playfair Display + JetBrains Mono
Combinación tipográfica: serif científica para títulos (legibilidad y elegancia)
y monospace técnica para datos taxonómicos (precisión y contraste).
