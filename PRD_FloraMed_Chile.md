# Documento de Requisitos del Producto (PRD)
## Proyecto: FloraMed Chile (Visualizador de Plantas Medicinales y Nativas)

---

## 1. Visión General del Proyecto
**FloraMed Chile** es una plataforma web interactiva diseñada para la catalogación, visualización y filtrado de plantas medicinales nativas y de uso habitual en Chile, organizadas por región geográfica y ubicación. El sistema proporciona fichas técnicas detalladas orientadas a la correcta identificación botánica y al rescate del conocimiento tradicional terapéutico. 

Este proyecto establece las bases estructurales, lógicas y de datos necesarias para una futura fase de desarrollo que implementará un **identificador automatizado de plantas basado en imágenes**.

### Objetivos Clave:
* Documentar y geolocalizar el uso tradicional de la flora herbolaria chilena.
* Proporcionar herramientas visuales y descriptivas morfológicas para evitar confusiones botánicas.
* Integrar capacidades de consulta externa mediante la API de **Pl@ntNet**.

---

## 2. Características Clave de la Aplicación

* **Catálogo Botánico Completo:** Inclusión inicial indexada de las especies requeridas, detallando: nombre popular, nombre científico, familia botánica, origen (nativa/asilvestrada de uso tradicional habitual) e imágenes de alta definición.
* **Geolocalización y Hábitat Detallado:** Clasificación macro-geográfica (Norte, Centro, Sur o Patagonia), regiones político-administrativas exactas y descripción de su ecosistema y hábitat natural.
* **Galería de Plantas Integral:** Interfaz responsiva en formato de grilla interactiva fluida adaptada tanto para computadoras como para dispositivos móviles.
* **Filtros Inteligentes en Tiempo Real:** Búsqueda textual y filtrado dinámico cruzado por origen biológico, región o usos/efectos terapéuticos específicos (ej. hepático, cicatrizante, ansiolítico, etc.).
* **Ficha Técnica Interactiva con Copia de Recetas:** Despliegue de beneficios, advertencias/precauciones y método de preparación tradicional, con un botón o acción directa para copiar esta receta completa al portapapeles.
* **Aesthetic Pairings (Identidad Visual):** Diseño limpio con paleta de colores orgánicos (*Sage & Clay*), usando fuentes tipográficas serifadas elegantes para el rigor científico de los nombres científicos y fuentes de espaciado uniforme (monospace) para datos técnicos y regiones.

---

## 3. Arquitectura Técnica y Stack

* **Framework Principal:** Django 6.0
* **Base de Datos:** SQLite (Entorno autocontenido, sin dependencias de PostgreSQL).
* **Autenticación:** Sistema nativo de Django (`User` model) gestionando flujos completos de Register, Login y Logout.
* **Frontend:** Django Templates integrados con **Tailwind CSS vía CDN** para agilidad de desarrollo.
* **Lógica de Vistas:** Vistas Basadas en Funciones (FBVs) exclusivamente, debidamente comentadas y documentadas (models, views, urls).
* **Integración Externa:** Conexión hacia la API de **Pl@ntNet** (`https://my.plantnet.org/`) para habilitar soporte complementario de identificación y contraste de imágenes reales.
* **Infraestructura de Despliegue:** Plataforma PaaS **Render** (configurada para Django + SQLite persistente mediante *Render Disks* o recreación de base de datos semilla).

---

## 4. Estructura del Proyecto y Documentación

El repositorio mantendrá el siguiente árbol de directorios mandatorio:

```text
├── core/                  # Configuración principal de Django
├── plantas/               # Aplicación del catálogo botánico
│   ├── templates/         # Vistas HTML con Tailwind CSS CDN
│   ├── models.py          # Definición de Base de Datos
│   ├── views.py           # Vistas basadas en funciones (FBVs)
│   └── urls.py            # Enrutamiento de la app
├── docs/                  # CARPETA REQUERIDA DE SEGUIMIENTO
│   ├── progreso.md        # Bitácora de desarrollo e hitos alcanzados
│   └── futuras_impl.md    # Hoja de ruta para el Identificador de Plantas
├── manage.py
└── requirements.txt
```

