# Tasks

**Proyecto**: [[projects/FloraMed-Chile/README|FloraMed-Chile]]


- **Project Scaffolding & Django Configuration** [completed]: Crear proyecto Django 6.0 con estructura core/, plantas/, docs/. Configurar settings (SQLite, static, media, auth URLs), base template con Tailwind CSS via CDN, y requirements.txt
- **Planta Model Implementation** [completed]: Implementar modelo Planta en plantas/models.py con todos los campos especificados en el PRD: nombre_comun, nombre_cientifico, familia_botanica, origen, zona_macro, regiones, habitat, descripciones morfológicas, foto_real, uso_principal, efecto_terapeutico, receta_preparacion, advertencias. Incluir choices para ORIGEN y ZONA.
- **Seed Data for 85 Species** [completed]: Crear management command load_plantas.py o data migration para poblar la base de datos con las 85 especies listadas en el PRD (Sección 6). Incluir datos completos: nombre común, científico, familia, origen, zona, regiones, hábitat, descripciones morfológicas, usos, recetas, advertencias.
- **Authentication System** [completed]: Implementar registro, inicio de sesión y cierre de sesión usando el modelo User nativo de Django. Crear templates con Tailwind para login, registro y logout. Proteger vistas de administración con @login_required.
- **Catalog Gallery View (Listado)** [completed]: Crear vista basada en función (FBV) para listar todas las plantas en grilla responsiva con Tailwind. Mostrar nombre común, nombre científico, foto, origen y zona. Incluir template con diseño Sage & Clay palette.
- **Filters & Search** [completed]: Implementar filtros dinámicos en tiempo real por origen (Nativa/Asilvestrada), zona macro (Norte/Centro/Sur/Patagonia), efecto terapéutico, y búsqueda textual por nombre. Usar GET parameters y QuerySet filtering.
- **Plant Detail View (Ficha Técnica)** [completed]: Crear FBV de detalle para cada planta mostrando toda la información: descripciones morfológicas, hábitat, usos, receta de preparación, advertencias. Incluir botón 'Copiar Receta' al portapapeles con JavaScript. Template con diseño Sage & Clay.
- **Pl@ntNet API Integration** [completed]: Implementar integración básica con API de Pl@ntNet (https://my.plantnet.org/) para contraste de imágenes. Crear vista para subir/buscar imagen y mostrar resultados de identificación. Usar variables de entorno para API key.
- **Documentation** [completed]: Crear docs/progreso.md (bitácora de desarrollo) y docs/futuras_impl.md (hoja de ruta para identificador de plantas por imágenes). Actualizar README.md con instrucciones de instalación y uso.
- **Testing** [completed]: Escribir tests unitarios con TestCase de Django para: modelo Planta (creación, validación), vistas (status codes, context), autenticación (registro, login, logout), filtros (búsqueda por texto y campos).
- **Git Commit & Push** [completed]: Realizar commit con todos los cambios de FloraMed y push al repositorio remoto. Mensaje de commit con task-id incluido.