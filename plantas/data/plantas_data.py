"""
Datos de las 85 especies de plantas medicinales nativas y asilvestradas de Chile.

Cada entrada contiene todos los campos requeridos por el modelo Planta:
- nombre_comun, nombre_cientifico, familia_botanica
- origen (NATIVA / ASILVESTRADA)
- zona_macro (NORTE / CENTRO / SUR / PATAGONIA)
- regiones, habitat
- descripcion_hoja, descripcion_tallo, descripcion_flor
- foto_real
- uso_principal, efecto_terapeutico, receta_preparacion, advertencias
"""

PLANTAS_DATA = [
    # ---------------------------------------------------------------------------
    # 1. Ajenjo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Ajenjo",
        "nombre_cientifico": "Artemisia absinthium",
        "familia_botanica": "Asteraceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule",
        "habitat": "Terrenos secos y soleados, bordes de caminos, laderas pedregosas y suelos pobres en nutrientes.",
        "descripcion_hoja": "Hojas alternas, pecioladas, de hasta 8 cm de largo, profundamente divididas en segmentos lanceolados, de color verde grisáceo por el haz y blanquecinas por el envés debido a una densa pilosidad. Desprenden un aroma característico intenso y amargo.",
        "descripcion_tallo": "Tallo herbáceo erecto, de 60 a 120 cm de altura, ramificado en la parte superior, de textura estriada y color verde plateado cubierto de finos pelos.",
        "descripcion_flor": "Inflorescencias en panículas de capítulos pequeños, de 3 a 5 mm de diámetro, con flores tubulares de color amarillo verdoso. Florece entre noviembre y marzo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Ajenjo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Antiparasitario, Emenagogo",
        "receta_preparacion": "Infusión: Verter 1 taza de agua hirviendo sobre 1 cucharadita de hojas secas (2-3 g). Reposar 10 minutos, colar y beber hasta 2 tazas al día, preferentemente antes de las comidas. Tintura: Macerar 20 g de hojas frescas en 100 ml de alcohol de 70° durante 10 días. Tomar 15 gotas en agua antes de cada comida.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Su uso prolongado puede provocar daños neurológicos por el aceite esencial de tuyona. Evitar en niños menores de 12 años. No exceder la dosis recomendada. Contraindicado en personas con epilepsia o úlceras digestivas.",
    },
    # ---------------------------------------------------------------------------
    # 2. Ajo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Ajo",
        "nombre_cientifico": "Allium sativum",
        "familia_botanica": "Amaryllidaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Atacama, Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Biobío",
        "habitat": "Cultivado extensamente en huertos y jardines; crece en suelos sueltos, fértiles y bien drenados, con exposición solar directa.",
        "descripcion_hoja": "Hojas planas, lineares, de hasta 50 cm de largo y 2-3 cm de ancho, de color verde intenso, con una quilla central prominente. Crecen desde la base del bulbo en disposición dística.",
        "descripcion_tallo": "Tallo floral erecto de 30 a 100 cm de altura, cilíndrico, hueco, que emerge desde el centro del bulbo. El tallo verdadero es comprimido y subterráneo, formando el disco basal del bulbo.",
        "descripcion_flor": "Inflorescencia en umbela globosa, con flores pequeñas de color blanco verdoso o rosado, protegidas por una espata membranosa. Entre las flores se desarrollan bulbillos. Florece en primavera-verano.",
        "foto_real": "https://via.placeholder.com/400x300?text=Ajo",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Antihipertensivo, Antimicrobiano, Expectorante, Hipotensor, Hipolipemiante",
        "receta_preparacion": "Jarabe: Machacar 5 dientes de ajo y macerar en 1/2 taza de miel por 12 horas. Tomar 1 cucharada 3 veces al día para afecciones respiratorias. Leche de ajo: Hervir 3 dientes de ajo picados en 1 taza de leche por 5 minutos. Beber antes de dormir para conciliar el sueño y aliviar la tos.",
        "advertencias": "Consumir con precaución en tratamientos anticoagulantes (potencia su efecto). Puede causar irritación gástrica en personas sensibles. Evitar en ayunas en caso de gastritis. Suspender 2 semanas antes de una cirugía. No aplicar directamente sobre la piel por riesgo de quemaduras.",
    },
    # ---------------------------------------------------------------------------
    # 3. Arrayán
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Arrayán",
        "nombre_cientifico": "Luma apiculata",
        "familia_botanica": "Myrtaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Bosques templados húmedos, riberas de ríos y lagos, desde el nivel del mar hasta los 500 m de altitud. Tolera suelos arenosos y arcillosos con buena humedad.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma elíptica a ovada, de 1.5 a 3 cm de largo, de textura coriácea, de color verde oscuro brillante en el haz y más pálido en el envés. Presentan glándulas translúcidas de aceites esenciales.",
        "descripcion_tallo": "Tronco erecto de corteza lisa, de color canela rojizo que se desprende en finas láminas papiráceas, dejando manchas blanquecinas características. Ramas delgadas y flexibles. Alcanza 5-15 m de altura.",
        "descripcion_flor": "Flores solitarias o en pequeños grupos, axilares, de 1.5 a 2 cm de diámetro, con 4 pétalos blancos y numerosos estambres largos y vistosos. Florece entre diciembre y marzo. El fruto es una baya globosa de color negro violáceo comestible.",
        "foto_real": "https://via.placeholder.com/400x300?text=Arrayan",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Astringente, Digestivo, Antidiarreico, Antiséptico",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 litro de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza después de cada comida para trastornos digestivos. Baño de asiento: Hervir 100 g de corteza en 2 litros de agua por 15 minutos, colar y agregar al agua del baño para afecciones vaginales.",
        "advertencias": "No se han reportado toxicidades significativas con uso moderado. Sin embargo, se recomienda evitar su consumo durante el embarazo y la lactancia por falta de estudios. Las bayas son comestibles pero en exceso pueden causar estreñimiento.",
    },
    # ---------------------------------------------------------------------------
    # 4. Bailahuén
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Bailahuén",
        "nombre_cientifico": "Haplopappus spp.",
        "familia_botanica": "Asteraceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule",
        "habitat": "Laderas asoleadas y secas, cerros costeros e interiores, suelos pobres y pedregosos, desde el nivel del mar hasta los 1.500 m de altitud.",
        "descripcion_hoja": "Hojas alternas, simples, de forma linear a lanceolada, de 2 a 5 cm de largo, de bordes enteros o ligeramente dentados, de textura coriácea y color verde grisáceo. Superficie resinoso-glandular con aroma aromático característico.",
        "descripcion_tallo": "Tallos leñosos en la base, ramificados desde la base, de 30 a 80 cm de altura, erectos o ascendentes, de color pardo grisáceo.",
        "descripcion_flor": "Capítulos solitarios en el extremo de las ramas, de 2 a 4 cm de diámetro, con flores liguladas periféricas de color amarillo intenso y flores tubulares centrales del mismo color. Florece entre octubre y enero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Bailahuen",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Colagogo, Estomacal",
        "receta_preparacion": "Infusión: Agregar 1 cucharada de hojas y tallos secos a 1 litro de agua hirviendo. Reposar 10 minutos, colar y beber 1 taza después de cada comida. Se utiliza tradicionalmente para trastornos hepáticos y digestivos. También se prepara en aguardiente como aperitivo digestivo.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. El uso excesivo puede provocar irritación gástrica. Evitar en personas con obstrucción biliar. Consultar con un médico antes de usar si se padecen enfermedades hepáticas crónicas.",
    },
    # ---------------------------------------------------------------------------
    # 5. Boldo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Boldo",
        "nombre_cientifico": "Peumus boldus",
        "familia_botanica": "Monimiaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Bosques esclerófilos de la zona central, laderas de cerros con exposición norte, suelos profundos y bien drenados. Desde el nivel del mar hasta los 1.000 m de altitud.",
        "descripcion_hoja": "Hojas opuestas, ovadas a elípticas, de 3 a 7 cm de largo, de textura coriácea, color verde oscuro en el haz y más pálido en el envés. Presentan bordes enteros y un aroma característico intenso. Son ásperas al tacto por la presencia de numerosas glándulas oleíferas.",
        "descripcion_tallo": "Árbol dioico de 5 a 15 m de altura, con corteza grisácea y rugosa. Ramas jóvenes cubiertas de una fina pubescencia. Copa densa y redondeada.",
        "descripcion_flor": "Flores dioicas, pequeñas, de color blanco amarillento, dispuestas en racimos terminales. Las flores masculinas presentan numerosos estambres; las femeninas tienen estaminodios. Florece entre octubre y diciembre. El fruto es una drupa pequeña de color verde amarillento comestible.",
        "foto_real": "https://via.placeholder.com/400x300?text=Boldo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Colagogo, Sedante suave",
        "receta_preparacion": "Infusión: Colocar 2-3 hojas secas de boldo en 1 taza de agua hirviendo. Reposar 5-8 minutos, colar y beber preferentemente después de las comidas. Máximo 3 tazas al día. Para problemas hepáticos se puede combinar con hierba del clavo y malva.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. El aceite esencial de boldo contiene ascaridol, tóxico en dosis elevadas. No usar en personas con obstrucción de las vías biliares. Evitar su consumo por más de 4 semanas continuas. Contraindicado en personas con enfermedades hepáticas graves.",
    },
    # ---------------------------------------------------------------------------
    # 6. Borraja
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Borraja",
        "nombre_cientifico": "Borago officinalis",
        "familia_botanica": "Boraginaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, Los Lagos",
        "habitat": "Terrenos cultivados, bordes de caminos, huertos y jardines. Prefiere suelos fértiles y húmedos con exposición solar moderada.",
        "descripcion_hoja": "Hojas alternas, simples, de forma oval a lanceolada, de 5 a 15 cm de largo, de color verde oscuro, cubiertas de pelos rígidos y ásperos que le dan una textura característica. Las hojas inferiores son pecioladas y las superiores sésiles.",
        "descripcion_tallo": "Tallo erecto, hueco, suculento, de 30 a 60 cm de altura, muy ramificado, cubierto de pelos ásperos y blanquecinos.",
        "descripcion_flor": "Flores pentámeras, colgantes, de 2 a 3 cm de diámetro, con corola de color azul intenso a violáceo, raramente blanca, con un cono central de estambres negruzcos. Cáliz con sépalos lanceolados muy pelosos. Florece desde primavera hasta otoño.",
        "foto_real": "https://via.placeholder.com/400x300?text=Borraja",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Diurético, Sudorífico, Emoliente, Antiinflamatorio",
        "receta_preparacion": "Infusión: Verter 1 taza de agua hirviendo sobre 1 cucharada de hojas y flores frescas o secas. Reposar 10 minutos, endulzar con miel y beber 2-3 tazas al día para resfriados y afecciones respiratorias. Las hojas jóvenes también se usan en ensaladas y sopas.",
        "advertencias": "No consumir durante el embarazo (puede estimular contracciones uterinas). El uso prolongado puede afectar la función hepática por los alcaloides pirrolizidínicos. No exceder las dosis recomendadas. Evitar en personas con enfermedades hepáticas.",
    },
    # ---------------------------------------------------------------------------
    # 7. Cabello de ángel
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Cabello de ángel",
        "nombre_cientifico": "Cuscuta chilensis",
        "familia_botanica": "Convolvulaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule",
        "habitat": "Parásita sobre arbustos y hierbas en laderas asoleadas, bordes de caminos y matorrales de la zona central. Crece sobre plantas hospederas como el quilo y el palqui.",
        "descripcion_hoja": "Hojas reducidas a escamas diminutas, sin clorofila, de color amarillo anaranjado, dispuestas de forma alterna a lo largo del tallo. No realiza fotosíntesis; obtiene nutrientes de la planta hospedera mediante haustorios.",
        "descripcion_tallo": "Tallos filiformes, largos (hasta 1 m o más), delgados como cabellos, de color amarillo a naranja intenso, enredados y ramificados, que se adhieren a la planta hospedera mediante estructuras chupadoras (haustorios).",
        "descripcion_flor": "Flores pequeñas, de 3 a 5 mm, de color blanco cremoso a rosado, agrupadas en glomérulos compactos a lo largo del tallo. Corola campanulada con 5 lóbulos. Florece entre primavera y verano. Produce cápsulas globosas con 2-4 semillas.",
        "foto_real": "https://via.placeholder.com/400x300?text=Cabello+de+angel",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Hepático, Hipotensor",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de tallos frescos en 1 litro de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza 2-3 veces al día. Se utiliza tradicionalmente para tratar la hipertensión arterial y como depurativo sanguíneo.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Usar con precaución en personas con presión arterial baja. No confundir con otras especies de Cuscuta que crecen sobre plantas tóxicas. Consultar a un médico antes de usar.",
    },
    # ---------------------------------------------------------------------------
    # 8. Cachanlagua
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Cachanlagua",
        "nombre_cientifico": "Centarium cachanlahuen",
        "familia_botanica": "Gentianaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío",
        "habitat": "Claros de bosques esclerófilos, laderas pedregosas, praderas húmedas y bordes de cursos de agua. Prefiere suelos húmedos y sombra parcial.",
        "descripcion_hoja": "Hojas basales en roseta, de forma espatulada a ovada, de 2 a 5 cm de largo; hojas superiores opuestas, sésiles, de forma lanceolada, de color verde claro a amarillento, con 3-5 nervaduras longitudinales prominentes.",
        "descripcion_tallo": "Tallo erecto, de 15 a 40 cm de altura, delgado, cuadrangular, ramificado en la parte superior, de color verde claro.",
        "descripcion_flor": "Flores terminales en cimas, de 1.5 a 2 cm de diámetro, con corola tubulosa de 5 pétalos de color rosa intenso a púrpura, raramente blancos. Cáliz tubular con 5 dientes agudos. Florece entre noviembre y febrero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Cachanlagua",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Tónico amargo, Febrífugo",
        "receta_preparacion": "Infusión: Hervir 1 cucharadita de la planta seca en 1 taza de agua por 3 minutos. Reposar 5 minutos, colar y beber 1 taza en ayunas para problemas hepáticos. También se prepara en maceración en vino blanco: 30 g de planta seca en 1 litro de vino por 7 días; tomar 1 copita antes de las comidas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Su sabor es muy amargo. No exceder las dosis recomendadas. Contraindicado en personas con gastritis o úlceras digestivas. No confundir con la cachanlahua blanca (Eupatorium salviae).",
    },
    # ---------------------------------------------------------------------------
    # 9. Canelo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Canelo",
        "nombre_cientifico": "Drimys winteri",
        "familia_botanica": "Winteraceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Bosques templados húmedos y lluviosos, desde el nivel del mar hasta los 1.500 m de altitud. Crece en suelos profundos, húmedos y ricos en materia orgánica, a orillas de ríos y lagos.",
        "descripcion_hoja": "Hojas simples, alternas, de forma lanceolada a elíptica, de 5 a 15 cm de largo, de color verde brillante en el haz y glaucas en el envés. Textura coriácea, bordes enteros, con nervadura pinnada prominente. Al estrujarlas liberan un aroma picante similar a la canela.",
        "descripcion_tallo": "Árbol de 5 a 15 m de altura, con tronco recto de corteza pardo-rojiza a grisácea, rugosa, con lenticelas prominentes. Ramas robustas que forman una copa piramidal.",
        "descripcion_flor": "Flores actinomorfas, de 2 a 3 cm de diámetro, dispuestas en umbelas terminales. Con 4-7 pétalos de color blanco cremoso a amarillo pálido, numerosos estambres y 1-5 carpelos. Florece entre octubre y enero. El fruto es una baya negra azulada comestible.",
        "foto_real": "https://via.placeholder.com/400x300?text=Canelo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Analgésico, Antiinflamatorio, Antiescorbútico, Digestivo, Febrífugo",
        "receta_preparacion": "Infusión de corteza: Hervir 1 cucharada de corteza troceada en 1 taza de agua por 10 minutos. Reposar 5 minutos, colar y beber 1 taza 2-3 veces al día para resfriados y dolores reumáticos. La corteza también se usa en baños para aliviar dolores musculares.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. En dosis elevadas puede causar irritación gástrica y vómitos. El aceite esencial es irritante en aplicación tópica pura. Usar con precaución en personas con hipersensibilidad. La corteza fresca puede provocar estornudos por su acción irritante sobre las mucosas.",
    },
    # ---------------------------------------------------------------------------
    # 10. Cebolla
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Cebolla",
        "nombre_cientifico": "Allium cepa",
        "familia_botanica": "Amaryllidaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Atacama, Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Biobío",
        "habitat": "Cultivada extensamente en huertas; prefiere suelos sueltos, fértiles y bien drenados con alto contenido de materia orgánica.",
        "descripcion_hoja": "Hojas fistulosas (huecas), cilíndricas, de hasta 50 cm de largo, de color verde azulado, cubiertas de una capa cerosa. Crecen en disposición dística desde el bulbo basal.",
        "descripcion_tallo": "Tallo floral erecto, cilíndrico, inflado en la parte media, de 60 a 100 cm de altura, hueco, que emerge desde el centro del bulbo. El tallo verdadero es un disco comprimido en la base del bulbo.",
        "descripcion_flor": "Inflorescencia en umbela globosa de 3 a 6 cm de diámetro, con numerosas flores pequeñas de color blanco a rosado violáceo, protegidas inicialmente por una espata membranosa. Florece en primavera-verano. El fruto es una cápsula trilocular.",
        "foto_real": "https://via.placeholder.com/400x300?text=Cebolla",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Expectorante, Diurético, Antiinflamatorio, Antimicrobiano, Hipotensor",
        "receta_preparacion": "Jarabe antitusivo: Picar finamente 1 cebolla grande, colocarla en un frasco con 3 cucharadas de miel. Reposar por 4-6 horas hasta que suelte el jugo. Tomar 1 cucharada cada 4 horas para la tos y resfriados. Cataplasma: Aplicar la cebolla asada directamente sobre forúnculos para acelerar su maduración.",
        "advertencias": "Consumir con moderación en caso de gastritis o reflujo gastroesofágico. Puede interferir con medicamentos anticoagulantes. Evitar su consumo excesivo durante el embarazo. Puede causar halitosis y flatulencias.",
    },
    # ---------------------------------------------------------------------------
    # 11. Cedrón
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Cedrón",
        "nombre_cientifico": "Aloysia citrodora",
        "familia_botanica": "Verbenaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío",
        "habitat": "Cultivado en huertos y jardines; prefiere suelos fértiles y bien drenados con exposición solar directa. Originario de Sudamérica, naturalizado en Chile central.",
        "descripcion_hoja": "Hojas simples, opuestas o verticiladas de a 3, de forma lanceolada a elíptica, de 3 a 8 cm de largo, de color verde claro, bordes enteros o ligeramente dentados. Desprenden un intenso aroma a limón característico. Textura áspera al tacto.",
        "descripcion_tallo": "Arbusto de 1 a 3 m de altura, muy ramificado, con tallos leñosos de color pardo grisáceo y ramas jóvenes verde claras, estriadas y ligeramente pubescentes.",
        "descripcion_flor": "Inflorescencias en espigas terminales y axilares de 5 a 10 cm de largo, con pequeñas flores blancas a liláceas pálidas, de 4-5 mm de diámetro, con corola bilabiada. Florece desde fines de primavera hasta otoño.",
        "foto_real": "https://via.placeholder.com/400x300?text=Cedron",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Carminativo, Antiespasmódico, Sedante suave",
        "receta_preparacion": "Infusión: Agregar 5-6 hojas frescas o 1 cucharadita de hojas secas a 1 taza de agua hirviendo. Reposar 5-7 minutos, colar y endulzar con miel. Beber 1 taza después de las comidas para facilitar la digestión. También se usa para dar sabor a postres, helados y bebidas.",
        "advertencias": "No se recomienda su consumo durante el embarazo ni la lactancia. En dosis elevadas puede causar irritación gástrica. Su aceite esencial puro puede ser irritante para la piel. Evitar el consumo excesivo por períodos prolongados.",
    },
    # ---------------------------------------------------------------------------
    # 12. Cepa de caballo / Amores secos
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Cepa de caballo, Amores secos",
        "nombre_cientifico": "Acaena splendens",
        "familia_botanica": "Rosaceae",
        "origen": "NATIVA",
        "zona_macro": "PATAGONIA",
        "regiones": "Aysén, Magallanes",
        "habitat": "Estepas patagónicas, laderas expuestas al viento, suelos arenosos y rocosos, desde el nivel del mar hasta los 1.000 m de altitud.",
        "descripcion_hoja": "Hojas compuestas, imparipinnadas, con 5-9 folíolos de forma obovada a elíptica, de 1 a 3 cm de largo, de color verde grisáceo, con bordes dentados. Textura coriácea, dispuestas en roseta basal.",
        "descripcion_tallo": "Tallos rastreros o ascendentes, de hasta 50 cm de largo, delgados, de color rojizo a pardo, que enraízan en los nudos formando densas alfombras.",
        "descripcion_flor": "Inflorescencias en cabezuelas globosas terminales, de 1.5 a 2 cm de diámetro, con numerosas flores pequeñas de color blanco verdoso. El fruto es un aquenio cubierto de espinas ganchudas que se adhieren al pelaje de los animales (dispersión epizoócora).",
        "foto_real": "https://via.placeholder.com/400x300?text=Cepa+caballo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Antiinflamatorio",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de hojas y raíces secas en 1 litro de agua por 10 minutos. Reposar 10 minutos, colar y beber 1 taza 2-3 veces al día como depurativo sanguíneo. Tradicionalmente usada en la medicina Kawésqar para tratar infecciones urinarias.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No se han reportado toxicidades significativas, pero se recomienda uso moderado. Consultar con un profesional de la salud antes de usar como tratamiento.",
    },
    # ---------------------------------------------------------------------------
    # 13. Coca
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Coca",
        "nombre_cientifico": "Erythroxylum coca",
        "familia_botanica": "Erythroxylaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "NORTE",
        "regiones": "Arica y Parinacota, Tarapacá",
        "habitat": "Cultivada en valles precordilleranos y quebradas del extremo norte, desde los 500 hasta los 2.000 m de altitud. Prefiere suelos fértiles y húmedos en climas subtropicales.",
        "descripcion_hoja": "Hojas simples, alternas, de forma elíptica a obovada, de 3 a 7 cm de largo, de color verde claro a intenso, textura membranácea delgada, con bordes enteros. Presenta dos líneas curvas longitudinales paralelas a la nervadura central (carácter distintivo).",
        "descripcion_tallo": "Arbusto de 1 a 3 m de altura, con tallos leñosos delgados, corteza lisa de color pardo claro. Ramificación abundante desde la base.",
        "descripcion_flor": "Flores pequeñas, de 3-5 mm de diámetro, de color blanco cremoso, dispuestas en grupos de 2-6 en las axilas foliares. Cáliz cupuliforme con 5 dientes. Corola con 5 pétalos. Florece durante todo el año en condiciones favorables. El fruto es una drupa roja comestible.",
        "foto_real": "https://via.placeholder.com/400x300?text=Coca",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Estimulante, Analgésico, Digestivo, Antifatiga",
        "receta_preparacion": "Masticación tradicional (acullico): Masticar 3-5 hojas secas con un poco de ceniza o bicarbonato para liberar los alcaloides. Infusión: 1 cucharada de hojas secas en 1 taza de agua hirviendo, reposar 10 minutos. Se usa para aliviar el mal de altura y la fatiga.",
        "advertencias": "Su uso está regulado por la legislación chilena e internacional. El consumo prolongado puede causar dependencia. No consumir durante el embarazo ni la lactancia. Puede interferir con el sueño y causar ansiedad. Contraindicado en personas con hipertensión arterial no controlada.",
    },
    # ---------------------------------------------------------------------------
    # 14. Culén
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Culén",
        "nombre_cientifico": "Otholobium glandulosum",
        "familia_botanica": "Fabaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Bosques esclerófilos y matorrales, laderas de cerros con exposición norte, suelos arcillosos y bien drenados. Desde el nivel del mar hasta los 1.200 m de altitud.",
        "descripcion_hoja": "Hojas compuestas, trifoliadas, con folíolos de forma obovada a elíptica, de 1 a 3 cm de largo, de color verde oscuro, con bordes finamente dentados y glándulas translúcidas punteadas. Textura suave y aromática al estrujarlas.",
        "descripcion_tallo": "Arbusto de 1 a 2.5 m de altura, muy ramificado, con tallos leñosos de color pardo grisáceo y ramas jóvenes angulosas de color verde.",
        "descripcion_flor": "Inflorescencias en racimos axilares de 3 a 8 cm de largo, con flores papilionadas de color blanco a lila pálido, de 6-8 mm de largo. Cáliz campanulado con 5 dientes. Florece entre noviembre y enero. El fruto es una legumbre pequeña.",
        "foto_real": "https://via.placeholder.com/400x300?text=Culen",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Estomacal, Antiséptico, Vulnerario",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de hojas secas en 1 litro de agua por 5 minutos. Reposar 10 minutos y beber 1 taza después de cada comida para problemas digestivos. En uso externo, la infusión concentrada se aplica en compresas para lavar heridas y llagas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Se recomienda uso moderado, ya que dosis elevadas pueden causar irritación digestiva. No confundir con el Culen blanco (Psoralea glandulosa). Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 15. Chachacoma
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Chachacoma",
        "nombre_cientifico": "Senecio eriophyton",
        "familia_botanica": "Asteraceae",
        "origen": "NATIVA",
        "zona_macro": "NORTE",
        "regiones": "Antofagasta, Atacama, Coquimbo",
        "habitat": "Altas montañas de la cordillera de los Andes, desde los 2.500 hasta los 4.500 m de altitud. Crece en laderas rocosas, pedregales y suelos volcánicos con exposición solar intensa.",
        "descripcion_hoja": "Hojas basales en roseta densa, de forma espatulada a lanceolada, de 5 a 15 cm de largo, de color verde grisáceo, cubiertas de un denso tomento lanoso blanquecino que las protege de la radiación solar extrema. Bordes dentados.",
        "descripcion_tallo": "Tallo floral erecto, de 20 a 50 cm de altura, grueso, algodonoso, de color blanquecino, que emerge desde el centro de la roseta basal.",
        "descripcion_flor": "Capítulos grandes, de 3 a 5 cm de diámetro, agrupados en corimbos densos. Flores liguladas periféricas de color amarillo intenso y flores tubulares centrales del mismo color. Florece entre diciembre y marzo. Es la flor emblemática del altiplano chileno.",
        "foto_real": "https://via.placeholder.com/400x300?text=Chachacoma",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Expectorante, Broncodilatador, Antitusivo, Antiasmático",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de hojas y tallos secos en 1 litro de agua por 10 minutos. Reposar 5 minutos, colar y beber 2-3 tazas al día para aliviar afecciones respiratorias como bronquitis, asma y resfriados. Tradicionalmente se usa con leche caliente y miel.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. El género Senecio contiene alcaloides pirrolizidínicos que pueden ser hepatotóxicos en dosis elevadas o uso prolongado. No exceder las dosis recomendadas. No usar por más de 2 semanas consecutivas.",
    },
    # ---------------------------------------------------------------------------
    # 16. Chequén
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Chequén",
        "nombre_cientifico": "Luma chequen",
        "familia_botanica": "Myrtaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío",
        "habitat": "Riberas de ríos y esteros, lugares húmedos y sombríos, fondos de quebradas. Desde el nivel del mar hasta los 500 m de altitud.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma elíptica a lanceolada, de 1 a 3 cm de largo, de color verde claro brillante en el haz y más pálido en el envés. Textura coriácea, con glándulas oleíferas translúcidas. Aroma aromático característico al estrujarlas.",
        "descripcion_tallo": "Árbol o arbusto de 3 a 10 m de altura, con tronco de corteza lisa de color canela rojizo que se desprende en placas delgadas, dejando manchas blanquecinas. Ramas delgadas y colgantes.",
        "descripcion_flor": "Flores axilares, solitarias o en pequeños grupos, de 1 a 1.5 cm de diámetro, con 4 pétalos blancos y numerosos estambres blancos prominentes. Florece entre noviembre y febrero. El fruto es una baya comestible de color negro violáceo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Chequen",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Astringente, Antidiarreico, Digestivo, Antiséptico",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 litro de agua por 5 minutos. Reposar 10 minutos y beber 1 taza 2-3 veces al día para diarreas y trastornos digestivos. En uso externo, la decocción concentrada se usa para lavar heridas y como gargarismo para inflamaciones bucales.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Su uso excesivo puede causar estreñimiento por su efecto astringente. No se recomienda en niños menores de 6 años. Consultar a un médico si la diarrea persiste por más de 2 días.",
    },
    # ---------------------------------------------------------------------------
    # 17. Chépica
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Chépica",
        "nombre_cientifico": "Paspalum vaginatum",
        "familia_botanica": "Poaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío",
        "habitat": "Praderas húmedas, bordes de cursos de agua, zanjas y terrenos pantanosos. Tolera suelos salinos y encharcados, desde el nivel del mar hasta los 500 m.",
        "descripcion_hoja": "Hojas lineares, de 5 a 20 cm de largo y 3-8 mm de ancho, de color verde claro a glauco, con una lígula membranosa corta. Textura áspera en los bordes. Vainas foliares comprimidas, de color verde a púrpura en la base.",
        "descripcion_tallo": "Tallos herbáceos, decumbentes en la base y luego ascendentes, de 20 a 60 cm de largo, comprimidos, formando densos céspedes o matas mediante estolones y rizomas.",
        "descripcion_flor": "Inflorescencia en panícula de 2 a 5 racimos espiciformes, de 2 a 6 cm de largo, de color verde a púrpura. Espiguillas dispuestas en 2 filas sobre un lado del raquis. Florece durante todo el período cálido.",
        "foto_real": "https://via.placeholder.com/400x300?text=Chepica",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Antiséptico urinario",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de la planta fresca (tallos y hojas) en 1 litro de agua por 10 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para infecciones urinarias y como depurativo. Tradicionalmente se usa en combinación con cola de caballo.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Por su efecto diurético, se recomienda mantener una adecuada hidratación. No exceder las dosis recomendadas. Consultar con un profesional de la salud para uso prolongado.",
    },
    # ---------------------------------------------------------------------------
    # 18. Chilco o Fucsia
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Chilco, Fucsia",
        "nombre_cientifico": "Fuchsia magellanica",
        "familia_botanica": "Onagraceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Bosques templados húmedos, riberas de ríos y lagos, claros de bosque. Desde el nivel del mar hasta los 1.200 m de altitud. Prefiere suelos húmedos y ricos en materia orgánica.",
        "descripcion_hoja": "Hojas simples, opuestas o verticiladas de a 3, de forma ovada a lanceolada, de 2 a 7 cm de largo, de color verde oscuro, bordes finamente dentados. Textura membranácea, con nervadura pinnada prominente en el envés.",
        "descripcion_tallo": "Arbusto de 1 a 3 m de altura, con tallos leñosos delgados, de color rojizo a pardo claro, muy ramificados desde la base. Ramas jóvenes de color verde rojizo, flexibles.",
        "descripcion_flor": "Flores solitarias, axilares, colgantes, de 3 a 5 cm de largo, con cáliz tubular de color rojo intenso y corola de pétalos de color púrpura violáceo. Estambres y estilo largos y exertos. Florece desde primavera hasta otoño. El fruto es una baya alargada comestible de color púrpura oscuro.",
        "foto_real": "https://via.placeholder.com/400x300?text=Chilco",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Antiinflamatorio, Antipirético, Vulnerario",
        "receta_preparacion": "Infusión de flores y hojas: Verter 1 taza de agua hirviendo sobre 1 cucharada de flores secas. Reposar 10 minutos, colar y beber 2 tazas al día como diurético suave. En uso externo, la decocción de hojas se usa en compresas para aliviar inflamaciones cutáneas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Las bayas son comestibles en cantidades moderadas. No se conocen toxicidades significativas con uso moderado. Consultar a un médico antes de usar con fines medicinales.",
    },
    # ---------------------------------------------------------------------------
    # 19. Cochayuyo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Cochayuyo, Ulte",
        "nombre_cientifico": "Durvillaea antarctica",
        "familia_botanica": "Durvillaeaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Valparaíso, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Costas rocosas expuestas al oleaje del océano Pacífico, desde Valparaíso hasta Cabo de Hornos. Crece en el intermareal y submareal rocoso, formando grandes bosques submarinos.",
        "descripcion_hoja": "No posee hojas verdaderas. El talo (cuerpo) es laminar, de color pardo oliváceo a verde oscuro, dividido en lacinias (segmentos) alargadas, de hasta 15 m de largo. Textura coriácea y flexible. Presenta un disco basal adhesivo que lo fija a las rocas.",
        "descripcion_tallo": "El estipe (tallo) es corto, grueso, de 10-30 cm de largo y 3-5 cm de diámetro, de textura firme y elástica, de color pardo oscuro.",
        "descripcion_flor": "No produce flores. Es un alga parda (Phaeophyceae) que se reproduce mediante esporas. Los órganos reproductivos (soros) se desarrollan en el talo como manchas fértiles oscuras.",
        "foto_real": "https://via.placeholder.com/400x300?text=Cochayuyo",
        "uso_principal": "Comestible",
        "efecto_terapeutico": "Nutritivo, Aporte de yodo y minerales, Digestivo",
        "receta_preparacion": "Cochayuyo en ensalada: Remojar el cochayuyo seco en agua fría por 12 horas, cambiando el agua 2-3 veces. Hervir en agua con sal por 30-40 minutos hasta que esté tierno. Escurrir, cortar en trozos finos y aliñar con limón, aceite de oliva, cebolla picada y cilantro. También se usa en guisos, sopas y carbonadas.",
        "advertencias": "Su alto contenido de yodo lo contraindica en personas con hipertiroidismo o enfermedad tiroidea autoinmune. Recolectar solo de aguas limpias y no contaminadas. Puede causar flatulencias en personas sensibles. Consumir con moderación durante el embarazo.",
    },
    # ---------------------------------------------------------------------------
    # 20. Copihue
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Copihue",
        "nombre_cientifico": "Lapageria rosea",
        "familia_botanica": "Philesiaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos",
        "habitat": "Bosques templados húmedos y lluviosos, crece trepando sobre árboles y arbustos en el sotobosque. Desde el nivel del mar hasta los 800 m de altitud. Prefiere suelos profundos, húmedos y ricos en materia orgánica.",
        "descripcion_hoja": "Hojas simples, alternas, de forma ovada a elíptica, de 4 a 12 cm de largo, de color verde oscuro brillante, textura coriácea, con bordes enteros y ápice mucronado. Nervadura reticulada prominente en ambas caras. Son perennes.",
        "descripcion_tallo": "Tallo voluble (trepador), leñoso en la base, que puede alcanzar hasta 10 m de largo enroscándose en los árboles. De color verde a pardo rojizo, con ramificaciones abundantes.",
        "descripcion_flor": "Flores solitarias, colgantes, de 5 a 8 cm de largo, con 6 tépalos carnosos de color rojo carmín intenso (variedad blanca menos frecuente), dispuestos en dos verticilos. El fruto es una baya ovalada de color verde amarillento, comestible, con numerosas semillas. Flor nacional de Chile.",
        "foto_real": "https://via.placeholder.com/400x300?text=Copihue",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Antigotosos",
        "receta_preparacion": "Infusión de frutos: Machacar 5-6 copihues maduros y hervirlos en 1 litro de agua por 10 minutos. Reposar, colar y beber 1 taza 2 veces al día para combatir el ácido úrico y problemas renales. La infusión de tallos se usa tradicionalmente para tratar la gota y el reumatismo.",
        "advertencias": "Especie protegida en Chile por su condición de flor nacional. No extraer plantas silvestres. Los frutos son comestibles pero en exceso pueden causar estreñimiento. No consumir durante el embarazo ni la lactancia por falta de estudios de seguridad.",
    },
    # ---------------------------------------------------------------------------
    # 21. Culantrillo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Culantrillo",
        "nombre_cientifico": "Adiantum chilensis",
        "familia_botanica": "Pteridaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos",
        "habitat": "Lugares húmedos y sombríos, interiores de bosques, riberas de cursos de agua, paredes rocosas con filtración de agua. Desde el nivel del mar hasta los 1.500 m de altitud.",
        "descripcion_hoja": "Frondas (hojas) de 15 a 40 cm de largo, de forma triangular a oblonga, compuestas por numerosos folíolos pequeños de forma flabelada (en abanico), de color verde claro a medio, con pecíolos delgados y negros brillantes. Textura delicada, no tiene flores ni semillas (helecho).",
        "descripcion_tallo": "Rizoma rastrero y delgado, de color pardo oscuro a negro, cubierto de escamas. Los pecíolos de las frondas son filiformes, de color negro brillante, de 10 a 30 cm de largo.",
        "descripcion_flor": "No produce flores. Es un helecho que se reproduce mediante esporas contenidas en soros (estructuras reproductivas) ubicados en el borde inferior de los folíolos, protegidos por el margen revoluto de la hoja (falso indusio).",
        "foto_real": "https://via.placeholder.com/400x300?text=Culantrillo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Expectorante, Antitusivo, Emenagogo, Diurético",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de frondas secas en 1 litro de agua por 5 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para afecciones respiratorias, especialmente tos y bronquitis. Jarabe: Cocer 30 g de la planta en 1 litro de agua hasta reducir a la mitad, agregar 250 g de azúcar y cocer hasta punto de jarabe.",
        "advertencias": "No consumir durante el embarazo (puede estimular contracciones uterinas). En dosis elevadas puede causar irritación gástrica. No confundir con el culantrillo de pozo (Adiantum capillus-veneris). Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 22. Diente de león
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Diente de León",
        "nombre_cientifico": "Taraxacum officinale",
        "familia_botanica": "Asteraceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos, Aysén, Magallanes",
        "habitat": "Praderas, jardines, bordes de caminos, terrenos baldíos. Planta cosmopolita que crece en todo tipo de suelos, prefiriendo los ricos en nitrógeno y con exposición solar.",
        "descripcion_hoja": "Hojas basales en roseta, de forma obovada a espatulada, de 5 a 30 cm de largo, profundamente lobuladas con lóbulos triangulares dirigidos hacia atrás (runcinadas). De color verde brillante, glabras, con una nervadura central prominente de color blanquecino.",
        "descripcion_tallo": "Tallo floral (escapo) de 5 a 40 cm de altura, hueco, cilíndrico, liso, de color verde claro, que emerge desde el centro de la roseta. Contiene látex blanco lechoso. El tallo verdadero es un rizoma corto y grueso.",
        "descripcion_flor": "Capítulo floral solitario de 2 a 5 cm de diámetro, compuesto por numerosas flores liguladas de color amarillo intenso. El involucro está formado por brácteas en varias filas. Florece durante todo el año. El fruto es un aquenio con vilano plumoso que forma la característica 'bola blanca'.",
        "foto_real": "https://via.placeholder.com/400x300?text=Diente+de+leon",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Diurético, Hepático, Digestivo, Depurativo",
        "receta_preparacion": "Infusión de hojas y raíz: Hervir 1 cucharada de hojas secas o raíz troceada en 1 taza de agua por 10 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para problemas hepáticos y digestivos. Las hojas jóvenes se usan en ensaladas. La raíz tostada se usa como sucedáneo del café.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Por su efecto diurético, mantener una hidratación adecuada. Contraindicado en personas con obstrucción biliar. Puede interferir con medicamentos diuréticos y anticoagulantes. No recolectar en lugares contaminados o con pesticidas.",
    },
    # ---------------------------------------------------------------------------
    # 23. Éter (Hierba lombriguera)
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Éter, Hierba lombriguera",
        "nombre_cientifico": "Artemisia abrotanum",
        "familia_botanica": "Asteraceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío",
        "habitat": "Terrenos secos, bordes de caminos, jardines y huertos. Prefiere suelos arenosos y bien drenados con exposición solar total.",
        "descripcion_hoja": "Hojas alternas, muy divididas en segmentos filiformes (lineares), de 2 a 6 cm de largo, de color verde grisáceo a plateado por la presencia de finos pelos. Textura suave al tacto. Desprenden un aroma intenso, dulzón y alcanforado característico.",
        "descripcion_tallo": "Arbusto de 60 a 120 cm de altura, erecto, muy ramificado, con tallos leñosos en la base y herbáceos en las puntas. De color pardo grisáceo con fina pubescencia.",
        "descripcion_flor": "Capítulos pequeños, de 3 a 5 mm de diámetro, de color amarillo verdoso, dispuestos en panículas largas y densas. Flores tubulares rodeadas de brácteas involucrales. Florece desde fines de verano hasta otoño.",
        "foto_real": "https://via.placeholder.com/400x300?text=Eter",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Antiparasitario, Digestivo, Emenagogo, Febrífugo",
        "receta_preparacion": "Infusión: Hervir 1 cucharadita de hojas secas en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza en ayunas para eliminar parásitos intestinales. Tradicionalmente se usa en combinación con ajenjo y palco para tratar lombrices intestinales.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Su aceite esencial contiene tuyona, neurotóxica en dosis altas. No exceder las dosis recomendadas. Contraindicado en personas con epilepsia o enfermedades neurológicas. No usar por más de 2 semanas consecutivas.",
    },
    # ---------------------------------------------------------------------------
    # 24. Eucalipto
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Eucalipto",
        "nombre_cientifico": "Eucalyptus globulus",
        "familia_botanica": "Myrtaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos",
        "habitat": "Plantaciones forestales y árboles naturalizados en laderas de cerros, bordes de caminos y quebradas. Originario de Australia, ampliamente cultivado en Chile central y sur.",
        "descripcion_hoja": "Hojas juveniles opuestas, sésiles, de forma ovada a cordada, de color verde glauco. Hojas adultas alternas, pecioladas, de forma lanceolada y falcada, de 10 a 30 cm de largo, de color verde oscuro, coriáceas, con glándulas oleíferas translúcidas. Aroma intenso a alcanfor.",
        "descripcion_tallo": "Árbol de gran tamaño, de 30 a 60 m de altura, con tronco recto de corteza lisa que se desprende en tiras largas, de color gris claro a blanquecino. Copa abierta y ramas extendidas.",
        "descripcion_flor": "Flores solitarias, axilares, sésiles, de 2 a 4 cm de diámetro, sin pétalos (el cáliz y la corola forman un opérculo que se desprende). Numerosos estambres largos de color blanco cremoso. Florece entre otoño e invierno. El fruto es una cápsula leñosa cónica.",
        "foto_real": "https://via.placeholder.com/400x300?text=Eucalipto",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Expectorante, Antiséptico, Descongestionante, Febrífugo",
        "receta_preparacion": "Inhalaciones: Hervir un puñado de hojas en 2 litros de agua, retirar del fuego y aspirar el vapor cubriendo la cabeza con una toalla durante 10 minutos. Infusión: 1 cucharada de hojas secas en 1 taza de agua hirviendo, reposar 10 minutos, beber 2 tazas al día para resfriados. Jarabe casero con miel y hojas de eucalipto.",
        "advertencias": "No ingerir el aceite esencial puro (altamente tóxico). No consumir durante el embarazo ni la lactancia. Contraindicado en personas con asma, enfermedades hepáticas o gastrointestinales graves. No aplicar aceite esencial directamente sobre la piel sin diluir. Evitar en niños menores de 6 años.",
    },
    # ---------------------------------------------------------------------------
    # 25. Guayacán / Palo Santo Chileno
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Guayacán, Palo Santo Chileno",
        "nombre_cientifico": "Porlieria chilensis",
        "familia_botanica": "Zygophyllaceae",
        "origen": "NATIVA",
        "zona_macro": "NORTE",
        "regiones": "Atacama, Coquimbo",
        "habitat": "Laderas áridas y semiáridas de la cordillera de la Costa y valles transversales, desde los 200 hasta los 1.500 m de altitud. Crece en suelos pobres, pedregosos y con extremo déficit hídrico.",
        "descripcion_hoja": "Hojas compuestas, paripinnadas, con 6-10 folíolos pequeños de forma oblonga a elíptica, de 5 a 15 mm de largo, de color verde grisáceo, textura coriácea. Se pliegan durante la sequía para reducir la pérdida de agua. Estípulas espinosas persistentes.",
        "descripcion_tallo": "Árbol pequeño o arbusto de 2 a 6 m de altura, con tronco corto de corteza agrietada de color gris oscuro. Madera muy dura y pesada (una de las más densas de Chile). Ramas nudosas, tortuosas, con espinas.",
        "descripcion_flor": "Flores axilares, solitarias o en pares, de 1.5 a 2.5 cm de diámetro, de color lila a púrpura intenso, con 5 pétalos obovados. Florece entre octubre y diciembre. El fruto es una cápsula globosa con 5 alas membranáceas.",
        "foto_real": "https://via.placeholder.com/400x300?text=Guayacan",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Antiinflamatorio, Analgésico, Antirreumático, Depurativo",
        "receta_preparacion": "Decocción de corteza y madera: Hervir 30 g de astillas de madera o corteza en 1 litro de agua por 20 minutos. Reposar 10 minutos, colar y beber 1 taza 2 veces al día para dolores reumáticos y artritis. En uso externo, aplicar la decocción en compresas sobre las articulaciones doloridas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Su uso prolongado puede causar irritación gástrica. Especie vulnerable por sobreexplotación; usar solo material de poda o cultivo. Consultar a un médico antes de usar de forma continua.",
    },
    # ---------------------------------------------------------------------------
    # 26. Hierba del Clavo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Hierba del Clavo",
        "nombre_cientifico": "Geum quellyon",
        "familia_botanica": "Rosaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Claros de bosques templados, praderas húmedas, bordes de caminos y cursos de agua. Desde el nivel del mar hasta los 1.500 m de altitud.",
        "descripcion_hoja": "Hojas basales en roseta, lirado-pinnatífidas, de 10 a 25 cm de largo, con folíolos desiguales, de color verde oscuro, textura áspera y pubescente. Hojas caulinares reducidas, alternas, con estípulas grandes.",
        "descripcion_tallo": "Tallos florales erectos, de 30 a 80 cm de altura, delgados pero firmes, de color verde rojizo, ramificados en la parte superior, cubiertos de pelos finos.",
        "descripcion_flor": "Flores terminales, solitarias o en grupos de 2-4, de 2 a 3 cm de diámetro, con 5 pétalos de color amarillo intenso a anaranjado. Cáliz con 5 sépalos y 5 bractéolas. Numerosos estambres y pistilos. Florece entre noviembre y febrero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Hierba+del+clavo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Colagogo, Antiácido",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de raíz seca troceada en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza después de las comidas principales para problemas digestivos y hepáticos. La raíz tiene aroma y sabor similar al clavo de olor, de ahí su nombre.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. Evitar en personas con gastritis o úlceras digestivas. Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 27. Hierba del Paño (Gordolobo)
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Hierba del Paño, Gordolobo",
        "nombre_cientifico": "Verbascum thapsus",
        "familia_botanica": "Scrophulariaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos",
        "habitat": "Terrenos baldíos, bordes de caminos, laderas secas y perturbadas. Prefiere suelos arenosos, pobres y bien drenados con plena exposición solar.",
        "descripcion_hoja": "Hojas basales en roseta, de forma espatulada a oblanceolada, de 10 a 40 cm de largo, cubiertas de un denso tomento algodonoso de color blanco grisáceo que les da aspecto aterciopelado. Hojas caulinares alternas, sésiles, de tamaño decreciente hacia el ápice.",
        "descripcion_tallo": "Tallo floral erecto, robusto, de 50 a 150 cm de altura, cilíndrico, densamente cubierto de pelos lanudos blancos. No ramificado (monocárpico).",
        "descripcion_flor": "Inflorescencia en espiga densa y alargada de 20 a 50 cm de largo, con numerosas flores sésiles de color amarillo intenso, de 1.5 a 3 cm de diámetro. Corola rotácea con 5 lóbulos. Florece entre diciembre y marzo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Hierba+del+pano",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Expectorante, Emoliente, Antiinflamatorio, Antitusivo",
        "receta_preparacion": "Infusión de flores: Verter 1 taza de agua hirviendo sobre 1 cucharada de flores secas. Reposar 10-15 minutos, colar con un paño fino (para retener los pelos) y beber 2-3 tazas al día para la tos y bronquitis. En uso externo, la infusión se aplica en compresas para aliviar hemorroides e inflamaciones.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Las hojas no deben usarse internamente por sus pelos irritantes. Colar siempre con un paño fino para eliminar los pelos. No confundir con otras especies de Verbascum. Consultar a un médico para uso prolongado.",
    },
    # ---------------------------------------------------------------------------
    # 28. Hierba Dulce (Palo Dulce)
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Hierba Dulce, Palo Dulce",
        "nombre_cientifico": "Calceolaria thyrsiflora",
        "familia_botanica": "Calceolariaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule",
        "habitat": "Laderas de cerros, praderas secas, matorrales abiertos. Desde el nivel del mar hasta los 1.200 m de altitud. Prefiere suelos arcillosos y exposición solar directa.",
        "descripcion_hoja": "Hojas opuestas, de forma ovada a lanceolada, de 3 a 8 cm de largo, de color verde grisáceo, textura aterciopelada por una fina pubescencia. Bordes dentados. Las hojas superiores son sésiles y las inferiores pecioladas.",
        "descripcion_tallo": "Tallos erectos, de 30 a 80 cm de altura, ramificados desde la base, de color verde rojizo, cubiertos de pelos glandulares que les dan textura pegajosa.",
        "descripcion_flor": "Inflorescencias en tirsos terminales densos, con flores de 1 a 2 cm de largo, de forma característica de zapatilla o bolsita (personada), de color amarillo intenso. Corola bilabiada con el labio inferior muy inflado. Florece entre octubre y enero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Hierba+dulce",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Estomacal, Hipoglucemiante",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de hojas secas en 1 litro de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza 2-3 veces al día después de las comidas. Su sabor dulce la hace especialmente agradable. Se utiliza tradicionalmente para la diabetes y trastornos digestivos.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Consultar con un médico antes de usar para tratar la diabetes, ya que puede interactuar con medicamentos hipoglucemiantes. No exceder las dosis recomendadas.",
    },
    # ---------------------------------------------------------------------------
    # 29. Hinojo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Hinojo",
        "nombre_cientifico": "Foeniculum vulgare",
        "familia_botanica": "Apiaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos",
        "habitat": "Terrenos baldíos, bordes de caminos, jardines y huertos. Prefiere suelos secos, calcáreos y exposición solar directa. Naturalizado extensamente en todo Chile.",
        "descripcion_hoja": "Hojas alternas, muy divididas en segmentos filiformes (lineares) de 2 a 10 cm de largo, de color verde intenso, que le dan un aspecto plumoso. Peciolos largos envainadores en la base. Desprenden un aroma anisado intenso al estrujarlas.",
        "descripcion_tallo": "Tallo erecto, cilíndrico, estriado, de 60 a 200 cm de altura, de color verde glauco, ramificado en la parte superior. Hueco entre los nudos.",
        "descripcion_flor": "Inflorescencias en umbelas compuestas de 10 a 30 cm de diámetro, con numerosas umbélulas de flores pequeñas de color amarillo intenso. Florece entre enero y abril. El fruto es un diaquenio oblongo de 4-6 mm, de color pardo, con costillas prominentes.",
        "foto_real": "https://via.placeholder.com/400x300?text=Hinojo",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Carminativo, Antiespasmódico, Galactagogo",
        "receta_preparacion": "Infusión de semillas: Machacar ligeramente 1 cucharadita de semillas y verter 1 taza de agua hirviendo. Reposar 10 minutos, colar y beber 1 taza después de cada comida para gases y cólicos digestivos. Los bulbos se usan en ensaladas y guisos. Las hojas frescas aromatizan pescados y salsas.",
        "advertencias": "No consumir durante el embarazo en dosis medicinales (uso culinario moderado es seguro). Evitar en personas alérgicas al apio y otras Apiáceas. En dosis muy elevadas puede causar fotosensibilidad. No usar aceite esencial puro internamente.",
    },
    # ---------------------------------------------------------------------------
    # 30. Hualtata / Lampazo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Hualtata, Lampazo",
        "nombre_cientifico": "Senecio fistulosus",
        "familia_botanica": "Asteraceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Lugares húmedos y pantanosos, vegas, bordes de lagos y cursos de agua. Desde el nivel del mar hasta los 500 m de altitud.",
        "descripcion_hoja": "Hojas basales grandes, de forma oblonga a lanceolada, de 20 a 50 cm de largo, de color verde oscuro en el haz y más claro en el envés. Textura suave, bordes dentados. Hojas caulinares alternas, abrazadoras, de tamaño decreciente.",
        "descripcion_tallo": "Tallo erecto, hueco (fistuloso), grueso, de 100 a 200 cm de altura, de color verde glauco, estriado, con médula blanquecina en su interior.",
        "descripcion_flor": "Inflorescencias en corimbos terminales laxos, con numerosos capítulos de 2 a 3 cm de diámetro. Flores liguladas periféricas de color amarillo intenso y flores tubulares centrales del mismo color. Florece entre diciembre y marzo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Hualtata",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Vulnerario, Antiinflamatorio, Emoliente, Cicatrizante",
        "receta_preparacion": "Cataplasma: Machacar las hojas frescas y aplicarlas directamente sobre heridas, quemaduras, abscesos y llagas. También se prepara una decocción hirviendo 100 g de hojas en 2 litros de agua por 15 minutos, que se usa en compresas y lavados de heridas.",
        "advertencias": "No consumir internamente. Contiene alcaloides pirrolizidínicos hepatotóxicos. Solo para uso externo. No aplicar sobre heridas abiertas extensas. Consultar a un médico antes de usar. No usar en niños ni durante el embarazo y lactancia.",
    },
    # ---------------------------------------------------------------------------
    # 31. Lampayo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Lampayo",
        "nombre_cientifico": "Lampaya medicinalis",
        "familia_botanica": "Verbenaceae",
        "origen": "NATIVA",
        "zona_macro": "NORTE",
        "regiones": "Antofagasta, Atacama, Coquimbo",
        "habitat": "Laderas áridas y semiáridas de la precordillera y cordillera de los Andes, desde los 2.000 hasta los 3.500 m de altitud. Crece en suelos pedregosos y arenosos con extrema exposición solar.",
        "descripcion_hoja": "Hojas pequeñas, opuestas, de forma oblonga a espatulada, de 1 a 3 cm de largo, de color verde grisáceo, con bordes enteros o crenados. Textura coriácea y carnosa (suculenta), cubiertas de una fina pubescencia blanquecina que las protege de la radiación solar.",
        "descripcion_tallo": "Arbusto bajo, de 30 a 80 cm de altura, muy ramificado desde la base, con tallos leñosos, tortuosos, de color pardo grisáceo con corteza agrietada.",
        "descripcion_flor": "Flores tubulosas de 1.5 a 2.5 cm de largo, de color azul violáceo intenso, dispuestas en espigas terminales densas. Corola bilabiada con 5 lóbulos. Florece entre noviembre y febrero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Lampayo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Antiinflamatorio, Analgésico, Antirreumático, Depurativo",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de hojas y tallos secos en 1 litro de agua por 10 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para aliviar dolores reumáticos y musculares. En uso externo, la misma infusión concentrada se aplica en fricciones sobre las zonas doloridas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. Evitar en personas con enfermedades hepáticas o renales graves. Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 32. Laurel
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Laurel",
        "nombre_cientifico": "Laurus nobilis",
        "familia_botanica": "Lauraceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Cultivado en jardines y huertos, naturalizado en quebradas húmedas y laderas sombrías. Prefiere suelos profundos, fértiles y bien drenados, con exposición solar moderada.",
        "descripcion_hoja": "Hojas simples, alternas, de forma lanceolada a elíptica, de 5 a 12 cm de largo, de color verde oscuro brillante en el haz y más pálido en el envés. Textura coriácea y aromática, bordes enteros y ondulados. Presentan glándulas oleíferas visibles.",
        "descripcion_tallo": "Árbol o arbusto de 2 a 10 m de altura, con tronco de corteza lisa de color pardo grisáceo. Copa densa y piramidal. Ramas erectas y flexibles.",
        "descripcion_flor": "Flores dioicas, pequeñas, de 4-5 mm de diámetro, de color blanco amarillento, dispuestas en umbelas axilares. Florece entre marzo y mayo. El fruto es una baya (drupa) de color negro violáceo al madurar, de 1-1.5 cm.",
        "foto_real": "https://via.placeholder.com/400x300?text=Laurel",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Carminativo, Antiespasmódico, Expectorante",
        "receta_preparacion": "Infusión: Hervir 2-3 hojas de laurel en 1 taza de agua por 5 minutos, reposar 10 minutos y beber después de las comidas para facilitar la digestión. En la cocina, las hojas se usan para aromatizar guisos, legumbres, salsas y encurtidos. El aceite de laurel se usa en fricciones para aliviar dolores reumáticos.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. No ingerir las hojas enteras (pueden causar obstrucción intestinal). Las bayas frescas son tóxicas en grandes cantidades. El aceite esencial es irritante y no debe ingerirse puro.",
    },
    # ---------------------------------------------------------------------------
    # 33. Llareta
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Llareta",
        "nombre_cientifico": "Laretia acaulis",
        "familia_botanica": "Apiaceae",
        "origen": "NATIVA",
        "zona_macro": "NORTE",
        "regiones": "Antofagasta, Atacama, Coquimbo",
        "habitat": "Alta cordillera de los Andes, desde los 3.000 hasta los 4.500 m de altitud. Crece en laderas expuestas al viento, suelos rocosos y pedregales volcánicos con temperaturas extremas.",
        "descripcion_hoja": "Hojas densamente agrupadas en rosetas compactas, de forma linear a acicular, de 3 a 8 mm de largo, de color verde brillante a amarillento, con textura resinosa. Están cubiertas de una resina aromática pegajosa que las protege del frío extremo.",
        "descripcion_tallo": "Tallos muy ramificados y compactos que forman cojines densos y duros de hasta 2 m de diámetro y 50 cm de alto. La estructura es tan densa que puede soportar el peso de una persona. Crece extremadamente lento (1 mm por año).",
        "descripcion_flor": "Inflorescencias en umbelas pequeñas sobre escapos cortos de 5-15 cm, con flores diminutas de color amarillo verdoso. Florece entre noviembre y enero. La planta tarda décadas en alcanzar la madurez reproductiva.",
        "foto_real": "https://via.placeholder.com/400x300?text=Llareta",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Expectorante, Antitusivo, Antiasmático, Digestivo",
        "receta_preparacion": "Infusión: Raspar 1 cucharada de la resina o usar 1 cucharadita de la planta seca triturada en 1 taza de agua hirviendo. Reposar 10 minutos, colar y beber 2 tazas al día para afecciones respiratorias como bronquitis y asma. Tradicionalmente se ha usado como bálsamo para el pecho.",
        "advertencias": "Especie vulnerable por su crecimiento extremadamente lento y la sobreexplotación (se usó como combustible). No extraer plantas silvestres. No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. Consultar a un médico antes de usar.",
    },
    # ---------------------------------------------------------------------------
    # 34. Llantén
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Llantén",
        "nombre_cientifico": "Plantago major",
        "familia_botanica": "Plantaginaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Atacama, Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Terrenos pisoteados, bordes de caminos, praderas, jardines y sitios baldíos. Crece en todo tipo de suelos, prefiriendo los compactados y húmedos. Planta cosmopolita.",
        "descripcion_hoja": "Hojas basales en roseta, de forma ovada a elíptica, de 5 a 20 cm de largo, con 5-7 nervaduras longitudinales paralelas muy marcadas. De color verde oscuro, textura membranácea, bordes enteros o ligeramente dentados. Peciolo largo, acanalado.",
        "descripcion_tallo": "Tallo floral (escapo) erecto, de 10 a 50 cm de altura, cilíndrico, liso, de color verde claro, que emerge desde el centro de la roseta. El tallo verdadero es un rizoma corto y grueso.",
        "descripcion_flor": "Inflorescencia en espiga densa y alargada de 5 a 25 cm de largo, con numerosas flores pequeñas de color verdoso a marrón claro. Corola tubular con 4 lóbulos. Florece durante todo el año. El fruto es un pixidio (cápsula que se abre transversalmente).",
        "foto_real": "https://via.placeholder.com/400x300?text=Llanten",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Vulnerario, Cicatrizante, Antiinflamatorio, Expectorante",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas frescas o secas en 1 taza de agua por 5 minutos. Reposar 10 minutos y beber 2-3 tazas al día para afecciones respiratorias. En uso externo, lavar la hoja fresca, machacarla ligeramente y aplicarla directamente sobre heridas, picaduras o quemaduras. También se usa en gargarismos para inflamaciones bucales.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Las semillas pueden causar reacciones alérgicas en personas sensibles. No recolectar en lugares contaminados o con pesticidas. Su uso externo es seguro, suspender si aparece irritación.",
    },
    # ---------------------------------------------------------------------------
    # 35. Maitén
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Maitén",
        "nombre_cientifico": "Maytenus boaria",
        "familia_botanica": "Celastraceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Bosques esclerófilos, praderas, orillas de ríos y lagos. Desde el nivel del mar hasta los 1.500 m de altitud. Tolera una amplia variedad de suelos.",
        "descripcion_hoja": "Hojas simples, alternas, de forma elíptica a lanceolada, de 2 a 6 cm de largo, de color verde claro a medio, con bordes finamente dentados. Textura membranácea, con nervadura pinnada prominente. Las hojas son péndulas, lo que le da un aspecto llorón característico.",
        "descripcion_tallo": "Árbol siempreverde de 5 a 15 m de altura, con tronco recto de corteza lisa de color pardo grisáceo. Copa globosa con ramas colgantes (péndulas). Es el árbol de hoja perenne más austral de América.",
        "descripcion_flor": "Flores pequeñas, de 3-4 mm de diámetro, de color verde amarillento, dispuestas en fascículos axilares. Plantas polígamo-dioicas. Florece entre octubre y diciembre. El fruto es una cápsula loculicida de color rojo anaranjado que se abre mostrando una semilla con arilo blanco.",
        "foto_real": "https://via.placeholder.com/400x300?text=Maiten",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Analgésico, Antiinflamatorio, Antipirético, Digestivo",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza 2 veces al día para aliviar dolores de cabeza, fiebre y trastornos digestivos. La infusión concentrada se usa en lavados para aliviar dolores reumáticos.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. Las semillas pueden ser tóxicas si se ingieren en grandes cantidades. Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 36. Malva
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Malva",
        "nombre_cientifico": "Malva sylvestris",
        "familia_botanica": "Malvaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos",
        "habitat": "Terrenos baldíos, bordes de caminos, jardines y huertos. Prefiere suelos fértiles, húmedos y bien drenados con exposición solar.",
        "descripcion_hoja": "Hojas alternas, largamente pecioladas, de forma orbicular a reniforme, de 3 a 10 cm de diámetro, con 5-7 lóbulos palmeados poco profundos y bordes crenados. De color verde oscuro, textura suave y pubescente. Estípulas foliáceas.",
        "descripcion_tallo": "Tallos erectos o ascendentes, de 30 a 120 cm de altura, ramificados, de color verde rojizo, cubiertos de pelos simples y estrellados.",
        "descripcion_flor": "Flores axilares, agrupadas en fascículos de 2-6, de 2 a 4 cm de diámetro, con 5 pétalos de color rosado violáceo con estrías más oscuras. Florece desde primavera hasta otoño. El fruto es un esquizocarpio en forma de queso (cremocarpo).",
        "foto_real": "https://via.placeholder.com/400x300?text=Malva",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Emoliente, Antiinflamatorio, Expectorante, Digestivo",
        "receta_preparacion": "Infusión de hojas y flores: Hervir 1 cucharada de la mezcla en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para afecciones respiratorias y digestivas. En uso externo, la infusión concentrada se usa en compresas para aliviar inflamaciones cutáneas, forúnculos y hemorroides.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. Generalmente segura para uso externo. No confundir con la malva real (Malva verticillata) o la malva loca (Modiola caroliniana). Consultar a un médico para uso prolongado.",
    },
    # ---------------------------------------------------------------------------
    # 37. Manzanilla
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Manzanilla",
        "nombre_cientifico": "Matricaria chamomilla",
        "familia_botanica": "Asteraceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Atacama, Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos, Aysén",
        "habitat": "Terrenos cultivados, bordes de caminos, jardines y praderas. Prefiere suelos arenosos, bien drenados y exposición solar. Naturalizada en todo Chile.",
        "descripcion_hoja": "Hojas alternas, sésiles, 2-3 pinnatisectas, divididas en segmentos filiformes muy finos, de 2 a 6 cm de largo, de color verde claro. Textura suave y ligeramente carnosa, con aroma característico agradable.",
        "descripcion_tallo": "Tallo erecto, de 15 a 50 cm de altura, delgado, muy ramificado desde la base, de color verde claro, glabro.",
        "descripcion_flor": "Capítulos solitarios en el extremo de las ramas, de 1.5 a 2.5 cm de diámetro, con receptáculo cónico hueco (característico). Flores liguladas periféricas de color blanco y flores tubulares centrales de color amarillo intenso. Florece durante todo el año.",
        "foto_real": "https://via.placeholder.com/400x300?text=Manzanilla",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Antiespasmódico, Digestivo, Sedante suave, Antiinflamatorio, Ansiolítico",
        "receta_preparacion": "Infusión: Verter 1 taza de agua hirviendo sobre 1 cucharada de flores secas. Reposar 5-10 minutos tapado (para conservar los aceites esenciales), colar y beber 2-3 tazas al día. Ideal para cólicos digestivos, nerviosismo e insomnio leve. En uso externo para lavar ojos irritados y heridas.",
        "advertencias": "No consumir durante el embarazo (puede estimular contracciones uterinas). Personas alérgicas a las Asteráceas (ambrosía, crisantemos) pueden presentar reacciones alérgicas. No usar en niños menores de 1 año. Evitar el uso excesivo y prolongado. No conducir si se consume en altas dosis por efecto sedante.",
    },
    # ---------------------------------------------------------------------------
    # 38. Maqui
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Maqui",
        "nombre_cientifico": "Aristotelia chilensis",
        "familia_botanica": "Elaeocarpaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Bosques templados húmedos, márgenes de bosques y cursos de agua, claros y renovales. Desde el nivel del mar hasta los 800 m de altitud. Prefiere suelos húmedos y ricos en materia orgánica.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma ovada a lanceolada, de 3 a 8 cm de largo, de color verde oscuro brillante en el haz y más pálido en el envés. Bordes finamente dentados. Textura membranácea, con nervadura pinnada prominente. Las hojas nuevas son de color rojizo.",
        "descripcion_tallo": "Arbusto o árbol pequeño de 3 a 5 m de altura, con tronco de corteza lisa de color pardo claro. Ramas delgadas y flexibles, de color rojizo en la juventud.",
        "descripcion_flor": "Flores pequeñas, de 3-5 mm de diámetro, de color blanco amarillento, dispuestas en panículas axilares. Florece entre octubre y diciembre. El fruto es una baya globosa de 4-6 mm, de color negro púrpura intenso, comestible, muy rica en antioxidantes.",
        "foto_real": "https://via.placeholder.com/400x300?text=Maqui",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Antioxidante, Antiinflamatorio, Astringente, Febrífugo, Antidiarreico",
        "receta_preparacion": "Infusión de hojas y frutos: Hervir 1 cucharada de hojas secas en 1 litro de agua por 5 minutos, reposar 10 minutos y beber 2 tazas al día para fiebre y diarreas. Los frutos frescos se consumen directamente o en jugos, mermeladas y licores. El maqui seco molido se usa en batidos y como superalimento.",
        "advertencias": "No consumir durante el embarazo ni la lactancia sin consultar. En dosis elevadas puede causar estreñimiento por su efecto astringente. Las hojas en grandes cantidades pueden ser eméticas. Personas con diabetes deben monitorear sus niveles por posible efecto hipoglucemiante.",
    },
    # ---------------------------------------------------------------------------
    # 39. Matico / Pañil
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Matico, Pañil",
        "nombre_cientifico": "Buddleja globosa",
        "familia_botanica": "Scrophulariaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos",
        "habitat": "Riberas de ríos y esteros, quebradas húmedas, laderas con humedad. Desde el nivel del mar hasta los 1.500 m de altitud.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma lanceolada a elíptica, de 5 a 15 cm de largo, de color verde oscuro en el haz y densamente tomentosas (lanudas) de color blanco grisáceo en el envés. Textura rugosa, bordes dentados. Desprenden aroma resinoso al estrujarlas.",
        "descripcion_tallo": "Arbusto de 1 a 4 m de altura, con tallos erectos y ramificados, de color pardo grisáceo, con corteza fibrosa que se desprende en tiras. Ramas jóvenes de color verde claro con pubescencia.",
        "descripcion_flor": "Inflorescencias en glomérulos globosos de 1.5 a 2.5 cm de diámetro, de color amarillo intenso a anaranjado, dispuestos en panículas terminales. Flores tubulosas con 4 lóbulos. Florece entre octubre y enero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Matico",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Vulnerario, Cicatrizante, Antiinflamatorio, Digestivo, Hepático",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para problemas digestivos y hepáticos. En uso externo, la infusión concentrada se usa para lavar heridas y llagas. Las hojas frescas machacadas se aplican directamente sobre golpes y heridas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. En uso externo es seguro, suspender si aparece irritación. Consultar a un médico antes de usar internamente de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 40. Melón Reuma
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Melón Reuma",
        "nombre_cientifico": "Ecballium elaterium",
        "familia_botanica": "Cucurbitaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule",
        "habitat": "Terrenos baldíos, bordes de caminos, laderas secas y pedregosas. Prefiere suelos arenosos con exposición solar directa.",
        "descripcion_hoja": "Hojas alternas, largamente pecioladas, de forma ovado-cordada, de 5 a 15 cm de largo, de color verde grisáceo, con bordes dentados y superficie áspera y pubescente. Textura rugosa.",
        "descripcion_tallo": "Tallos postrados o trepadores, de 50 a 150 cm de largo, gruesos, suculentos, de color verde claro, cubiertos de pelos ásperos, con zarcillos simples.",
        "descripcion_flor": "Flores monoicas, axilares, de color amarillo pálido. Flores masculinas en racimos, femeninas solitarias. Corola acampanada con 5 lóbulos. Florece entre primavera y verano. El fruto es una baya oblonga de 3-5 cm, de color verde, que expulsa violentamente las semillas al madurar (dehiscencia explosiva).",
        "foto_real": "https://via.placeholder.com/400x300?text=Melon+reuma",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Purgante drástico, Antiinflamatorio, Antirreumático",
        "receta_preparacion": "Uso externo tradicional: El zumo fresco del fruto se aplica tópicamente sobre las articulaciones doloridas por reumatismo y artritis. No se recomienda su uso interno debido a su alta toxicidad. Tradicionalmente se usaba en ungüentos y linimentos.",
        "advertencias": "Planta extremadamente tóxica. NO ingerir bajo ninguna circunstancia. El zumo del fruto es un purgante drástico que puede causar irritación gastrointestinal severa, vómitos y deshidratación. Solo para uso externo. Mantener fuera del alcance de niños y mascotas. Consultar urgentemente al médico si se produce ingestión accidental.",
    },
    # ---------------------------------------------------------------------------
    # 41. Menta
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Menta",
        "nombre_cientifico": "Mentha spp.",
        "familia_botanica": "Lamiaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Atacama, Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Lugares húmedos, bordes de cursos de agua, huertos y jardines. Crece vigorosamente en suelos húmedos y fértiles, extendiéndose mediante rizomas.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma lanceolada a ovada, de 3 a 9 cm de largo, de color verde oscuro a claro, con bordes dentados. Textura rugosa, con glándulas oleíferas visibles. Desprenden un aroma intenso a mentol característico. Pecíolo corto.",
        "descripcion_tallo": "Tallos erectos, de 30 a 80 cm de altura, cuadrangulares (característico de las Lamiaceae), de color verde a púrpura, ramificados, con tendencia a emitir estolones subterráneos.",
        "descripcion_flor": "Inflorescencias en espigas terminales densas de 3 a 8 cm de largo, con verticilos de flores pequeñas de color lila a rosado o blanco. Corola bilabiada con 4 lóbulos. Florece desde fines de primavera hasta otoño.",
        "foto_real": "https://via.placeholder.com/400x300?text=Menta",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Carminativo, Antiespasmódico, Expectorante, Analgésico suave",
        "receta_preparacion": "Infusión: Verter 1 taza de agua hirviendo sobre 5-6 hojas frescas de menta. Reposar 5-8 minutos, colar y beber después de las comidas para facilitar la digestión. Ideal para cólicos estomacales, gases y náuseas. En la cocina se usa en ensaladas, sopas, salsas, postres, cócteles y tés.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. El aceite esencial de menta no debe ingerirse puro ni aplicarse en la cara de niños menores de 2 años (riesgo de laringoespasmo). Puede relajar el esfínter esofágico, empeorando el reflujo gastroesofágico. Personas con cálculos biliares deben consultar a su médico.",
    },
    # ---------------------------------------------------------------------------
    # 42. Miyaya (Estramonio)
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Miyaya, Estramonio",
        "nombre_cientifico": "Datura stramonium",
        "familia_botanica": "Solanaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Terrenos baldíos, bordes de caminos, corrales, depósitos de basura y suelos ricos en nitrógeno. Prefiere suelos arenosos y exposición solar directa.",
        "descripcion_hoja": "Hojas alternas, de forma ovada a triangular, de 5 a 20 cm de largo, de color verde oscuro, con bordes irregularmente dentados y lóbulos puntiagudos. Textura membranácea, con nervadura prominente. Desprenden olor desagradable al estrujarlas.",
        "descripcion_tallo": "Tallo erecto, de 30 a 150 cm de altura, grueso, de color verde a púrpura, ramificado de forma dicotómica, hueco en los entrenudos.",
        "descripcion_flor": "Flores solitarias, axilares, erectas, de 6 a 10 cm de largo, con corola infundibuliforme (en forma de embudo) de color blanco, con 5 dientes apicales. Cáliz tubular, pentagonal. Florece entre primavera y otoño. El fruto es una cápsula espinosa ovoide que se abre en 4 valvas.",
        "foto_real": "https://via.placeholder.com/400x300?text=Miyaya",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Antiespasmódico, Analgésico, Antiasmático (uso controlado)",
        "receta_preparacion": "Tradicionalmente las hojas secas se fumaban en pequeñas cantidades para aliviar el asma y los espasmos bronquiales. El uso debe ser estrictamente supervisado por un profesional de la salud. En homeopatía se usa en diluciones extremas.",
        "advertencias": "Planta altamente tóxica por su contenido de alcaloides tropánicos (escopolamina, hiosciamina, atropina). Su consumo puede causar delirio, alucinaciones, taquicardia, midriasis, hipertermia y muerte. NO AUTOMEDICARSE. Mantener fuera del alcance de niños y mascotas. Prohibida su venta sin receta médica.",
    },
    # ---------------------------------------------------------------------------
    # 43. Naranjo (Naranjo agrio)
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Naranjo",
        "nombre_cientifico": "Citrus aurantium",
        "familia_botanica": "Rutaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule",
        "habitat": "Cultivado en huertos y jardines de la zona central. Prefiere climas templados, suelos profundos, fértiles y bien drenados con exposición solar directa.",
        "descripcion_hoja": "Hojas simples, alternas, de forma elíptica a ovada, de 5 a 10 cm de largo, de color verde oscuro brillante, textura coriácea con glándulas oleíferas translúcidas. Peciolo alado (con alas estrechas). Aroma cítrico intenso al estrujarlas.",
        "descripcion_tallo": "Árbol de 3 a 8 m de altura, con tronco de corteza lisa de color pardo claro. Ramas con espinas axilares agudas. Copa redondeada y densa.",
        "descripcion_flor": "Flores solitarias o en pequeños racimos axilares, de 2 a 3 cm de diámetro, de color blanco intenso (azahar), con 5 pétalos carnosos y numerosos estambres. Muy fragantes. Florece entre septiembre y noviembre. El fruto es un hesperidio (naranja) de color naranja intenso, de sabor amargo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Naranjo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Sedante, Ansiolítico, Digestivo, Carminativo",
        "receta_preparacion": "Infusión de hojas y flores (azahar): Verter 1 taza de agua hirviendo sobre 1 cucharada de hojas secas o 2 cucharadas de flores frescas. Reposar 10 minutos, colar y beber 1 taza antes de dormir para conciliar el sueño y calmar los nervios. La cáscara del fruto se usa en infusiones digestivas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. El aceite esencial puede causar fotosensibilidad. Evitar el consumo excesivo de la cáscara por su contenido de sinefrina. Interactúa con algunos medicamentos (consultar al médico). No confundir con el naranjo dulce (Citrus sinensis).",
    },
    # ---------------------------------------------------------------------------
    # 44. Nalca / Pangue
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Nalca, Pangue",
        "nombre_cientifico": "Gunnera tinctoria",
        "familia_botanica": "Gunneraceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Lugares húmedos y pantanosos, riberas de ríos y lagos, laderas con filtraciones de agua. Desde el nivel del mar hasta los 500 m de altitud.",
        "descripcion_hoja": "Hojas enormes, de 50 a 150 cm de diámetro, de forma orbicular a reniforme, palmadamente lobuladas con bordes dentados. De color verde intenso, textura rugosa y coriácea. Peciolos largos (hasta 2 m), gruesos y acanalados, con espinas. La planta tiene una relación simbiótica con cianobacterias fijadoras de nitrógeno.",
        "descripcion_tallo": "Rizoma grande, grueso y carnoso, de color pardo oscuro, que se extiende horizontalmente. Los peciolos (nalcas) emergen directamente del rizoma. No tiene tallos aéreos verdaderos.",
        "descripcion_flor": "Inflorescencias en panículas densas de 30 a 60 cm de largo, de color verde amarillento a rojizo. Flores pequeñas, sin pétalos, con cáliz tubular. Florece entre noviembre y enero. El fruto es una drupa pequeña de color anaranjado a rojo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Nalca",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Astringente, Depurativo, Diurético",
        "receta_preparacion": "Los peciolos (nalcas) se pelan y se consumen frescos en ensaladas con sal y limón, o cocidos en mermeladas y postres. La infusión de rizoma se prepara hirviendo 30 g de rizoma troceado en 1 litro de agua por 15 minutos; se usa para lavar heridas y como astringente. Tradicionalmente se usa para el mal de altura.",
        "advertencias": "No consumir durante el embarazo ni la lactancia sin consultar. Los peciolos frescos son ácidos y pueden dañar el esmalte dental si se consumen en exceso. No confundir con Gunnera magellanica, que es más pequeña. Recolectar solo de lugares no contaminados.",
    },
    # ---------------------------------------------------------------------------
    # 45. Natre
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Natre",
        "nombre_cientifico": "Solanum ligustrinum",
        "familia_botanica": "Solanaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Matorrales esclerófilos, laderas de cerros, bordes de caminos y quebradas. Desde el nivel del mar hasta los 1.500 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, de forma lanceolada a oblonga, de 2 a 6 cm de largo, de color verde oscuro brillante, textura coriácea, con bordes enteros y ápice agudo. Nervadura pinnada prominente en el envés.",
        "descripcion_tallo": "Arbusto de 1 a 3 m de altura, muy ramificado, con tallos leñosos delgados, de color verde amarillento a pardo claro. Corteza lisa.",
        "descripcion_flor": "Flores en cimas axilares, de 1.5 a 2 cm de diámetro, con corola rotácea de color blanco a lila pálido, con 5 lóbulos y un cono central de anteras amarillas. Florece entre noviembre y marzo. El fruto es una baya globosa de 8-12 mm, de color rojo brillante (tóxica).",
        "foto_real": "https://via.placeholder.com/400x300?text=Natre",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Analgésico, Antiinflamatorio, Antipirético, Depurativo",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 litro de agua por 10 minutos. Reposar 10 minutos, colar y beber 1 taza 2 veces al día para resfriados, fiebre y dolores musculares. En uso externo, la decocción se aplica en compresas para aliviar contusiones y dolores reumáticos.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Los frutos rojos son tóxicos y no deben ingerirse. No exceder las dosis recomendadas. Contraindicado en personas con insuficiencia renal o hepática. Consultar a un médico antes de usar.",
    },
    # ---------------------------------------------------------------------------
    # 46. Nogal
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Nogal",
        "nombre_cientifico": "Juglans regia",
        "familia_botanica": "Juglandaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Cultivado en huertos y terrenos agrícolas; naturalizado en quebradas y laderas húmedas. Prefiere suelos profundos, fértiles y bien drenados.",
        "descripcion_hoja": "Hojas compuestas, imparipinnadas, de 15 a 30 cm de largo, con 5-9 folíolos de forma ovada a elíptica, de 6 a 15 cm de largo, de color verde claro, textura membranácea. Desprenden aroma característico al estrujarlas. El folíolo terminal es el más grande.",
        "descripcion_tallo": "Árbol de 10 a 25 m de altura, con tronco robusto de corteza lisa y gris plateada cuando joven, que se vuelve agrietada y parda con la edad. Copa ancha y redondeada.",
        "descripcion_flor": "Flores monoicas: masculinas en amentos colgantes de 5-15 cm; femeninas en grupos de 2-5 en el extremo de las ramas. Florece entre octubre y noviembre. El fruto es una drupa (nuez) con cáscara verde carnosa (ruezno) que se abre al madurar.",
        "foto_real": "https://via.placeholder.com/400x300?text=Nogal",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Astringente, Antiséptico, Cicatrizante, Antiparasitario",
        "receta_preparacion": "Decocción de hojas: Hervir un puñado de hojas secas en 1 litro de agua por 15 minutos. En uso externo, aplicar en compresas para tratar heridas, eccemas, hemorroides y caída del cabello. En uso interno (con precaución), 1 taza al día para diarreas leves. Las nueces son altamente nutritivas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. Las hojas contienen juglona, que puede ser tóxica en dosis elevadas. No usar internamente por períodos prolongados. La cáscara verde del fruto puede manchar la piel. Personas alérgicas a los frutos secos deben evitar su uso.",
    },
    # ---------------------------------------------------------------------------
    # 47. Ñanco lahuen
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Ñanco lahuen",
        "nombre_cientifico": "Valeriana carnosa",
        "familia_botanica": "Caprifoliaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Bosques templados húmedos, praderas de montaña, vegas y bordes de cursos de agua. Desde el nivel del mar hasta los 1.000 m de altitud.",
        "descripcion_hoja": "Hojas basales en roseta, de forma espatulada a oblonga, de 5 a 15 cm de largo, de color verde claro, carnosas (de ahí el epíteto 'carnosa'), con bordes enteros o sinuados. Hojas caulinares opuestas, reducidas, sésiles.",
        "descripcion_tallo": "Tallo floral erecto, de 20 a 50 cm de altura, cilíndrico, hueco, de color verde claro, con nudos prominentes. Rizoma corto y grueso con numerosas raíces fibrosas de olor característico a valeriana.",
        "descripcion_flor": "Inflorescencias en corimbos o panículas terminales densas, con flores pequeñas de color blanco a rosado pálido, de 3-5 mm de diámetro. Corola infundibuliforme con 5 lóbulos. Florece entre diciembre y febrero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Nanco+lahuen",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Sedante, Ansiolítico, Antiespasmódico, Relajante muscular",
        "receta_preparacion": "Infusión de raíz: Hervir 1 cucharadita de raíz seca troceada en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza antes de acostarse para tratar el insomnio, la ansiedad y los nervios. También se usa en baños relajantes hirviendo 50 g de raíz en 2 litros de agua.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Puede causar somnolencia; no conducir ni operar maquinaria después de consumirla. No combinar con alcohol u otros depresores del sistema nervioso. El uso prolongado puede causar dependencia. Evitar en personas con enfermedades hepáticas.",
    },
    # ---------------------------------------------------------------------------
    # 48. Orégano
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Orégano",
        "nombre_cientifico": "Origanum majorana",
        "familia_botanica": "Lamiaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Cultivado en huertos y jardines, naturalizado en laderas secas y soleadas. Prefiere suelos calcáreos, bien drenados y exposición solar directa.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma ovada a elíptica, de 1 a 3 cm de largo, de color verde grisáceo, cubiertas de fina pubescencia. Textura suave, bordes enteros. Desprenden un aroma intenso y característico, más dulce que el orégano común (Origanum vulgare).",
        "descripcion_tallo": "Tallos erectos o ascendentes, de 20 a 50 cm de altura, cuadrangulares (característico de Lamiaceae), muy ramificados, de color verde a púrpura, con pubescencia blanquecina.",
        "descripcion_flor": "Inflorescencias en espigas terminales densas, con flores pequeñas de color blanco a lila pálido, dispuestas en verticilos. Corola bilabiada. Brácteas imbricadas de color verde claro. Florece entre diciembre y abril.",
        "foto_real": "https://via.placeholder.com/400x300?text=Oregano",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Carminativo, Antiséptico, Expectorante, Antiespasmódico",
        "receta_preparacion": "Infusión: Verter 1 taza de agua hirviendo sobre 1 cucharadita de hojas secas de orégano. Reposar 5-8 minutos, colar y beber después de las comidas para facilitar la digestión y aliviar cólicos. En la cocina, es un condimento esencial para pizzas, salsas, carnes, guisos y ensaladas. Aceite de orégano: macerar hojas en aceite de oliva.",
        "advertencias": "No consumir durante el embarazo en dosis medicinales (uso culinario moderado es seguro). El aceite esencial concentrado puede irritar la piel y las mucosas. Evitar en personas alérgicas a las Lamiaceae (menta, albahaca, etc.). Puede interferir con medicamentos anticoagulantes.",
    },
    # ---------------------------------------------------------------------------
    # 49. Ortiga
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Ortiga",
        "nombre_cientifico": "Urtica dioica",
        "familia_botanica": "Urticaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Atacama, Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Terrenos baldíos, bordes de caminos, jardines, lugares húmedos y ricos en nitrógeno. Crece en todo tipo de suelos, desde el nivel del mar hasta los 2.000 m de altitud.",
        "descripcion_hoja": "Hojas opuestas, de forma ovada a lanceolada, de 5 a 15 cm de largo, de color verde oscuro, con bordes profundamente aserrados. Textura membranácea, cubierta de pelos urticantes (tricomas) que liberan histamina y ácido fórmico al contacto. Nervadura pinnada prominente.",
        "descripcion_tallo": "Tallos erectos, de 30 a 150 cm de altura, cuadrangulares (o estriados), de color verde a púrpura, cubiertos de pelos urticantes y no urticantes. Rizomas estoloníferos extensos.",
        "descripcion_flor": "Flores unisexuales, pequeñas, de color verde amarillento, dispuestas en inflorescencias colgantes (amentos) axilares. Plantas generalmente dioicas (flores masculinas y femeninas en plantas separadas). Florece durante casi todo el año.",
        "foto_real": "https://via.placeholder.com/400x300?text=Ortiga",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Antiinflamatorio, Antianémico, Antialérgico",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 taza de agua por 5 minutos (las hojas secas no pican). Reposar 10 minutos, colar y beber 2-3 tazas al día para alergias, gota, reumatismo y como depurativo. También se usa en sopas (ortiga fresca cocida) y ensaladas. En uso externo, el cocimiento se aplica sobre el cuero cabelludo para la caspa.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. La planta fresca causa urticaria severa al contacto; manipular con guantes. Las hojas secas pierden el poder urticante. Contraindicada en personas con edema por insuficiencia cardíaca o renal. Puede interferir con medicamentos diuréticos y anticoagulantes.",
    },
    # ---------------------------------------------------------------------------
    # 50. Paico
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Paico",
        "nombre_cientifico": "Dysphania ambrosioides",
        "familia_botanica": "Amaranthaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Atacama, Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Terrenos baldíos, bordes de caminos, huertos y jardines. Prefiere suelos arenosos, secos y exposición solar directa.",
        "descripcion_hoja": "Hojas alternas, de forma oblonga a lanceolada, de 3 a 10 cm de largo, de color verde amarillento, con bordes dentados o lobulados. Textura membranácea, con glándulas oleíferas translúcidas que desprenden un aroma intenso, alcanforado y penetrante característico.",
        "descripcion_tallo": "Tallo erecto, de 30 a 100 cm de altura, estriado, ramificado, de color verde claro a rojizo, glabro o con fina pubescencia.",
        "descripcion_flor": "Inflorescencias en panículas terminales y axilares, con numerosas flores pequeñas de color verde amarillento, agrupadas en glomérulos. Sin pétalos evidentes. Florece durante casi todo el año.",
        "foto_real": "https://via.placeholder.com/400x300?text=Paico",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Antiparasitario, Digestivo, Carminativo, Emenagogo",
        "receta_preparacion": "Infusión: Hervir 1 cucharadita de hojas secas en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza en ayunas por 3-5 días para eliminar parásitos intestinales (lombrices). Tradicionalmente se combina con ajenjo y éter. El 'agua de paico' se usa para cólicos menstruales y digestivos.",
        "advertencias": "No consumir durante el embarazo (es abortivo) ni la lactancia. El aceite esencial contiene ascaridol, altamente tóxico en dosis elevadas. No exceder las dosis recomendadas. Contraindicado en personas con enfermedades hepáticas, renales o neurológicas. No usar por más de 5 días consecutivos.",
    },
    # ---------------------------------------------------------------------------
    # 51. Palqui
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Palqui",
        "nombre_cientifico": "Cestrum parqui",
        "familia_botanica": "Solanaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Matorrales esclerófilos, bordes de caminos, quebradas y laderas de cerros. Desde el nivel del mar hasta los 1.200 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, de forma lanceolada a elíptica, de 5 a 12 cm de largo, de color verde claro a medio, textura membranácea, con bordes enteros. Desprenden olor desagradable al estrujarlas, similar al de la hierba mora.",
        "descripcion_tallo": "Arbusto de 1 a 3 m de altura, erecto, muy ramificado, con tallos leñosos delgados de color pardo claro a grisáceo. Ramas jóvenes de color verde claro.",
        "descripcion_flor": "Inflorescencias en panículas terminales y axilares, con flores tubulosas de 2 a 3 cm de largo, de color amarillo verdoso a crema, con 5 lóbulos. Desprenden un aroma intenso y dulzón durante la noche. Florece entre primavera y otoño. El fruto es una baya globosa de color negro violáceo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Palqui",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Febrífugo, Antipirético, Antiinflamatorio, Analgésico",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 litro de agua por 10 minutos. Reposar 10 minutos, colar y beber 1 taza 2-3 veces al día para bajar la fiebre. En uso externo, la decocción concentrada se usa en compresas para aliviar dolores reumáticos y musculares.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Los frutos (bayas negras) son tóxicos y no deben ingerirse. No exceder las dosis recomendadas. En dosis elevadas puede causar vómitos, diarrea y alteraciones neurológicas. Mantener fuera del alcance de niños y mascotas.",
    },
    # ---------------------------------------------------------------------------
    # 52. Palto
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Palto",
        "nombre_cientifico": "Persea americana",
        "familia_botanica": "Lauraceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule",
        "habitat": "Cultivado extensamente en huertos frutales de la zona central. Prefiere climas templados, suelos profundos, fértiles y bien drenados, protegido de heladas.",
        "descripcion_hoja": "Hojas simples, alternas, de forma elíptica a obovada, de 8 a 20 cm de largo, de color verde oscuro brillante en el haz y más pálido en el envés. Textura coriácea, con bordes enteros, nervadura pinnada prominente. Desprenden aroma anisado al estrujarlas.",
        "descripcion_tallo": "Árbol de 6 a 20 m de altura, con tronco de corteza rugosa de color pardo grisáceo. Copa densa y redondeada. Ramas extendidas.",
        "descripcion_flor": "Flores pequeñas, de 5-10 mm, de color verde amarillento, dispuestas en panículas terminales. Presentan un mecanismo de floración sincronizada (dicogamia protogínea). Florece entre octubre y diciembre. El fruto es una baya grande, piriforme o globosa (palta/aguacate), de piel verde a oscura.",
        "foto_real": "https://via.placeholder.com/400x300?text=Palto",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Emoliente, Hipotensor, Antiinflamatorio",
        "receta_preparacion": "Infusión de hojas: Hervir 2-3 hojas frescas en 1 taza de agua por 5 minutos. Reposar 10 minutos y beber 1 taza después de las comidas para problemas digestivos. El aceite de palta se usa para la piel y el cabello. La pulpa del fruto se consume fresca en ensaladas, guacamole y cosmética natural.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. Las hojas pueden causar toxicidad en grandes cantidades (contienen persina). La semilla no es comestible. No confundir con el laurel chileno (Laurelia sempervirens). Consultar a un médico para uso prolongado.",
    },
    # ---------------------------------------------------------------------------
    # 53. Pata de vaca
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Pata de vaca",
        "nombre_cientifico": "Bauhinia candicans",
        "familia_botanica": "Fabaceae",
        "origen": "NATIVA",
        "zona_macro": "NORTE",
        "regiones": "Antofagasta, Atacama, Coquimbo",
        "habitat": "Laderas áridas y semiáridas de la precordillera y valles transversales. Desde los 500 hasta los 2.000 m de altitud. Crece en suelos pedregosos con escasa precipitación.",
        "descripcion_hoja": "Hojas simples, alternas, de forma bilobada (como pezuña de vaca), de 3 a 8 cm de largo y ancho, de color verde grisáceo, textura coriácea. Presentan 7-9 nervaduras principales que parten de la base. Estípulas caducas.",
        "descripcion_tallo": "Árbol pequeño o arbusto de 2 a 6 m de altura, con tronco de corteza agrietada de color pardo oscuro. Ramas tortuosas, a veces con espinas.",
        "descripcion_flor": "Flores grandes, de 4 a 7 cm de diámetro, de color blanco puro a crema, con 5 pétalos anchos y oblongos, dispuestas en racimos terminales cortos. Numerosos estambres largos. Florece entre octubre y diciembre. El fruto es una legumbre plana y leñosa de 10-20 cm.",
        "foto_real": "https://via.placeholder.com/400x300?text=Pata+de+vaca",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Hipoglucemiante, Diurético, Depurativo",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 taza de agua por 10 minutos. Reposar 10 minutos, colar y beber 2 tazas al día para ayudar a controlar los niveles de glucosa en sangre. Tradicionalmente usada para la diabetes mellitus tipo 2 y como depurativo renal.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Consultar con un médico antes de usar para tratar la diabetes, ya que puede potenciar el efecto de los medicamentos hipoglucemiantes. Monitorear los niveles de glucosa regularmente. No exceder las dosis recomendadas.",
    },
    # ---------------------------------------------------------------------------
    # 54. Peumo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Peumo",
        "nombre_cientifico": "Cryptocarya alba",
        "familia_botanica": "Lauraceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Bosques esclerófilos de la zona central, laderas de cerros, quebradas. Desde el nivel del mar hasta los 1.200 m de altitud.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma elíptica a ovada, de 3 a 8 cm de largo, de color verde oscuro brillante en el haz y glaucas (blanquecinas) en el envés, con nervadura reticulada prominente. Textura coriácea, con bordes enteros. Desprenden aroma característico al estrujarlas.",
        "descripcion_tallo": "Árbol siempreverde de 10 a 20 m de altura, con tronco de corteza rugosa de color pardo grisáceo. Copa densa y redondeada. Ramas robustas.",
        "descripcion_flor": "Flores pequeñas, de 3-5 mm de diámetro, de color blanco amarillento, dispuestas en panículas axilares y terminales. Perianto con 6 tépalos. Florece entre octubre y diciembre. El fruto es una drupa ovoide de 1.5-2 cm, de color rojo brillante al madurar, comestible.",
        "foto_real": "https://via.placeholder.com/400x300?text=Peumo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Colagogo, Antirreumático",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza después de las comidas para problemas hepáticos y digestivos. Los frutos rojos son comestibles y se usan para preparar mermeladas y licores. En uso externo, la decocción se usa para aliviar dolores reumáticos.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Los frutos en exceso pueden causar estreñimiento. No exceder las dosis recomendadas. Consultar a un médico antes de usar de forma prolongada. No confundir con otras especies del género Cryptocarya.",
    },
    # ---------------------------------------------------------------------------
    # 55. Pichi / Pichi Romero
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Pichi, Pichi Romero",
        "nombre_cientifico": "Fabiana imbricata",
        "familia_botanica": "Solanaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Laderas de cerros, praderas secas, claros de bosques esclerófilos y esteparios. Desde el nivel del mar hasta los 1.000 m de altitud.",
        "descripcion_hoja": "Hojas diminutas, de 2 a 6 mm de largo, de forma linear a escuamiforme, imbricadas (como tejas), de color verde grisáceo, densamente dispuestas a lo largo de los tallos. Textura coriácea. Dan a la planta un aspecto similar al del romero, de ahí su nombre.",
        "descripcion_tallo": "Arbusto erecto de 1 a 3 m de altura, muy ramificado, con tallos leñosos delgados, erectos, de color pardo grisáceo, con corteza que se desprende en tiras.",
        "descripcion_flor": "Flores solitarias, axilares, tubulosas, de 1.5 a 2 cm de largo, de color blanco a lila pálido, con corola infundibuliforme y 5 lóbulos. Florece entre noviembre y enero. El fruto es una cápsula pequeña con numerosas semillas.",
        "foto_real": "https://via.placeholder.com/400x300?text=Pichi",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Digestivo, Hepático, Depurativo",
        "receta_preparacion": "Infusión de hojas y tallos: Hervir 1 cucharada de la planta seca (ramas con hojas) en 1 litro de agua por 10 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para trastornos digestivos, hepáticos y renales. Tradicionalmente usado para problemas de vejiga y como depurativo.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. Por su efecto diurético, mantener una adecuada hidratación. Contraindicado en personas con insuficiencia renal. Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 56. Pimiento / Molle
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Pimiento, Molle",
        "nombre_cientifico": "Schinus areira",
        "familia_botanica": "Anacardiaceae",
        "origen": "NATIVA",
        "zona_macro": "NORTE",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Atacama, Coquimbo, Valparaíso, Metropolitana",
        "habitat": "Valles y laderas de la precordillera y cordillera de los Andes, desde los 500 hasta los 3.000 m de altitud. También cultivado como ornamental en parques y calles.",
        "descripcion_hoja": "Hojas compuestas, alternas, imparipinnadas, con 5-15 folíolos de forma linear a lanceolada, de 2 a 5 cm de largo, de color verde claro, con bordes enteros o finamente dentados. Textura coriácea, con glándulas oleíferas translúcidas. Aroma resinoso característico.",
        "descripcion_tallo": "Árbol dioico de 5 a 15 m de altura, con tronco de corteza rugosa de color pardo oscuro. Ramas colgantes (péndulas), dando una apariencia llorona. Copa densa y redondeada.",
        "descripcion_flor": "Flores pequeñas, de 3-4 mm, de color blanco amarillento, dispuestas en panículas colgantes de 10 a 20 cm de largo. Plantas dioicas. Florece entre octubre y diciembre. El fruto es una drupa globosa de 5-7 mm, de color rosa a rojo brillante, con aroma y sabor a pimienta.",
        "foto_real": "https://via.placeholder.com/400x300?text=Pimiento",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Carminativo, Antiséptico, Expectorante, Analgésico",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza después de las comidas. Los frutos (pimienta rosada) se usan como condimento. En uso externo, la decocción de corteza se usa en baños para aliviar dolores reumáticos y musculares.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Los frutos pueden causar reacciones alérgicas en personas sensibles al mango, pistacho o hiedra (familia Anacardiaceae). El contacto con la savia puede causar dermatitis en personas predispuestas. No confundir con el pimiento (Capsicum).",
    },
    # ---------------------------------------------------------------------------
    # 57. Pingo-Pingo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Pingo-Pingo",
        "nombre_cientifico": "Ephedra chilensis",
        "familia_botanica": "Ephedraceae",
        "origen": "NATIVA",
        "zona_macro": "NORTE",
        "regiones": "Antofagasta, Atacama, Coquimbo",
        "habitat": "Laderas áridas y semiáridas de la precordillera y cordillera de los Andes, desde los 500 hasta los 3.500 m de altitud. Crece en suelos arenosos y pedregosos con extrema aridez.",
        "descripcion_hoja": "Hojas reducidas a escamas membranáceas diminutas, de 1-3 mm, opuestas o verticiladas, de color verde claro a pardo, que rodean los nudos del tallo. La función fotosintética es realizada por los tallos verdes.",
        "descripcion_tallo": "Arbusto de 50 a 150 cm de altura, con tallos erectos o ascendentes, finamente estriados, de color verde claro a grisáceo, con nudos engrosados. Ramificación abundante, dando aspecto denso. Los tallos son fotosintéticos y contienen el alcaloide efedrina.",
        "descripcion_flor": "Plantas dioicas. Estróbilos (conos) masculinos y femeninos en plantas separadas, pequeños, de 3-5 mm, de color amarillo verdoso. Los conos femeninos producen semillas rodeadas por un arilo carnoso rojo (falso fruto). Florece entre agosto y noviembre.",
        "foto_real": "https://via.placeholder.com/400x300?text=Pingo-pingo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Estimulante, Broncodilatador, Descongestionante, Hipotensor",
        "receta_preparacion": "Infusión de tallos: Hervir 1 cucharadita de tallos secos en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza 1-2 veces al día para afecciones respiratorias y alergias. Tradicionalmente usado por los atacameños para el mal de altura y la fatiga.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Contiene efedrina, alcaloide con efectos estimulantes que puede causar taquicardia, hipertensión, insomnio y ansiedad. Contraindicado en personas con enfermedades cardiovasculares, hipertensión, hipertiroidismo o glaucoma. No exceder las dosis recomendadas.",
    },
    # ---------------------------------------------------------------------------
    # 58. Quebracho Blanco / Sen Chileno
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Quebracho Blanco, Sen Chileno",
        "nombre_cientifico": "Senna stipulacea",
        "familia_botanica": "Fabaceae",
        "origen": "NATIVA",
        "zona_macro": "NORTE",
        "regiones": "Arica y Parinacota, Tarapacá, Antofagasta, Atacama",
        "habitat": "Valles y laderas de la precordillera andina, desde los 500 hasta los 2.500 m de altitud. Crece en suelos arenosos y pedregosos con escasa precipitación.",
        "descripcion_hoja": "Hojas compuestas, alternas, paripinnadas, con 6-12 pares de folíolos de forma oblonga a elíptica, de 1 a 3 cm de largo, de color verde grisáceo, textura coriácea. Presentan una glándula entre los folíolos del pecíolo.",
        "descripcion_tallo": "Arbusto de 1 a 3 m de altura, erecto, ramificado, con tallos leñosos de color pardo claro a grisáceo. Corteza agrietada. Ramas jóvenes de color verde.",
        "descripcion_flor": "Flores de 2 a 3 cm de diámetro, de color amarillo intenso, dispuestas en racimos axilares y terminales. Corola con 5 pétalos desiguales. Florece entre noviembre y febrero. El fruto es una legumbre (vaina) de 5-10 cm, aplanada, de color pardo oscuro.",
        "foto_real": "https://via.placeholder.com/400x300?text=Quebracho+blanco",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Laxante, Purgante suave, Digestivo, Hepático",
        "receta_preparacion": "Infusión de hojas y frutos: Hervir 1 cucharadita de hojas secas en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza en ayunas para tratar el estreñimiento ocasional. Tradicionalmente usado como laxante suave en la medicina andina.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. El uso prolongado puede causar dependencia laxante y alteraciones electrolíticas. No exceder las dosis recomendadas. Contraindicado en personas con obstrucción intestinal, enfermedad inflamatoria intestinal o dolor abdominal de causa desconocida.",
    },
    # ---------------------------------------------------------------------------
    # 59. Quillay
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Quillay",
        "nombre_cientifico": "Quillaja saponaria",
        "familia_botanica": "Quillajaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Bosques esclerófilos, laderas de cerros y quebradas de la zona central. Desde el nivel del mar hasta los 1.500 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, de forma elíptica a obovada, de 3 a 6 cm de largo, de color verde oscuro brillante, textura coriácea, con bordes dentados en la parte superior. Nervadura pinnada prominente. Estípulas caducas.",
        "descripcion_tallo": "Árbol siempreverde de 10 a 20 m de altura, con tronco de corteza lisa de color gris claro a plateado. Copa redondeada. Ramas extendidas, de color rojizo en la juventud.",
        "descripcion_flor": "Flores de 1 a 1.5 cm de diámetro, de color blanco cremoso, dispuestas en umbelas axilares de 3-6 flores. Corola con 5 pétalos y 5 sépalos. Florece entre noviembre y enero. El fruto es un folículo (vaina) de color pardo, con semillas aladas.",
        "foto_real": "https://via.placeholder.com/400x300?text=Quillay",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Expectorante, Detergente, Antiséptico, Antiinflamatorio",
        "receta_preparacion": "Infusión de corteza: Hervir 1 cucharada de astillas de corteza en 1 taza de agua por 10 minutos. Reposar 10 minutos, colar y beber 1-2 tazas al día para la tos y bronquitis. En uso externo, la decocción de corteza se usa como champú natural, para lavar heridas y para eccemas. La corteza produce espuma por su alto contenido de saponinas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. En dosis elevadas puede causar irritación gastrointestinal, vómitos y diarrea. Las saponinas pueden irritar las mucosas. No exceder las dosis recomendadas. Mantener fuera del alcance de los niños. Consultar a un médico antes de usar.",
    },
    # ---------------------------------------------------------------------------
    # 60. Quilo / Mollaco / Voqui
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Quilo, Mollaco, Voqui",
        "nombre_cientifico": "Muehlenbeckia hastulata",
        "familia_botanica": "Polygonaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos",
        "habitat": "Matorrales, bordes de caminos, laderas de cerros, quebradas y renovales de bosque. Desde el nivel del mar hasta los 1.200 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, de forma hastada (como punta de flecha) o triangular, de 2 a 7 cm de largo, de color verde claro a medio, textura membranácea. Presentan una ócrea (vaina) membranosa en la base del pecíolo, característica de las Polygonaceae.",
        "descripcion_tallo": "Tallos largos, delgados, trepadores o enredados (voqui), de 2 a 6 m de largo, de color verde a pardo rojizo, leñosos en la base, con nudos engrosados.",
        "descripcion_flor": "Flores pequeñas, de 3-4 mm, de color blanco verdoso, dispuestas en racimos axilares delgados. Perianto con 5 tépalos. Florece entre octubre y febrero. El fruto es un aquenio pequeño, negro brillante, envuelto por el perianto carnoso y blanco que se vuelve comestible.",
        "foto_real": "https://via.placeholder.com/400x300?text=Quilo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Antipirético, Digestivo",
        "receta_preparacion": "Infusión de hojas y tallos: Hervir 1 cucharada de la planta seca en 1 litro de agua por 10 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para resfriados, fiebre y como depurativo. En uso externo, la decocción concentrada se usa para lavar heridas y aliviar inflamaciones cutáneas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. No se han reportado toxicidades significativas con uso moderado. Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 61. Quinchamalí
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Quinchamalí",
        "nombre_cientifico": "Quinchamalium chilense",
        "familia_botanica": "Schoepfiaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos",
        "habitat": "Praderas húmedas, bordes de caminos, laderas de cerros con humedad. Desde el nivel del mar hasta los 1.000 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, lineares a muy estrechas, de 1 a 4 cm de largo, de color verde claro, sésiles, con bordes enteros. Textura membranácea. Dispuestas densamente a lo largo de los tallos.",
        "descripcion_tallo": "Tallos erectos, delgados, de 15 a 40 cm de altura, simples o ramificados, de color verde claro, estriados longitudinalmente.",
        "descripcion_flor": "Inflorescencias terminales en cabezuelas globosas de 1-2 cm de diámetro, rodeadas por brácteas de color amarillo intenso a anaranjado (que a menudo se confunden con pétalos). Las verdaderas flores son pequeñas, tubulosas, de color amarillo verdoso. Florece entre noviembre y marzo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Quinchamali",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Hepático, Digestivo",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de la planta seca (tallos y brácteas) en 1 taza de agua por 10 minutos. Reposar 10 minutos, colar y beber 2 tazas al día para problemas hepáticos y renales. Tradicionalmente usado por el pueblo mapuche para trastornos digestivos y como depurativo.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. No se han reportado toxicidades significativas, pero se recomienda uso moderado. Consultar a un profesional de la salud antes de usar.",
    },
    # ---------------------------------------------------------------------------
    # 62. Quintral
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Quintral",
        "nombre_cientifico": "Tristerix corymbosus",
        "familia_botanica": "Loranthaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos",
        "habitat": "Parásito sobre ramas de árboles, especialmente sobre especies nativas como el quillay, el espino, el peumo y el boldo. Desde el nivel del mar hasta los 1.000 m de altitud.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma elíptica a ovada, de 3 a 7 cm de largo, de color verde amarillento a verde oscuro, textura coriácea, con bordes enteros. Presentan 3-5 nervaduras longitudinales paralelas.",
        "descripcion_tallo": "Tallos leñosos, articulados, de color pardo verdoso, de 30 a 100 cm de largo, que crecen sobre las ramas del árbol hospedero. Se fijan mediante haustorios que penetran en los tejidos del hospedero.",
        "descripcion_flor": "Flores tubulares de 3 a 5 cm de largo, de color rojo intenso a anaranjado, con 4-6 pétalos recurvados que exponen los estambres y el estilo. Dispuestas en racimos terminales (corimbos). Florece entre octubre y marzo. El fruto es una baya elipsoide de color verde amarillento, pegajosa.",
        "foto_real": "https://via.placeholder.com/400x300?text=Quintral",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Colagogo, Laxante suave",
        "receta_preparacion": "Infusión de hojas y tallos: Hervir 1 cucharada de la planta seca en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza después de las comidas principales para problemas hepáticos y digestivos. Tradicionalmente se usa para tratar la ictericia y trastornos de la vesícula.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Las bayas son tóxicas y no deben ingerirse. No exceder las dosis recomendadas. Identificar correctamente la especie, ya que otros quintrales pueden ser tóxicos. Consultar a un médico antes de usar.",
    },
    # ---------------------------------------------------------------------------
    # 63. Radal
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Radal",
        "nombre_cientifico": "Lomatia hirsuta",
        "familia_botanica": "Proteaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Bosques templados húmedos, laderas de cerros y riberas de ríos. Desde el nivel del mar hasta los 800 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, de forma ovada a elíptica, de 4 a 12 cm de largo, de color verde oscuro brillante en el haz y pubescentes (peludas) de color rojizo en el envés. Textura coriácea, con bordes dentados. Nervadura pinnada prominente. Pecíolo corto y grueso.",
        "descripcion_tallo": "Árbol de 5 a 15 m de altura, con tronco de corteza rugosa de color pardo grisáceo, con lenticelas prominentes. Ramas jóvenes cubiertas de una densa pubescencia rojiza (de ahí 'hirsuta').",
        "descripcion_flor": "Inflorescencias en racimos axilares de 5 a 12 cm de largo, con flores de color blanco cremoso a amarillo pálido, dispuestas en pares. Cáliz tubuloso-curvado. Florece entre diciembre y febrero. El fruto es un folículo leñoso de 3-6 cm, de color pardo, con semillas aladas.",
        "foto_real": "https://via.placeholder.com/400x300?text=Radal",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Expectorante, Antiséptico",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 litro de agua por 5 minutos. Reposar 10 minutos, colar y beber 2 tazas al día después de las comidas para problemas hepáticos y digestivos. En uso externo, la decocción de la corteza se usa para lavar heridas y como antiséptico.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. Las semillas no son comestibles. Su madera es muy apreciada en ebanistería. Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 64. Rica-Rica / Kore
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Rica-Rica, Kore",
        "nombre_cientifico": "Acantholippia deserticola",
        "familia_botanica": "Verbenaceae",
        "origen": "NATIVA",
        "zona_macro": "NORTE",
        "regiones": "Antofagasta, Atacama, Coquimbo",
        "habitat": "Altas laderas áridas y semiáridas de la precordillera y cordillera de los Andes, desde los 2.500 hasta los 3.800 m de altitud. Crece en suelos pedregosos y arenosos con extrema radiación solar.",
        "descripcion_hoja": "Hojas pequeñas, opuestas o fasciculadas, de forma linear a espatulada, de 5 a 15 mm de largo, de color verde grisáceo a plateado por una densa pubescencia. Textura coriácea, con glándulas oleíferas que desprenden un aroma intenso y agradable similar al limón y la menta.",
        "descripcion_tallo": "Arbusto bajo de 30 a 80 cm de altura, muy ramificado, con tallos leñosos, nudosos, de color pardo grisáceo. Ramas jóvenes blanquecinas.",
        "descripcion_flor": "Flores pequeñas, de 5-8 mm, de color blanco a lila pálido, dispuestas en espigas terminales densas. Corola tubulosa con 5 lóbulos. Florece entre noviembre y febrero. Muy aromática.",
        "foto_real": "https://via.placeholder.com/400x300?text=Rica-rica",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Carminativo, Estomacal, Antiespasmódico",
        "receta_preparacion": "Infusión: Verter 1 taza de agua hirviendo sobre 1 cucharadita de hojas secas. Reposar 5-8 minutos, colar y beber 1 taza después de las comidas para gases y cólicos digestivos. Tradicionalmente se usa como hierba aromática para sazonar comidas en el altiplano, especialmente sopas y guisos.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. Generalmente segura como condimento. No exceder las dosis recomendadas. Evitar en personas con alergia a las Verbenaceae. No confundir con otras especies de Acantholippia.",
    },
    # ---------------------------------------------------------------------------
    # 65. Romero
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Romero",
        "nombre_cientifico": "Rosmarinus officinalis",
        "familia_botanica": "Lamiaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Cultivado extensamente en jardines y huertos; naturalizado en laderas secas y soleadas. Prefiere suelos calcáreos, bien drenados y exposición solar directa.",
        "descripcion_hoja": "Hojas simples, opuestas, sésiles, de forma linear, de 2 a 4 cm de largo, de color verde oscuro brillante en el haz y blanquecino tomentoso en el envés. Bordes revolutos. Textura coriácea. Desprenden un aroma intenso y característico.",
        "descripcion_tallo": "Arbusto de 50 a 150 cm de altura, erecto, muy ramificado, con tallos leñosos de color pardo grisáceo y ramas jóvenes de color verde claro.",
        "descripcion_flor": "Flores axilares, dispuestas en racimos cortos, de 1 a 1.5 cm de largo, de color azul violáceo a lila pálido, con corola bilabiada. Florece durante casi todo el año, especialmente entre primavera y verano.",
        "foto_real": "https://via.placeholder.com/400x300?text=Romero",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Estimulante, Antioxidante, Antiséptico, Memoria",
        "receta_preparacion": "Infusión: Verter 1 taza de agua hirviendo sobre 1 cucharadita de hojas secas de romero, reposar 5-10 minutos, colar y beber 1-2 tazas al día para mejorar la memoria y la digestión. En la cocina se usa para aromatizar carnes, aves, salsas y panes. Aceite de romero: macerar ramas en aceite de oliva para masajes.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. El aceite esencial no debe ingerirse puro. Contraindicado en personas con epilepsia, hipertensión no controlada o enfermedades intestinales inflamatorias. Evitar dosis elevadas por riesgo de convulsiones. Uso culinario moderado es seguro.",
    },
    # ---------------------------------------------------------------------------
    # 66. Rosa Mosqueta
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Rosa Mosqueta",
        "nombre_cientifico": "Rosa moschata",
        "familia_botanica": "Rosaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Matorrales, bordes de caminos, praderas, terrenos baldíos y orillas de cursos de agua. Prefiere suelos húmedos y exposición solar.",
        "descripcion_hoja": "Hojas compuestas, imparipinnadas, con 5-7 folíolos de forma ovada a elíptica, de 2 a 5 cm de largo, de color verde oscuro, con bordes finamente dentados. Estípulas grandes y adheridas al pecíolo. El raquis presenta espinas.",
        "descripcion_tallo": "Arbusto de 1 a 3 m de altura, con tallos arqueados, trepadores, de color verde rojizo, armados de espinas fuertes y curvas.",
        "descripcion_flor": "Flores solitarias o en pequeños grupos, de 3 a 5 cm de diámetro, de color blanco a rosado pálido, con 5 pétalos anchos y numerosos estambres amarillos. Florece entre noviembre y febrero. El fruto (escaramujo) es un receptáculo carnoso de color rojo anaranjado, rico en vitamina C.",
        "foto_real": "https://via.placeholder.com/400x300?text=Rosa+mosqueta",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Cicatrizante, Regenerador celular, Antioxidante, Antienvejecimiento",
        "receta_preparacion": "Infusión de frutos: Machacar 2 cucharadas de escaramujos secos y hervirlos en 1 litro de agua por 10 minutos. Reposar 15 minutos, colar y beber 2-3 tazas al día como fuente natural de vitamina C. Aceite de rosa mosqueta: extraer de las semillas, se aplica directamente sobre cicatrices, arrugas y quemaduras. Mermelada de escaramujos.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. Los pelos internos de los frutos pueden irritar el tracto digestivo; colar bien las infusiones. El aceite puro puede causar acné en personas con piel grasa. No recolectar en lugares contaminados o con pesticidas.",
    },
    # ---------------------------------------------------------------------------
    # 67. Ruda
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Ruda",
        "nombre_cientifico": "Ruta graveolens",
        "familia_botanica": "Rutaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío",
        "habitat": "Cultivada en jardines y huertos; naturalizada en laderas secas y pedregosas. Prefiere suelos calcáreos, bien drenados y exposición solar.",
        "descripcion_hoja": "Hojas alternas, compuestas, 2-3 pinnatisectas, con segmentos oblongos a espatulados, de 2 a 6 cm de largo, de color verde azulado (glauco), textura carnosa y glabra. Desprenden un olor fuerte, acre y penetrante característico.",
        "descripcion_tallo": "Tallos erectos, de 30 a 80 cm de altura, leñosos en la base, muy ramificados, de color verde azulado a pardo claro.",
        "descripcion_flor": "Inflorescencias en corimbos terminales, con flores de 1 a 2 cm de diámetro, de color amarillo intenso, con 4-5 pétalos y 8-10 estambres. Florece entre primavera y verano. El fruto es una cápsula globosa con 4-5 lóbulos.",
        "foto_real": "https://via.placeholder.com/400x300?text=Ruda",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Antiespasmódico, Emenagogo, Digestivo, Antiparasitario, Antiinflamatorio",
        "receta_preparacion": "Infusión: Hervir 1 cucharadita de hojas secas en 1 taza de agua por 3 minutos. Reposar 10 minutos, colar y beber 1 taza 1-2 veces al día para cólicos menstruales y trastornos digestivos. En uso externo, la infusión concentrada se usa para lavar heridas y en compresas para aliviar dolores reumáticos.",
        "advertencias": "No consumir durante el embarazo (es abortiva) ni la lactancia. En dosis elevadas es tóxica, causando vómitos, dolor abdominal y daño renal. Puede causar fotosensibilidad severa; evitar exponerse al sol después de manipularla. Usar guantes al cosecharla. Contraindicada en personas con enfermedades hepáticas o renales.",
    },
    # ---------------------------------------------------------------------------
    # 68. Sabinilla / Perlilla
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Sabinilla, Perlilla",
        "nombre_cientifico": "Margyricarpus pinnatus",
        "familia_botanica": "Rosaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos, Aysén",
        "habitat": "Praderas secas, laderas de cerros, matorrales abiertos, suelos arenosos. Desde el nivel del mar hasta los 1.500 m de altitud.",
        "descripcion_hoja": "Hojas compuestas, alternas, imparipinnadas, con 5-11 folíolos pequeños de forma linear a oblonga, de 3 a 8 mm de largo, de color verde oscuro, con bordes revolutos. Textura coriácea. Estípulas pequeñas y persistentes.",
        "descripcion_tallo": "Arbusto bajo de 20 a 60 cm de altura, muy ramificado desde la base, con tallos delgados, erectos o ascendentes, de color pardo rojizo a grisáceo. Ramas densas que forman cojines.",
        "descripcion_flor": "Flores pequeñas, de 3-4 mm, solitarias, axilares, de color blanco verdoso, sin pétalos (solo cáliz). Florece entre octubre y diciembre. El fruto es una drupa globosa de 5-8 mm, de color blanco perlado (de ahí 'perlilla'), comestible y de sabor dulce.",
        "foto_real": "https://via.placeholder.com/400x300?text=Sabinilla",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Digestivo, Antiinflamatorio",
        "receta_preparacion": "Infusión de hojas y tallos: Hervir 1 cucharada de la planta seca en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 2 tazas al día como depurativo y para problemas digestivos. Los frutos blancos se comen frescos como golosina silvestre.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No se han reportado toxicidades significativas con uso moderado. No confundir con la sabina (Juniperus sabina), que es tóxica. Consultar a un médico antes de usar.",
    },
    # ---------------------------------------------------------------------------
    # 69. Salvia
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Salvia",
        "nombre_cientifico": "Salvia officinalis",
        "familia_botanica": "Lamiaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía",
        "habitat": "Cultivada en huertos y jardines; naturalizada en laderas secas y soleadas. Prefiere suelos calcáreos, bien drenados y exposición solar directa.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma oblonga a lanceolada, de 3 a 8 cm de largo, de color verde grisáceo, con textura rugosa y finamente pubescente. Bordes finamente crenados. Desprenden un aroma intenso y alcanforado característico.",
        "descripcion_tallo": "Arbusto de 30 a 80 cm de altura, erecto, muy ramificado, con tallos leñosos en la base, cuadrangulares, de color verde grisáceo a pardo claro.",
        "descripcion_flor": "Inflorescencias en espigas terminales de 10 a 20 cm de largo, con verticilos de 4-8 flores de color azul violáceo a lila intenso. Corola bilabiada con el labio superior en forma de casco. Florece entre noviembre y marzo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Salvia",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Digestivo, Antiséptico, Antiinflamatorio, Antioxidante, Emenagogo",
        "receta_preparacion": "Infusión: Verter 1 taza de agua hirviendo sobre 1 cucharadita de hojas secas de salvia, reposar 8-10 minutos, colar y beber 1-2 tazas al día para problemas digestivos, menopausia y excesiva sudoración. En la cocina se usa para aromatizar carnes, aves, pastas y salsas. Gargarismos para inflamaciones bucales.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. El aceite esencial contiene tuyona, neurotóxica en dosis altas. No exceder las dosis recomendadas. Evitar el consumo prolongado (más de 2 semanas continuas). Contraindicado en personas con epilepsia o enfermedades neurológicas.",
    },
    # ---------------------------------------------------------------------------
    # 70. Salvia blanca
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Salvia blanca",
        "nombre_cientifico": "Sphacele salviae",
        "familia_botanica": "Lamiaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío",
        "habitat": "Laderas de cerros, matorrales esclerófilos y quebradas de la zona central. Desde el nivel del mar hasta los 1.000 m de altitud.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma ovada a elíptica, de 3 a 8 cm de largo, de color verde claro a medio, cubiertas de una densa pubescencia blanquecina que les da un aspecto plateado (de ahí 'salvia blanca'). Textura aterciopelada, bordes dentados.",
        "descripcion_tallo": "Arbusto de 60 a 150 cm de altura, erecto, ramificado, con tallos de color verde blanquecino, cuadrangulares, cubiertos de pelos finos.",
        "descripcion_flor": "Flores axilares, solitarias o en pares, de 2 a 3 cm de largo, de color azul violáceo intenso a morado, con corola bilabiada grande. Cáliz acampanado, pubescente. Florece entre octubre y enero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Salvia+blanca",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Colagogo, Antiespasmódico",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza después de las comidas para problemas digestivos y hepáticos. Tradicionalmente usada por el pueblo mapuche como remedio estomacal y para la vesícula.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. No confundir con la salvia común (Salvia officinalis). Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 71. Sanguinaria
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Sanguinaria",
        "nombre_cientifico": "Polygonum sanguinaria",
        "familia_botanica": "Polygonaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Lugares húmedos, riberas de ríos y lagos, zanjas y pantanos. Desde el nivel del mar hasta los 500 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, de forma lanceolada a oblonga, de 4 a 12 cm de largo, de color verde oscuro, a menudo con una mancha oscura en el haz. Presentan una ócrea (vaina) membranosa que rodea el tallo en la base del pecíolo. Textura membranácea.",
        "descripcion_tallo": "Tallos erectos o ascendentes, de 30 a 100 cm de altura, cilíndricos, de color verde a rojizo, con nudos engrosados, simples o ramificados. Presentan rizomas rastreros.",
        "descripcion_flor": "Inflorescencias en espigas densas terminales, de 3 a 8 cm de largo, con numerosas flores pequeñas de color rosado intenso a rojo. Perianto con 5 tépalos. Florece entre diciembre y marzo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Sanguinaria",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Vulnerario, Cicatrizante, Astringente, Hemostático",
        "receta_preparacion": "En uso externo: Machacar las hojas frescas y aplicarlas directamente sobre heridas sangrantes para detener la hemorragia. Decocción: Hervir 100 g de la planta fresca en 2 litros de agua por 15 minutos, usar en compresas y lavados de heridas y llagas. Tradicionalmente usada para cortes y hemorroides.",
        "advertencias": "No consumir internamente. Solo para uso externo. No aplicar sobre heridas infectadas sin consultar a un médico. Suspender su uso si aparece irritación. No usar durante el embarazo ni la lactancia.",
    },
    # ---------------------------------------------------------------------------
    # 72. Sauce Amargo / Sauce Llorón
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Sauce Amargo, Sauce Llorón",
        "nombre_cientifico": "Salix humboldtiana",
        "familia_botanica": "Salicaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos",
        "habitat": "Riberas de ríos, esteros y lagos, vegas y lugares húmedos. Desde el nivel del mar hasta los 800 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, de forma lanceolada a linear-lanceolada, de 5 a 15 cm de largo, de color verde claro a medio, con bordes finamente aserrados. Textura membranácea, glabras, con ápice acuminado. Pecíolo corto, con estípulas pequeñas y caducas.",
        "descripcion_tallo": "Árbol de 5 a 20 m de altura, con tronco de corteza agrietada de color pardo grisáceo. Copa irregular. Ramas largas, delgadas y colgantes (péndulas), de color verde amarillento.",
        "descripcion_flor": "Flores en amentos (inflorescencias colgantes) de 3 a 8 cm de largo. Plantas dioicas. Las flores son pequeñas, de color amarillo verdoso, sin pétalos. Florece entre agosto y octubre, antes de la brotación de las hojas.",
        "foto_real": "https://via.placeholder.com/400x300?text=Sauce",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Analgésico, Antiinflamatorio, Antipirético, Astringente",
        "receta_preparacion": "Infusión de corteza: Hervir 1 cucharada de corteza seca troceada en 1 taza de agua por 10 minutos. Reposar 10 minutos, colar y beber 1 taza 2-3 veces al día para dolores de cabeza, fiebre y dolores musculares. La corteza contiene salicina, precursor del ácido acetilsalicílico (aspirina).",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Contraindicado en personas alérgicas a la aspirina o con úlceras gástricas. No administrar a niños menores de 12 años por riesgo de síndrome de Reye. Puede interferir con anticoagulantes. No exceder las dosis recomendadas.",
    },
    # ---------------------------------------------------------------------------
    # 73. Sauco
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Sauco",
        "nombre_cientifico": "Sambucus nigra",
        "familia_botanica": "Viburnaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Lugares húmedos, bordes de cursos de agua, quebradas, jardines y huertos. Prefiere suelos profundos y húmedos.",
        "descripcion_hoja": "Hojas compuestas, opuestas, imparipinnadas, con 5-7 folíolos de forma ovada a elíptica, de 5 a 15 cm de largo, de color verde oscuro, con bordes finamente aserrados. Textura membranácea. Desprenden olor característico al estrujarlas.",
        "descripcion_tallo": "Arbusto o árbol pequeño de 2 a 8 m de altura, con tronco de corteza rugosa de color pardo grisáceo. Ramas jóvenes gruesas, con médula blanquecina y suave.",
        "descripcion_flor": "Inflorescencias en corimbos grandes (10-20 cm de diámetro), con numerosas flores pequeñas de color blanco cremoso, de 5-8 mm de diámetro, con 5 pétalos. Muy fragantes. Florece entre octubre y diciembre. El fruto es una baya globosa de 5-8 mm, de color negro violáceo brillante.",
        "foto_real": "https://via.placeholder.com/400x300?text=Sauco",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Expectorante, Sudorífico, Antigripal, Antiinflamatorio, Antioxidante",
        "receta_preparacion": "Infusión de flores: Verter 1 taza de agua hirviendo sobre 1 cucharada de flores secas. Reposar 10 minutos, colar y beber 2-3 tazas al día para resfriados y gripes. Jarabe de sauco: Hervir los frutos maduros con azúcar y agua, tomar 1 cucharada 3 veces al día para fortalecer el sistema inmunológico.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Las bayas deben consumirse siempre cocidas (crudas pueden causar náuseas y vómitos por su contenido de sambunigrina). No confundir con el sauco del diablo (Sambucus australis). Todas las partes verdes de la planta contienen glucósidos cianogénicos tóxicos.",
    },
    # ---------------------------------------------------------------------------
    # 74. Tilo
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Tilo",
        "nombre_cientifico": "Tilia spp.",
        "familia_botanica": "Malvaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos",
        "habitat": "Cultivado en parques, jardines y calles como ornamental. Prefiere suelos profundos, fértiles y húmedos. Naturalizado en algunos sectores húmedos.",
        "descripcion_hoja": "Hojas simples, alternas, de forma ovada a cordada (en forma de corazón), de 5 a 15 cm de largo, de color verde oscuro en el haz y más pálido en el envés. Bordes finamente aserrados. Textura membranácea. Base cordada asimétrica. Pecíolo largo y delgado.",
        "descripcion_tallo": "Árbol de 10 a 25 m de altura, con tronco de corteza lisa de color gris claro cuando joven, que se vuelve agrietada con la edad. Copa amplia y redondeada. Ramas extendidas.",
        "descripcion_flor": "Inflorescencias en cimas colgantes de 5-10 flores, de color blanco amarillento, muy fragantes. Presentan una bráctea alargada (bractéola) soldada al pedúnculo. Florece entre diciembre y enero. El fruto es una nuez globosa, leñosa, de 5-8 mm.",
        "foto_real": "https://via.placeholder.com/400x300?text=Tilo",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Sedante, Ansiolítico, Antiespasmódico, Digestivo, Hipotensor suave",
        "receta_preparacion": "Infusión de flores y brácteas: Verter 1 taza de agua hirviendo sobre 1 cucharada de flores secas (con bráctea). Reposar 10 minutos tapado, colar y beber 1 taza caliente 2-3 veces al día para nerviosismo, insomnio, ansiedad y resfriados. Tradicionalmente se usa para bajar la presión arterial.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Puede causar somnolencia; no conducir ni operar maquinaria pesada después de consumirlo. Las flores pueden causar reacciones alérgicas en personas sensibles. No combinar con alcohol u otros sedantes. Consultar a un médico para uso prolongado.",
    },
    # ---------------------------------------------------------------------------
    # 75. Toronjil Cuyano (Marrubio) / Toronjil (Melisa)
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Toronjil Cuyano, Toronjil",
        "nombre_cientifico": "Melissa officinalis",
        "familia_botanica": "Lamiaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Lagos",
        "habitat": "Cultivado en huertos y jardines; naturalizado en bordes de caminos y lugares húmedos. Prefiere suelos fértiles y húmedos con semisombra.",
        "descripcion_hoja": "Hojas simples, opuestas, de forma ovada a acorazonada, de 3 a 8 cm de largo, de color verde claro a medio, textura membranácea, con bordes crenados. Desprenden un intenso aroma a limón al estrujarlas. Nervadura reticulada prominente en el envés.",
        "descripcion_tallo": "Tallos erectos, de 30 a 80 cm de altura, cuadrangulares, muy ramificados, de color verde claro, con pubescencia en las aristas.",
        "descripcion_flor": "Flores axilares, dispuestas en verticilos de 4-12 en la parte superior de los tallos, de color blanco a crema o lila pálido. Corola bilabiada con el labio superior erecto. Florece entre diciembre y marzo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Toronjil",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Sedante, Ansiolítico, Digestivo, Antiespasmódico, Antiviral",
        "receta_preparacion": "Infusión: Verter 1 taza de agua hirviendo sobre 1 cucharada de hojas frescas o secas de toronjil. Reposar 8-10 minutos tapado, colar y beber 1 taza 2-3 veces al día para calmar los nervios, mejorar el sueño y aliviar cólicos digestivos. Se puede tomar fría como bebida refrescante. Tradicionalmente se usa en aguas frescas.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Generalmente segura, pero en dosis muy elevadas puede causar somnolencia. El aceite esencial puede irritar la piel sensible. No confundir con el toronjil cuyano (Marrubium vulgare), que tiene propiedades diferentes. Consultar a un médico si se toman medicamentos sedantes.",
    },
    # ---------------------------------------------------------------------------
    # 76. Triqui-Triqui / Trique
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Triqui-Triqui, Trique",
        "nombre_cientifico": "Libertia sessiliflora",
        "familia_botanica": "Iridaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Bosques templados húmedos, claros de bosque, bordes de caminos y turberas. Desde el nivel del mar hasta los 500 m de altitud.",
        "descripcion_hoja": "Hojas basales, dísticas (en dos filas), en forma de abanico, lineares, de 30 a 80 cm de largo y 5-12 mm de ancho, de color verde oscuro brillante, con textura coriácea y bordes enteros. La base de las hojas es envainadora.",
        "descripcion_tallo": "Tallo floral (escapo) erecto, de 40 a 100 cm de altura, delgado, cilíndrico, de color verde claro, ramificado en la parte superior. Rizoma corto y rastrero.",
        "descripcion_flor": "Inflorescencias en panículas terminales laxas, con numerosas flores de 2 a 3 cm de diámetro, de color blanco puro, con 6 tépalos y centro amarillo. Florece entre noviembre y enero. El fruto es una cápsula globosa de color pardo que contiene semillas anaranjadas.",
        "foto_real": "https://via.placeholder.com/400x300?text=Triqui-triqui",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Antiinflamatorio",
        "receta_preparacion": "Infusión de hojas y raíces: Hervir 1 cucharada de la planta seca troceada en 1 litro de agua por 10 minutos. Reposar 10 minutos, colar y beber 2 tazas al día como depurativo y para problemas urinarios. Tradicionalmente usada por el pueblo mapuche para tratar infecciones renales y como purgante suave.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. Consultar a un médico antes de usar de forma prolongada. No se han reportado toxicidades significativas con uso moderado.",
    },
    # ---------------------------------------------------------------------------
    # 77. Valeriana
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Valeriana",
        "nombre_cientifico": "Valeriana officinalis",
        "familia_botanica": "Caprifoliaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Praderas húmedas, riberas de cursos de agua, bosques húmedos. Prefiere suelos profundos, fértiles y con buen drenaje.",
        "descripcion_hoja": "Hojas opuestas, compuestas, pinnadas, con 7-15 folíolos de forma lanceolada, de 5 a 15 cm de largo, de color verde oscuro, con bordes dentados. Las hojas inferiores son pecioladas y las superiores sésiles.",
        "descripcion_tallo": "Tallo erecto, de 50 a 150 cm de altura, cilíndrico, hueco, estriado, de color verde claro, ramificado en la parte superior. Rizoma corto, grueso, con numerosas raíces fibrosas de olor fuerte y característico.",
        "descripcion_flor": "Inflorescencias en corimbos o panículas terminales densas, con flores pequeñas de color blanco a rosado pálido, de 3-5 mm de diámetro. Corola infundibuliforme con 5 lóbulos. Florece entre diciembre y febrero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Valeriana",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Sedante, Ansiolítico, Antiespasmódico, Relajante muscular",
        "receta_preparacion": "Infusión de raíz: Hervir 1 cucharadita de raíz seca troceada en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza 1 hora antes de acostarse para tratar el insomnio y la ansiedad. Tintura: Macerar 30 g de raíz seca en 100 ml de alcohol de 70° por 10 días; tomar 20-30 gotas en agua antes de dormir.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. Puede causar somnolencia; no conducir ni operar maquinaria después de consumirla. No combinar con alcohol u otros depresores del sistema nervioso central. El uso prolongado puede causar dependencia. Evitar en personas con enfermedades hepáticas. En algunas personas puede causar efecto estimulante paradójico.",
    },
    # ---------------------------------------------------------------------------
    # 78. Verbena
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Verbena",
        "nombre_cientifico": "Verbena litoralis",
        "familia_botanica": "Verbenaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos",
        "habitat": "Terrenos baldíos, bordes de caminos, praderas húmedas, riberas de cursos de agua. Desde el nivel del mar hasta los 1.000 m de altitud.",
        "descripcion_hoja": "Hojas opuestas, de forma lanceolada a oblonga, de 3 a 10 cm de largo, de color verde oscuro, con bordes irregularmente dentados (más profundos en la base). Textura áspera y rugosa, con nervadura reticulada prominente en el envés.",
        "descripcion_tallo": "Tallos erectos, cuadrangulares, de 40 a 120 cm de altura, estriados, de color verde a púrpura, ramificados en la parte superior, con pubescencia áspera.",
        "descripcion_flor": "Inflorescencias en espigas terminales delgadas y alargadas (5-20 cm), con numerosas flores pequeñas de color azul violáceo a lila. Corola tubulosa con 5 lóbulos. Florece durante casi todo el año.",
        "foto_real": "https://via.placeholder.com/400x300?text=Verbena",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Febrífugo, Analgésico, antiinflamatorio",
        "receta_preparacion": "Infusión de hojas y flores: Hervir 1 cucharada de la planta seca en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para problemas hepáticos, digestivos y fiebre. En uso externo, la infusión concentrada se aplica en compresas para aliviar golpes y contusiones.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. Evitar en personas con enfermedades hepáticas crónicas. Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 79. Violeta
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Violeta",
        "nombre_cientifico": "Viola odorata",
        "familia_botanica": "Violaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos",
        "habitat": "Jardines, bordes de caminos, lugares sombríos y húmedos, praderas. Prefiere suelos fértiles, húmedos y ricos en materia orgánica.",
        "descripcion_hoja": "Hojas basales en roseta, de forma acorazonada (cordada) a reniforme, de 2 a 6 cm de ancho, de color verde oscuro brillante, con bordes crenados. Largos pecíolos (5-15 cm). Textura suave y membranácea.",
        "descripcion_tallo": "Tallo floral (escapo) de 5 a 15 cm de altura, delgado, de color verde claro, que emerge desde la base. La planta produce estolones que enraízan en los nudos, formando colonias. Rizoma corto.",
        "descripcion_flor": "Flores solitarias, de 1.5 a 2.5 cm de diámetro, de color violeta intenso a lila, con 5 pétalos desiguales, el inferior con espolón. Muy fragantes. Florece entre agosto y noviembre. También produce flores cleistógamas (no abiertas) que se autofecundan.",
        "foto_real": "https://via.placeholder.com/400x300?text=Violeta",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Expectorante, Antiinflamatorio, Emoliente, Antitusivo",
        "receta_preparacion": "Infusión de flores y hojas: Verter 1 taza de agua hirviendo sobre 1 cucharada de flores frescas o secas. Reposar 10 minutos, colar y beber 2-3 tazas al día para la tos, bronquitis y resfriados. Jarabe de violetas: Hervir las flores en agua con azúcar para preparar un jarabe expectorante. Las flores cristalizadas se usan en repostería.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. La raíz y las semillas son eméticas y purgantes en dosis altas. No confundir con la violeta africana (Saintpaulia), que no es medicinal. No recolectar en lugares contaminados. Consultar a un médico para uso prolongado.",
    },
    # ---------------------------------------------------------------------------
    # 80. Vira-Vira
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Vira-Vira",
        "nombre_cientifico": "Pseudognaphalium viravira",
        "familia_botanica": "Asteraceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío",
        "habitat": "Laderas de cerros, praderas secas, matorrales abiertos y terrenos arenosos. Desde el nivel del mar hasta los 1.500 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, de forma linear a espatulada, de 2 a 6 cm de largo, de color blanco plateado a grisáceo, densamente cubiertas de un tomento lanoso (como fieltro). Textura suave y aterciopelada. Bordes enteros.",
        "descripcion_tallo": "Tallos erectos o ascendentes, de 20 a 60 cm de altura, ramificados desde la base, densamente lanosos, de color blanco plateado.",
        "descripcion_flor": "Capítulos pequeños, de 5-8 mm de diámetro, agrupados en corimbos densos terminales, de color amarillo pálido a crema. Involucro con brácteas escariosas. Florece entre noviembre y marzo.",
        "foto_real": "https://via.placeholder.com/400x300?text=Vira-vira",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Expectorante, Antitusivo, Broncodilatador, Antiasmático, Antiinflamatorio",
        "receta_preparacion": "Infusión: Hervir 1 cucharada de hojas y tallos secos en 1 litro de agua por 5 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para afecciones respiratorias como asma, bronquitis, tos y resfriados. Tradicionalmente se prepara con leche caliente y miel para potenciar su efecto.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. No se han reportado toxicidades significativas, pero se recomienda uso moderado. Consultar a un médico antes de usar para tratar el asma crónica. No debe sustituir los medicamentos recetados.",
    },
    # ---------------------------------------------------------------------------
    # 81. Yerba de la Plata / Limpiaplata
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Yerba de la Plata, Limpiaplata",
        "nombre_cientifico": "Equisetum bogotense",
        "familia_botanica": "Equisetaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Lugares húmedos, arenosos, bordes de cursos de agua, zanjas y terrenos pantanosos. Desde el nivel del mar hasta los 1.500 m de altitud.",
        "descripcion_hoja": "Hojas reducidas a escamas membranáceas en los nudos, fusionadas en una vaina dentada que rodea el tallo. De color pardo oscuro. No realiza fotosíntesis en las hojas; la función fotosintética la realizan los tallos.",
        "descripcion_tallo": "Tallos erectos, de 20 a 80 cm de altura, cilíndricos, de color verde medio, con 10-20 costillas longitudinales prominentes. Presentan nudos y entrenudos huecos. Textura áspera y estriada por su alto contenido de sílice. Rizomas largos y rastreros.",
        "descripcion_flor": "No produce flores ni semillas. Es un helecho primitivo que se reproduce mediante esporas producidas en un cono (estróbilo) terminal de 1-3 cm en el ápice de los tallos fértiles. Las esporas son verdes y tienen eláteres para su dispersión.",
        "foto_real": "https://via.placeholder.com/400x300?text=Yerba+de+la+plata",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Diurético, Depurativo, Antiinflamatorio, Hemostático",
        "receta_preparacion": "Infusión de tallos: Hervir 1 cucharada de tallos secos en 1 taza de agua por 10 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día para infecciones urinarias, cálculos renales y como depurativo. En uso externo, la infusión concentrada se usa para lavar heridas y detener hemorragias superficiales. Se usa tradicionalmente para limpiar objetos de plata (de ahí su nombre).",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No usar por más de 2 semanas consecutivas. Por su alto contenido de sílice, el uso prolongado puede causar irritación renal. Contraindicado en personas con insuficiencia cardíaca o renal. No confundir con Equisetum giganteum (cola de caballo gigante).",
    },
    # ---------------------------------------------------------------------------
    # 82. Yerba del Clavo / Leliantu
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Yerba del Clavo, Leliantu",
        "nombre_cientifico": "Geum magellanicum",
        "familia_botanica": "Rosaceae",
        "origen": "NATIVA",
        "zona_macro": "PATAGONIA",
        "regiones": "Aysén, Magallanes",
        "habitat": "Praderas húmedas, bordes de turberas, vegas y laderas con humedad en la Patagonia y Tierra del Fuego. Desde el nivel del mar hasta los 500 m de altitud.",
        "descripcion_hoja": "Hojas basales en roseta densa, lirado-pinnatífidas, de 5 a 15 cm de largo, con folíolos desiguales, de color verde oscuro, textura pubescente. Hojas caulinares reducidas, con estípulas grandes y foliáceas.",
        "descripcion_tallo": "Tallos florales erectos, de 15 a 40 cm de altura, delgados, de color verde rojizo, cubiertos de pelos finos. Rizoma grueso y aromático.",
        "descripcion_flor": "Flores terminales, solitarias o en grupos de 2-3, de 2 a 3 cm de diámetro, con 5 pétalos de color amarillo intenso a anaranjado. Cáliz con 5 sépalos y bractéolas. Numerosos estambres y pistilos. Florece entre noviembre y febrero.",
        "foto_real": "https://via.placeholder.com/400x300?text=Yerba+del+clavo+patagonia",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Digestivo, Hepático, Colagogo, Antiinflamatorio",
        "receta_preparacion": "Infusión de raíz: Hervir 1 cucharadita de raíz seca troceada en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 1 taza después de las comidas para problemas digestivos y hepáticos. La raíz tiene aroma y sabor similar al clavo de olor. Tradicionalmente usada por los pueblos Kawésqar y Yámana.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. Evitar en personas con gastritis o úlceras digestivas. Consultar a un médico antes de usar de forma prolongada.",
    },
    # ---------------------------------------------------------------------------
    # 83. Yerba del Lagarto / Calaguala
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Yerba del Lagarto, Calaguala",
        "nombre_cientifico": "Synammia feuillei",
        "familia_botanica": "Polypodiaceae",
        "origen": "NATIVA",
        "zona_macro": "CENTRO",
        "regiones": "Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos",
        "habitat": "Crece como epífita sobre troncos de árboles (especialmente robles y coigües) y también sobre rocas cubiertas de musgo. Desde el nivel del mar hasta los 1.000 m de altitud.",
        "descripcion_hoja": "Frondas (hojas) lineares, de 20 a 80 cm de largo, de 1-3 cm de ancho, de color verde oscuro, con bordes enteros u ondulados. Textura coriácea. No tiene hojas verdaderas; las frondas son los órganos fotosintéticos. El rizoma está cubierto de escamas pardo-doradas.",
        "descripcion_tallo": "Rizoma rastrero, grueso (1-2 cm de diámetro), de color pardo oscuro, densamente cubierto de escamas de color dorado a pardo claro. Las frondas surgen individualmente a lo largo del rizoma.",
        "descripcion_flor": "No produce flores. Es un helecho que se reproduce mediante esporas. Los soros (estructuras reproductivas) son de forma redondeada, de color pardo anaranjado, dispuestos en 2 filas a lo largo del envés de las frondas, sin indusio.",
        "foto_real": "https://via.placeholder.com/400x300?text=Calaguala",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Depurativo, Antiinflamatorio, Diurético, Antipirético, Expectorante",
        "receta_preparacion": "Decocción de rizoma: Hervir 30 g de rizoma seco troceado en 1 litro de agua por 15 minutos. Reposar 10 minutos, colar y beber 2-3 tazas al día como depurativo para afecciones cutáneas, gota y reumatismo. En uso externo, la decocción se aplica en compresas sobre heridas, úlceras y afecciones de la piel.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. No recolectar helechos silvestres sin identificar correctamente la especie. Consultar a un médico antes de usar de forma prolongada. No confundir con helechos tóxicos como el helecho macho (Dryopteris filix-mas).",
    },
    # ---------------------------------------------------------------------------
    # 84. Zarzamora
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Zarzamora",
        "nombre_cientifico": "Rubus ulmifolius",
        "familia_botanica": "Rosaceae",
        "origen": "ASILVESTRADA",
        "zona_macro": "CENTRO",
        "regiones": "Coquimbo, Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén",
        "habitat": "Matorrales, bordes de caminos, cercos, quebradas y terrenos baldíos. Crece vigorosamente en suelos húmedos y fértiles, formando densas zarzas impenetrables.",
        "descripcion_hoja": "Hojas compuestas, alternas, palmadas o digitadas, con 3-5 folíolos de forma ovada a elíptica, de 3 a 8 cm de largo, de color verde oscuro en el haz y blanquecino tomentoso en el envés. Bordes finamente aserrados. Pecíolo y nervaduras con espinas.",
        "descripcion_tallo": "Tallos arqueados, largos (2-5 m), vigorosos, de color verde rojizo a púrpura, con sección pentagonal o acanalada, armados de fuertes espinas curvas. Forman matorrales impenetrables. Raíces profundas.",
        "descripcion_flor": "Inflorescencias en racimos terminales, con flores de 2 a 3 cm de diámetro, de color rosado a blanco, con 5 pétalos. Florece entre octubre y febrero. El fruto es una polidrupa (mora) compuesta por múltiples drupéolas, de color negro brillante al madurar.",
        "foto_real": "https://via.placeholder.com/400x300?text=Zarzamora",
        "uso_principal": "Medicinal y Culinario",
        "efecto_terapeutico": "Astringente, Antioxidante, Antiinflamatorio, Antidiarreico",
        "receta_preparacion": "Infusión de hojas: Hervir 1 cucharada de hojas secas en 1 taza de agua por 5 minutos. Reposar 10 minutos, colar y beber 2 tazas al día para diarreas y trastornos digestivos. Las moras se consumen frescas o en mermeladas, jugos, postres y licores. En uso externo, la decocción de hojas se usa para hacer gárgaras en inflamaciones bucales.",
        "advertencias": "No consumir durante el embarazo ni la lactancia en dosis medicinales. Las hojas contienen taninos que en exceso pueden causar estreñimiento. Tener cuidado al recolectar por las abundantes espinas. No recolectar en lugares contaminados o con pesticidas. Las moras silvestres pueden albergar insectos.",
    },
    # ---------------------------------------------------------------------------
    # 85. Zarzaparrilla
    # ---------------------------------------------------------------------------
    {
        "nombre_comun": "Zarzaparrilla",
        "nombre_cientifico": "Ribes cucullatum",
        "familia_botanica": "Grossulariaceae",
        "origen": "NATIVA",
        "zona_macro": "SUR",
        "regiones": "Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes",
        "habitat": "Bosques templados húmedos, laderas de cerros, bordes de cursos de agua y claros de bosque. Desde el nivel del mar hasta los 800 m de altitud.",
        "descripcion_hoja": "Hojas simples, alternas, de forma orbicular a reniforme, de 2 a 6 cm de ancho, palmeadas con 3-5 lóbulos poco profundos y bordes dentados. De color verde claro a medio, textura membranácea, con glándulas oleíferas aromáticas. Pecíolo largo y delgado.",
        "descripcion_tallo": "Arbusto de 50 a 150 cm de altura, con tallos erectos, delgados, de color verde rojizo a pardo claro, con espinas pequeñas en los nudos. Corteza que se desprende en tiras finas.",
        "descripcion_flor": "Flores unisexuales, pequeñas, de 4-6 mm, de color verde amarillento a rojizo, dispuestas en racimos colgantes de 3-8 cm. Plantas dioicas o polígamas. Florece entre octubre y diciembre. El fruto es una baya globosa de 5-8 mm, de color rojo oscuro a negro, comestible.",
        "foto_real": "https://via.placeholder.com/400x300?text=Zarzaparrilla",
        "uso_principal": "Medicinal",
        "efecto_terapeutico": "Depurativo, Diurético, Antiinflamatorio, Digestivo",
        "receta_preparacion": "Infusión de hojas y tallos: Hervir 1 cucharada de la planta seca troceada en 1 litro de agua por 10 minutos. Reposar 10 minutos, colar y beber 2 tazas al día como depurativo sanguíneo y para problemas digestivos. Los frutos se consumen frescos o en mermeladas. Tradicionalmente se usa para tratar afecciones reumáticas y de la piel.",
        "advertencias": "No consumir durante el embarazo ni la lactancia. No exceder las dosis recomendadas. No confundir con la zarzaparrilla mexicana (Smilax aristolochiifolia) o la zarzaparrilla paraguaya (Smilax campestris), que son especies diferentes. Consultar a un médico antes de usar de forma prolongada.",
    },
]