---

## 5. Modelamiento de Datos (Estructura de Base de Datos)

El archivo `plantas/models.py` estructurará la persistencia bajo el siguiente esquema lógico simplificado para SQLite:

```python
from django.db import models
from django.contrib.auth.models import User

class Planta(models.Model):
    ORIGEN_CHOICES = [
        ('NATIVA', 'Nativa de Chile'),
        ('ASILVESTRADA', 'Asilvestrada de Uso Tradicional'),
    ]
    
    ZONA_CHOICES = [
        ('NORTE', 'Norte'),
        ('CENTRO', 'Centro'),
        ('SUR', 'Sur'),
        ('PATAGONIA', 'Patagonia'),
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
    uso_principal = models.CharField(max_length=100, help_text="Ej: Medicinal, Comestible, Venenosa")
    efecto_terapeutico = models.CharField(max_length=150, help_text="Ej: Hepático, cicatrizante, ansiolítico")
    receta_preparacion = models.TextField()
    advertencias = models.TextField()

    def __str__(self):
        return f"{self.nombre_comun} ({self.nombre_cientifico})"
```

---

## 6. Listado Oficial de Especies a Indexar

El sistema precargará obligatoriamente los registros de la herbolaria chilena detallados en los requisitos:

1. **Ajenjo** (*Artemisia absinthium*)
2. **Ajo** (*Allium sativum*)
3. **Arrayan** (*Luma apiculata*)
4. **Bailahuen** (*Haplopappus spp.*) 
5. **Boldo** (*Peumus boldus*) 
6. **Borraja** (*Borago officinalis*)
7. **Cabello de ángel** (*Cuscuta chilensis*) 
8. **Cachanlagua** (*Centarium cachanlahuen*)
9. **Canelo** (*Drimys winteri*) 
10. **Cebolla** (*Allium cepa*)
11. **Cedron** (*Aloysia citrodora*)
12. **Cepa caballo, Amores secos** (*Acaena splendens*)
13. **Coca** (*Erythroxylum coca*)
14. **Culen** (*Psoralea glandulosa* / *Otholobium glandulosum*)
15. **Chachacoma** (*Senecio eriophyton*)
16. **Chequén** (*Luma chequen*)
17. **Chépica** (*Paspalum vaginatum*)
18. **Chilco o Fucsia** (*Fuchsia magellanica*) 
19. **Cochayuyo, Ulte** (*Durvillea antarctica*)
20. **Copihue** (*Lapageria rosea*)
21. **Culantrillo** (*Adiantum chilensis*) 
22. **Diente de León** (*Taraxacum officinale*) 
23. **Eter** (*Artemisia abrotanum*)
24. **Eucalipto** (*Eucalyptus globulus*) 
25. **Guayacán, Palo Santo Chileno** (*Porlieria chilensis*) 
26. **Hierba del Clavo** (*Geum quellyon sweet* / *Geum magellanicum*) 
27. **Hierba del paño** (*Verbascum thapsus*)
28. **Hierba Dulce (Palo Dulce)** (*Calceolaria thyrsiflora*)
29. **Hinojo** (*Foeniculum vulgare*)
30. **Hualtata, Lampazo** (*Senecio fistulosus*) 
31. **Lampayo** (*Lampaya medicinalis*)
32. **Laurel** (*Laurelia sempervirens* / *Laurus nobilis*) 
33. **Llareta** (*Laretia acaulis*) 
34. **Llanten** (*Plantago major*) 
35. **Maiten** (*Maytenus boaria*) 
36. **Malva** (*Malva sylvestris*) 
37. **Manzanilla** (*Matricaria chamomilla*) 
38. **Maqui** (*Aristotelia chilensis*) 
39. **Matico, Pañil** (*Buddleja globosa*)
40. **Melón Reuma** (*Ecballium elaterium*) 
41. **Menta** (*Mentha spp.*) 
42. **Miyaya** (*Datura stramonium*) 
43. **Naranjo** (*Citrus aurantium*) 
44. **Nalca, Pangue** (*Gunnera tinctoria*) 
45. **Natre** (*Solanum ligustrinum*) 
46. **Nogal** (*Juglans regia*) 
47. **Ñanco lahuen** (*Valeriana carnosa*)
48. **Oregano** (*Origanum majorana*) 
49. **Ortiga** (*Urtica urens* / *Urtica dioica* / *Urtica andicola*)
50. **Paico** (*Dysphania ambrosioides*) 
51. **Palqui** (*Cestrum parqui*) 
52. **Palto** (*Persea americana*) 
53. **Pata de Vaca** (*Bauhinia candicans*) 
54. **Peumo** (*Cryptocarya alba*) 
55. **Pichi, Pichi Romero** (*Fabiana imbricata*) 
56. **Pimiento, Molle** (*Schinus areira*) 
57. **Pingo-Pingo** (*Ephedra chilensis* / *Ephedra andina*)
58. **Quebracho Blanco, Sen Chileno** (*Senna stipulacea*) 
59. **Quillay** (*Quillaja saponaria*) 
60. **Quilo, Mollaco, Voqui** (*Muehlenbeckia hastulata*) 
61. **Quinchamalí** (*Quinchamalium chilense*) 
62. **Quintral** (*Tristerix corymbosus*) 
63. **Radal** (*Lomatia hirsuta*) 
64. **Rica-Rica, Kore** (*Acantholippia deserticola*) 
65. **Romero** (*Rosmarinus officinalis*) 
66. **Rosa Mosqueta** (*Rosa moschata*)
67. **Ruda** (*Ruta graveolens*) 
68. **Sabinilla, Perlilla** (*Margyricarpus pinnatus*) 
69. **Salvia** (*Salvia officinalis*) 
70. **Salvia blanca** (*Sphacele salviae*) 
71. **Sanguinaria** (*Polygonum sanguinaria*) 
72. **Sauce Amargo / Sauce Llorón** (*Salix humboldtiana* / *Salix babylonica*) 
73. **Sauco** (*Sambucus nigra*)
74. **Tilo** (*Tilia spp.*) 
75. **Toronjil Cuyano / Toronjil** (*Marrubium vulgare* / *Melissa officinalis*) 
76. **Triqui-Triqui, Trique** (*Libertia sessiliflora*) 
77. **Valeriana** (*Valeriana officinalis*)
78. **Verbena** (*Verbena litoralis*) 
79. **Violeta** (*Viola odorata*)
80. **Vira-Vira** (*Pseudognaphalium viravira*) 
81. **Yerba de la Plata, Limpiaplata** (*Equisetum bogotense*) 
82. **Yerba del Clavo, Leliantu** (*Geum magellanicum*) 
83. **Yerba del Lagarto, Calaguala** (*Synammia feuillei*) 
84. **Zarzamora** (*Rubus ulmifolius*)
85. **Zarzaparrilla** (*Ribes cucullatum*)

---

## 7. Requisitos No Funcionales y Criterios de Aceptación
1. **Portabilidad UI:** Todo el diseño CSS debe ser autogestionado por clases utilitarias de Tailwind mediante CDN sin dependencias locales de compilación (npm/node).
2. **Seguridad y Sesiones:** Rutas críticas protegidas por el decorador `@login_required` para vistas de administración o marcaje de favoritos.
3. **Persistencia en Render:** Configurar adecuadamente la base SQLite mediante variables de entorno o almacenamiento persistente controlado para asegurar la disponibilidad del catálogo botánico tras reinicios del contenedor.
