# Hoja de Ruta: Identificador Automatizado de Plantas por Imágenes

> **Nota:** Este documento describe funcionalidades planificadas para futuras
> fases del proyecto, una vez completado el ciclo actual de desarrollo.

---

## Visión General

Evolucionar FloraMed Chile hacia una plataforma inteligente de identificación
botánica, combinando modelos de machine learning entrenados con datos locales,
sistema de recomendación basado en síntomas y una experiencia mobile nativa.

---

## Fase 1: Entrenar modelo ML con imágenes de las 85 especies

**Objetivo:** Crear un modelo de clasificación de imágenes específico para la
flora medicinal chilena, utilizando las 85 especies del catálogo como clases.

### Actividades

- Recopilar dataset de imágenes para cada especie (mínimo 100 imágenes por clase)
  - Fuentes: iNaturalist, GBIF, herbarios digitales, contribuciones comunitarias
  - Aumento de datos: rotación, zoom, cambio de iluminación, recorte aleatorio
- Entrenar modelo de clasificación (transfer learning con EfficientNet o ResNet)
- Evaluar métricas: accuracy, precision, recall, F1-score por especie
- Exportar modelo a formato TensorFlow Lite o ONNX para inferencia eficiente

### Entregables

- Dataset etiquetado de imágenes de flora chilena
- Modelo entrenado con ≥ 85% de accuracy en validación
- Script de inferencia para integración con Django

---

## Fase 2: Integrar modelo ML como reemplazo/complemento de Pl@ntNet

**Objetivo:** Reemplazar o complementar la API de Pl@ntNet con el modelo propio,
reduciendo dependencias externas y mejorando la precisión para especies chilenas.

### Actividades

- Implementar endpoint de inferencia en Django (TensorFlow Serving o PyTorch Serve)
- Crear servicio de identificación híbrido:
  - Primera pasada: modelo local (rápido, sin costo)
  - Segunda pasada: Pl@ntNet como respaldo cuando la confianza es baja (< 70%)
- Almacenar resultados de identificaciones para mejora continua (active learning)
- Cache de resultados para imágenes similares (hashing perceptual)

### Entregables

- Endpoint `/api/identificar-local/` con inferencia del modelo propio
- Sistema híbrido de identificación con fallback a Pl@ntNet
- Dashboard de monitoreo de identificaciones

---

## Fase 3: Sistema de recomendación basado en síntomas

**Objetivo:** Permitir a las usuarias buscar plantas según síntomas o dolencias,
usando un motor de recomendación basado en propiedades terapéuticas.

### Actividades

- Modelar ontología de síntomas ↔ efectos terapéuticos ↔ plantas
- Implementar motor de búsqueda semántica (embedding de síntomas)
- Crear interfaz "¿Qué te duele?" con selector de síntomas comunes
- Sistema de pesos: múltiples síntomas producen ranking de plantas relevantes
- Filtro por contraindicaciones: evitar recomendar plantas con advertencias
  relevantes al perfil del usuario

### Entregables

- Página "Recomendación por síntoma" con interfaz visual
- API de recomendación REST
- Tabla de relaciones síntoma-planta con pesos

---

## Fase 4: Aplicación mobile con cámara en tiempo real

**Objetivo:** Desarrollar una app mobile (React Native o Flutter) que permita
identificar plantas en tiempo real usando la cámara del dispositivo.

### Actividades

- Desarrollo de app con cámara integrada y captura de imágenes
- Consumo de API de identificación (modelo propio + Pl@ntNet)
- Modo offline: caché de especies y modelo liviano en dispositivo
- Sincronización con la web: favoritos, historial de identificaciones
- Notificaciones push: temporada de floración, alertas de especies invasoras

### Entregables

- App para iOS y Android (Play Store + App Store)
- API GraphQL o REST para sincronización
- Documentación de la API pública

---

## Fase 5: Comunidad y contribuciones de usuarios

**Objetivo:** Crear una comunidad en torno al conocimiento herbolaria, donde
usuarias puedan contribuir con imágenes, observaciones y conocimiento local.

### Actividades

- Sistema de contribuciones: subir fotos de plantas con georreferenciación
- Validación comunitaria: votos y revisión de identificaciones por pares
- Foro o sección de discusión por especie
- Gamificación: insignias por contribuciones, rachas de identificaciones
- Mapa colaborativo de avistamientos (crowdsourcing)
- Integración con iNaturalist y GBIF para exportación de datos

### Entregables

- Perfil público de usuaria con historial de contribuciones
- Mapa interactivo de avistamientos
- API pública para acceso a datos contribuidos
- Estadísticas de la comunidad (dashboard)

---

## Resumen de Roadmap

| Fase | Descripción | Prioridad | Dependencias |
|------|-------------|-----------|--------------|
| 1 | Entrenar modelo ML con imágenes de 85 especies | Alta | Dataset de imágenes |
| 2 | Integrar modelo como reemplazo/complemento de Pl@ntNet | Alta | Fase 1 completada |
| 3 | Sistema de recomendación basado en síntomas | Media | Datos terapéuticos estructurados |
| 4 | App mobile con cámara en tiempo real | Media | Fase 2 completada |
| 5 | Comunidad y contribuciones de usuarios | Baja | Fase 4 completada, base de usuarios |

---

## Estado Actual

| Fase | Estado |
|------|--------|
| Identificación por imagen con Pl@ntNet API | ✅ Completado (integración actual) |
| Fase 1: Modelo ML propio | ⏳ Pendiente |
| Fase 2: Integración modelo propio | ⏳ Pendiente |
| Fase 3: Recomendación por síntomas | ⏳ Pendiente |
| Fase 4: App mobile | ⏳ Pendiente |
| Fase 5: Comunidad | ⏳ Pendiente |
