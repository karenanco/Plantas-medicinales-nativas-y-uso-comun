# 🌿 FloraMed Chile

**Catálogo de Plantas Medicinales Nativas y de Uso Común en Chile**

[![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite)](https://www.sqlite.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?logo=tailwindcss)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/Licencia-MIT-green)](LICENSE)

FloraMed Chile es una plataforma web que cataloga y divulga el conocimiento
tradicional de las plantas medicinales chilenas. Ofrece fichas técnicas
detalladas, identificación por imagen mediante la API de Pl@ntNet, filtros
inteligentes de búsqueda y geolocalización de especies por zona macro del país.

---

## 📸 Capturas de pantalla

> *(Agregar capturas de pantalla aquí)*
>
> | Vista | Descripción |
> |-------|-------------|
> | Inicio | Landing page con hero y presentación del proyecto |
> | Catálogo | Galería de plantas con filtros |
> | Ficha técnica | Detalle completo con receta y copia |
> | Identificador | Subida de imagen y resultados de Pl@ntNet |
> | Autenticación | Registro, inicio de sesión y perfil |

---

## ✨ Características

| Funcionalidad | Descripción |
|---------------|-------------|
| **🌱 Catálogo botánico** | Galería responsiva con las 85 especies de plantas medicinales chilenas |
| **📍 Geolocalización** | Clasificación por macrozonas (Norte, Centro, Sur, Patagonia) y regiones |
| **🔍 Filtros inteligentes** | Búsqueda por texto, origen (nativa/asilvestrada), zona macro y efecto terapéutico |
| **📋 Fichas técnicas** | Información detallada con clasificación, morfología, usos, receta y advertencias. Botón **Copiar Receta** |
| **📷 Identificación por imagen** | Integración con API Pl@ntNet para identificar plantas desde una foto |
| **🔐 Autenticación** | Registro de usuarios, inicio/cierre de sesión y perfil personal |
| **⭐ Favoritos** | Usuarios autenticados pueden guardar plantas favoritas (modelo implementado) |

---

## 🛠️ Stack tecnológico

| Tecnología | Versión | Uso |
|------------|---------|-----|
| [Django](https://www.djangoproject.com/) | 6.0 | Framework web Python |
| [SQLite](https://www.sqlite.org/) | — | Base de datos embebida (desarrollo) |
| [Tailwind CSS](https://tailwindcss.com/) | CDN | Estilos y diseño responsivo |
| [Pl@ntNet API](https://my.plantnet.org/) | v2 | Identificación de plantas por imagen |
| [Google Fonts](https://fonts.google.com/) | — | Playfair Display + JetBrains Mono |

---

## 🚀 Instalación

### Requisitos previos

- Python 3.11 o superior
- pip
- git

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/Plantas-medicinales-nativas-y-uso-comun.git
cd Plantas-medicinales-nativas-y-uso-comun

# 2. (Opcional) Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar migraciones
python manage.py migrate

# 5. Cargar datos de las 85 especies
python manage.py load_plantas

# 6. (Opcional) Crear superusuario para el admin
python manage.py createsuperuser

# 7. Iniciar servidor de desarrollo
python manage.py runserver
```

Abrir [http://localhost:8000](http://localhost:8000) en el navegador.

---

## 🔧 Configuración

### Variables de entorno

| Variable | Valor por defecto | Descripción |
|----------|-------------------|-------------|
| `DJANGO_SECRET_KEY` | *(clave insegura)* | Clave secreta de Django. **Cambiar en producción** |
| `DJANGO_DEBUG` | `True` | Modo debug (`True`/`False`) |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Hosts permitidos separados por coma |
| `PLANTNET_API_KEY` | *(vacío)* | API Key de Pl@ntNet (opcional en desarrollo) |

> **Nota:** Sin `PLANTNET_API_KEY` y con `DEBUG=True`, la identificación usa datos
> mock de demostración. Con `DEBUG=False`, muestra un error informativo.

Puedes crear un archivo `.env` en la raíz del proyecto:

```bash
DJANGO_SECRET_KEY=tu-clave-secreta
DJANGO_DEBUG=True
PLANTNET_API_KEY=tu-api-key-plantnet
```

> El proyecto utiliza `os.environ` para leer variables, no `python-decouple`
> (aunque `python-decouple` está disponible en `requirements.txt`).

---

## 🗂️ Estructura del proyecto

```
Plantas-medicinales-nativas-y-uso-comun/
├── core/                       # Configuración del proyecto Django
│   ├── settings.py             # Configuración global
│   ├── urls.py                 # URLs raíz
│   ├── wsgi.py                 # WSGI para producción
│   └── asgi.py                 # ASGI (futuro)
├── plantas/                    # Aplicación principal
│   ├── models.py               # Modelos Planta y Favorito
│   ├── views.py                # Vistas basadas en función (FBV)
│   ├── urls.py                 # URLs de la aplicación
│   ├── admin.py                # Configuración del admin
│   ├── tests.py                # Tests unitarios
│   ├── services/
│   │   └── plantnet_service.py # Integración con API Pl@ntNet
│   ├── data/
│   │   └── plantas_data.py     # Seed data con 85 especies
│   ├── management/commands/
│   │   ├── load_plantas.py     # Comando para cargar datos
│   │   └── seed_data.py        # Seed adicional (preliminar)
│   └── templates/
│       ├── base.html           # Template base con Tailwind
│       ├── index.html          # Landing page
│       ├── catalogo.html       # Galería con filtros
│       ├── detalle_planta.html # Ficha técnica
│       ├── identificar.html    # Identificador Pl@ntNet
│       └── registration/       # Templates de auth
│           ├── login.html
│           ├── register.html
│           └── profile.html
├── static/                     # Archivos estáticos
├── media/                      # Archivos subidos por usuarios
├── docs/                       # Documentación
│   ├── progreso.md             # Registro de progreso
│   └── futuras_impl.md         # Hoja de ruta futura
├── vault/                      # Obsidian vault (sincronizado)
├── lemoria/                    # Configuración Lemoria (agentes)
├── requirements.txt            # Dependencias Python
├── manage.py                   # CLI de Django
└── README.md                   # Este archivo
```

---

## 🧪 Tests

```bash
python manage.py test plantas
```

Cobertura actual:
- Vista índice (carga, template, enlace al catálogo)
- Vista catálogo (carga, template, orden alfabético, badges, estado vacío, filtros)
- Modelo Planta (implícito en tests de vistas)

---

## 📖 Uso

### Navegación principal

1. **Inicio** — Landing page con descripción del proyecto y enlaces
2. **Catálogo** — Explora las 85 especies con filtros por texto, origen, zona y efecto
3. **Identificar** — Sube una foto para identificar una planta vía Pl@ntNet
4. **Registro/Login** — Crea una cuenta para guardar favoritos

### Filtros del catálogo

El catálogo soporta filtros combinados vía GET:
- `q` — Búsqueda textual por nombre común, científico o familia
- `origen` — `NATIVA` o `ASILVESTRADA`
- `zona` — `NORTE`, `CENTRO`, `SUR`, `PATAGONIA`
- `efecto` — Efecto terapéutico (Digestivo, Hepático, Cicatrizante, etc.)

### Copia de receta

En cada ficha técnica, el botón **"Copiar Receta"** copia la receta de
preparación al portapapeles con un clic.

---

## ☁️ Despliegue en Render

### Opción 1: Desde GitHub (recomendada)

1. Conectar repositorio a [Render](https://render.com/)
2. Crear un **Web Service**
3. Configurar:
   - **Runtime:** Python 3.11
   - **Build Command:** `pip install -r requirements.txt && python manage.py migrate && python manage.py load_plantas`
   - **Start Command:** `gunicorn core.wsgi:application --bind 0.0.0.0:$PORT`
4. Agregar variables de entorno en Render Dashboard:
   - `DJANGO_SECRET_KEY` — Generar una clave segura
   - `DJANGO_DEBUG` = `False`
   - `DJANGO_ALLOWED_HOSTS` = `tudominio.onrender.com`
   - `PLANTNET_API_KEY` — (opcional)

### Opción 2: Manual (Docker)

Si prefieres Docker, crea un `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py migrate && python manage.py load_plantas
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
```

> **Importante:** En producción, Render asigna el puerto vía `$PORT`.
> Asegúrate de que `ALLOWED_HOSTS` incluya el dominio de Render.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -m 'feat: agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📄 Licencia

MIT © 2026 FloraMed Chile

---

## 🙏 Agradecimientos

- [Pl@ntNet](https://plantnet.org/) — API de identificación de plantas
- [Django](https://www.djangoproject.com/) — Framework web
- [Tailwind CSS](https://tailwindcss.com/) — Estilos utilitarios
- A las comunidades indígenas y tradicionales que preservan el conocimiento herbolaria chileno
