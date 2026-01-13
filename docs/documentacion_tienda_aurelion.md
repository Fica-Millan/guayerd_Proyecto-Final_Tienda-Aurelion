# 🛒Proyecto Tienda Aurelion – Documentación técnica

### 📚 Índice de contenidos

- [🛒Proyecto Tienda Aurelion – Documentación técnica](#proyecto-tienda-aurelion--documentación-técnica)
    - [📚 Índice de contenidos](#-índice-de-contenidos)
    - [Tema](#tema)
    - [Problema](#problema)
    - [Solución](#solución)
    - [Fuente](#fuente)
    - [Datasets: definición, columnas y tipos](#datasets-definición-columnas-y-tipos)
    - [Estructura](#estructura)
    - [Información](#información)
    - [Pasos](#pasos)
    - [Pseudocódigo](#pseudocódigo)
    - [Diagrama del flujo](#diagrama-del-flujo)
    - [Interpretaciones EDA – Visualizaciones](#interpretaciones-eda--visualizaciones)
      - [🔸 Gráfica: distribucion\_numericas](#-gráfica-distribucion_numericas)
      - [🔸 Gráfica: correlacion](#-gráfica-correlacion)
      - [🔸 Gráfica: ventas\_total\_por\_mes](#-gráfica-ventas_total_por_mes)
      - [🔸 Gráfica: relacion\_cantidad](#-gráfica-relacion_cantidad)
      - [🔸 Gráfica: outliers](#-gráfica-outliers)
    - [Preprocesamiento para Machine Learning](#preprocesamiento-para-machine-learning)
    - [AutoML: Benchmarking con PyCaret](#automl-benchmarking-con-pycaret)
    - [Entrenamiento Manual: Random Forest](#entrenamiento-manual-random-forest)
    - [Dashboard Ejecutivo](#dashboard-ejecutivo)
      - [🔸 Dashboard](#-dashboard)
      - [🔸 Réplicas de Vistas](#-réplicas-de-vistas)
      - [🔸 Conclusiones](#-conclusiones)

---

### Tema

Análisis y consulta interactiva de datos de ventas de la Tienda Aurelion, una tienda minorista que desea comprender mejor el comportamiento de sus ventas, productos y clientes.

### Problema

La Tienda Aurelion enfrenta dificultades para mantener un equilibrio adecuado entre el stock disponible y la demanda real de los productos. Esto genera dos problemas recurrentes:

  - _Rupturas de stock_: cuando un producto se agota y no puede ser vendido.
  - _Exceso de inventario_: cuando se compran productos que permanecen sin rotación durante mucho tiempo.

Ambas situaciones impactan negativamente en la rentabilidad del negocio:

  - Las rupturas de stock reducen las ventas y afectan la satisfacción del cliente.
  - El exceso de inventario genera costos de almacenamiento innecesarios.

### Solución

Desarrollar un programa en Python y Streamlit que permita interactuar con los datos y consultar de forma sencilla información relevante. Utilizar los datos históricos de ventas, clientes y productos para:

  - Analizar la demanda real de cada producto.
  - Identificar los productos de mayor y menor rotación.
  - Estimar la demanda futura promedio mensual.
  - Proporcionar información visual que ayude a tomar decisiones de compra y reposición más inteligentes.

**Análisis que se puede realizar**

1. Ventas totales por producto y mes.
2. Ranking de productos más vendidos.
3. Relación entre stock disponible y ventas promedio.
4. Productos con ventas decrecientes (riesgo de exceso de stock).
5. Productos con ventas crecientes (riesgo de ruptura de stock).
6. Predicción de demanda promedio mediante una regresión lineal simple.

**Resultado esperado**

Una aplicación en Streamlit que permita:

   - Visualizar métricas de ventas y rotación.
   - Detectar los productos críticos para reposición.
   - Consultar la documentación del proyecto.


---

### Fuente

Su origen es secundario, los datasets fueron provistos por Guayerd dentro del programa de Fundamentos de Inteligencia Artificial que desarrolla junto a IBM.

_Nota_: Estos datasets son de carácter didáctico y se proporcionan solo con fines de prueba y aprendizaje, para poder estudiar y practicar el análisis de datos y la implementación de modelos.

---

### Datasets: definición, columnas y tipos

| Dataset | Descripción breve | Columnas | Tipo / Escala |
|----------|------------------|-----------|----------------|
| **clientes.xlsx** | Información de los clientes | id_cliente<br>nombre_cliente<br>email<br>ciudad<br>fecha_alta | int64 (Razón)<br>object (Nominal)<br>object (Nominal)<br>object (Nominal)<br>datetime64 (Intervalo) |
| **productos.xlsx** | Información de los productos | id_producto<br>nombre_producto<br>categoria<br>precio_unitario | int64 (Razón)<br>object (Nominal)<br>object (Nominal)<br>int64 (Razón) |
| **ventas.xlsx** | Registro de cada venta realizada | id_venta<br>fecha<br>id_cliente<br>nombre_cliente<br>email<br>medio_pago | int64 (Razón)<br>datetime64 (Intervalo)<br>int64 (Razón)<br>object (Nominal)<br>object (Nominal)<br>object (Nominal) |
| **detalle_ventas.xlsx** | Detalle de cada producto vendido | id_venta<br>id_producto<br>nombre_producto<br>cantidad<br>precio_unitario<br>importe | int64 (Razón)<br>int64 (Razón)<br>object (Nominal)<br>int64 (Razón)<br>int64 (Razón)<br>int64 (Razón) |

**Comentarios:**

- **PK (Primary Key):** identificador único de cada registro.  
- **FK (Foreign Key):** columna que referencia la PK de otro dataset.  
- `id_cliente`, `id_producto` y `id_venta` son **PK** en sus respectivas tablas.  
- `ventas.id_cliente` referencia a `clientes.id_cliente`.  
- `detalle_ventas.id_venta` referencia a `ventas.id_venta`.  
- `detalle_ventas.id_producto` referencia a `productos.id_producto`.  

---

### Estructura

Cada dataset está estructurado: se organiza en filas que representan registros individuales y columnas que representan atributos de interés para el análisis. Contienen datos tanto cuantitativos como cualitativos. Todos ellos en formato .xlsx (Excel).

---

### Información

🔸 **Nombre del programa:** Proyecto Tienda Aurelion

🔸 **Objetivo:**
  Permitir la exploración interactiva de los datos de ventas, clientes y productos de la tienda, proporcionados en los siguientes conjuntos de datos:
  - `clientes.xlsx`
  - `productos.xlsx`
  - `ventas.xlsx` 
  - `detalle_ventas.xlsx`
   
  Estos archivos fueron unificados en un único dataset integrado denominado `df_tienda_aurelion.csv`, que concentra toda la información relevante para su análisis. 
   
  Además, la aplicación muestra la documentación, el pseudocódigo y los diagramas de flujo del proyecto.

🔸 **Lenguaje y librerías utilizadas**

  - `Python 3.13` (entorno recomendado; crea un virtualenv para reproducibilidad)
  - Librerías principales (versiones en `requirements.txt`):
    - `streamlit==1.52.1` (interfaz web)
    - `pandas==2.1.4` (manipulación de datos)
    - `Pillow==12.0.0` (manipulación de imágenes)
    - `numpy==1.26.4` (cálculo numérico)
    - `matplotlib==3.7.5`, `seaborn==0.13.2` (visualización)
    - `plotly==6.5.0` (visualización interactiva)
    - `ydata-profiling==4.18.0` (EDA automatizado)
    - `streamlit-pandas-profiling` (integración de perfiles en Streamlit)
    - `wordcloud==1.9.4` (nubes de palabras)
  - Librerías para Machine Learning:
    - `pycaret==3.3.2` (AutoML / benchmarking)
    - `scikit-learn` (`sklearn`: preprocesamiento, modelos y métricas)
    - `joblib==1.3.2` (serialización de modelos)
  - Utilidades y sistema de archivos:
    - `os`, `pathlib` (gestión de rutas y archivos)
    - `openpyxl==3.1.5` (motor para lectura/escritura de Excel)
    - `pickle` (serialización en memoria o en archivo)
  - Observación: Las versiones exactas están en `requirements.txt`; para reproducir el entorno usar `pip install -r requirements.txt`. Si quieres, actualizo esta sección para listar los paquetes opcionales o los requisitos de desarrollo (test, lint, etc.).

🔸 **Entrada de datos**
  - Archivos Excel: `clientes.xlsx`, `productos.xlsx`, `ventas.xlsx`, `detalle_ventas.xlsx`
  - Archivo de documentación: `documentacion_tienda_aurelion.md`

🔸 **Salida / Visualización**
  - Interfaz web interactiva con menú lateral
  - Expanders utilizados en la sección Ver documentación para mostrar de forma organizada el contenido técnico (contexto, datasets, metodología, pseudocódigo y diagrama de flujo).
  - Tablas de datos y resúmenes estadísticos

🔸 **Funcionalidades principales**
  - **Información General**: Vista previa de cada dataset, tipos de datos, metadatos y estadísticas básicas.
  - **Estadísticas Descriptivas**: Análisis detallado mediante `pandas.describe(include="all")` con visualizaciones personalizadas:
    - Distribución de variables numéricas y categóricas
    - Matrices de correlación
    - Gráficos específicos por dataset (series temporales, distribuciones, etc.)
  - **EDA Automatizado**: Análisis exploratorio completo utilizando `ydata-profiling`:
    - Perfilado automático de variables
    - Detección de correlaciones y patrones
    - Análisis de valores faltantes y cardinalidad
  - **EDA Diagnóstico**: Análisis en profundidad del dataset unificado:
    - Limpieza y preparación de datos
    - Detección y análisis de outliers
    - Visualizaciones avanzadas de series temporales
    - Identificación de productos top y patrones de venta
  - **Preprocesamiento ML**: Herramientas interactivas para preparar datos antes del modelado:
    - Selección de objetivo (`target`) y variables predictoras
    - Imputación de valores faltantes (media/mediana/moda)
    - Codificación de variables categóricas (`one-hot`, `ordinal`)
    - Escalado de variables numéricas (`StandardScaler`, `MinMaxScaler`)
    - Selección/filtrado de features y exportación del dataset preprocesado a CSV
  - **ML Automatizado (AutoML)**: Benchmarking y selección automática de modelos (PyCaret):
    - Inicialización del experimento (`setup`) con normalización y control de multicolinealidad
    - Comparación automática de modelos (`compare_models`) y visualización de métricas
    - Exportación y descarga del mejor modelo encontrado
  - **Entrenamiento Manual (Random Forest)**: Entrenamiento y evaluación controlada:
    - Ajuste interactivo de hiperparámetros (n_estimators, max_depth, class_weight, etc.)
    - Validación cruzada, métricas de test, curvas ROC y matriz de confusión
    - Interpretación mediante `feature_importances_` y curvas de aprendizaje
    - Guardado y descarga del modelo (`joblib`/`pickle`)
  - **Dashboard Ejecutivo**: Vista ejecutiva y operativa para toma de decisiones:
    - Panel ejecutivo con KPIs: Ticket Promedio, Total Ventas, Unidades vendidas, % Top10, Promedio móvil.
    - Vistas por sección: Ventas (tendencia, ventas por categoría, ranking), Clientes (ventas por ciudad, ticket promedio), Productos (rotación, stock crítico, top N por ventas).
    - Filtros globales interactivos: rango de fechas, categoría, ciudad (aplican a todas las vistas).
    - Opciones de exportación: descargar CSV del dataset filtrado, descargar gráficos (PNG) y generar reporte (PDF/imagen).
    - Guardado automático de imágenes y figuras en `assets/plots` y posibilidad de descarga directa.
  - **Documentación Interactiva**: Acceso organizado a la documentación técnica del proyecto, pseudocódigo y diagramas.
  - **Exportación de artefactos y utilidades**: Guardado automático de figuras en `assets/plots`, modelos en `models/`, y opciones para descargar conjuntos de datos filtrados y reportes.

🔸 **Estructura del programa**
  - **Carga y Unificación**: 
    - Función `load_dataset()` con caché de Streamlit (`st.cache_data`) para eficiencia y reproducibilidad.
    - Generación automática del dataset unificado mediante `load_and_merge_datasets()` y guardado como CSV para uso posterior.
    - Validaciones y checks: tipos de dato, valores nulos y cardinalidad antes del procesamiento.
  - **Menú Principal**: Radio buttons en la barra lateral con las opciones:
    - Información General
    - Estadísticas
    - EDA Automatizado
    - EDA Diagnóstico
    - Preprocesamiento ML
    - ML Automatizado
    - Entrenamiento Random Forest
    - Dashboard Ejecutivo
    - Ver Documentación
  - **Módulos Organizados**:
    - Cargadores de datos (`data_loader.py`) — lectura, validación y unificación de fuentes.
    - Páginas separadas por funcionalidad (`src/pages/`): `general_info.py`, `statistics.py`, `automated_eda.py`, `diagnostic_eda.py`, `ml_preprocessing.py`, `automl.py`, `random_forest_manual.py`, `dashboard.py`, `documentacion.py`.
    - Utilidades (`src/utils/`): `figures.py` (guardado/estilo de gráficas), `dashboard_utils.py` (cálculo de KPIs), `export.py` (descarga CSV/PDF/PNG), `validation.py`.
    - Recursos y artefactos:
       - `assets/plots/` para figuras generadas automáticamente
       - `models/` para modelos serializados (`joblib` / `pickle`)
       - `docs/` y `README.md` para documentación y reproducibilidad
    - Observaciones de rendimiento: operaciones costosas (ProfileReport, generación de KPIs agregados) se cachean o se ejecutan bajo demanda para mejorar la UX.

---

### Pasos

<h5>1️⃣ <b>Inicio de la aplicación</b></h5>

- Se inicializa Streamlit y se configura la página (título, ícono y diseño).
- Se muestra el logotipo de la tienda junto al encabezado principal de la interfaz.

<h5>2️⃣ <b>Carga de datasets</b></h5>

- Se leen los archivos Excel: `clientes.xlsx`, `productos.xlsx`, `ventas.xlsx` y `detalle_ventas.xlsx` mediante **pandas**.
- Cada archivo se carga en un **DataFrame** independiente.
- La función de carga se **almacena en caché** (`st.cache_data`) para optimizar el rendimiento y evitar recargas innecesarias.

<h5>3️⃣ <b>Menú principal</b></h5>

- Se implementa mediante radio buttons en la barra lateral, ofreciendo secciones principales:
  - **Información General**: Exploración básica de datasets
  - **Estadísticas**: Análisis descriptivo y visualizaciones
  - **EDA Automatizado**: Perfilado completo de datos
  - **EDA Diagnóstico**: Análisis detallado y visualizaciones
  - **Preprocesamiento ML**: Limpieza, transformación y preparación del dataset para entrenamiento.
  - **AutoML (Benchmark)**: Comparación automática de múltiples modelos y selección del mejor rendimiento.
  - **Entrenamiento Manual (Random Forest)**: Configuración, entrenamiento y evaluación detallada del modelo Random Forest.
  - **Dashboard Ejecutivo**: Acceso al Dashboard Ejecutivo con KPIs y vistas (Ventas / Clientes / Productos)
  - **Ver Documentación**: Acceso a documentación técnica

<h5>4️⃣ <b>Opción: Información General</b></h5>

  - Interfaz de selección de dataset mediante selectbox
  - Para cada archivo seleccionado muestra:
    - Metadatos: fecha de modificación y tamaño
    - Vista previa de registros mediante `head()`
    - Estructura detallada: tipos de datos y columnas
    - Resumen: dimensiones y cantidad de registros
  - Información organizada en expanders para mejor navegación

<h5>5️⃣ <b>Opción 2: Estadísticas</b></h5>

   - Selección interactiva del dataset a analizar
   - Análisis estadístico completo que incluye:
     - Estadísticas descriptivas vía `describe(include="all")`
     - Análisis de valores nulos y únicos
     - Visualizaciones específicas según tipo de datos:
       • Variables numéricas: histogramas y boxplots
       • Variables categóricas: gráficos de barras y pie
       • Series temporales: evolución y tendencias

<h5>6️⃣ <b>Opción 3: EDA Automatizado</b></h5>

   - Generación automática del dataset unificado si no existe
   - Creación de un reporte interactivo completo usando `ydata-profiling`
   - Visualización integrada mediante `streamlit-pandas-profiling`
   - Análisis automático de:
     • Distribuciones y estadísticas
     • Correlaciones entre variables
     • Valores faltantes y duplicados
     • Alertas y recomendaciones

<h5>7️⃣ <b>Opción 4: EDA Diagnóstico</b></h5>

   - Análisis profundo del dataset unificado
   - Proceso de limpieza y preparación de datos
   - Generación de visualizaciones avanzadas:
     • Matrices de correlación
     • Series temporales de ventas
     • Análisis de outliers
     • Rankings y patrones de venta
   - Guardado automático de gráficos en `assets/plots`

<h5>8️⃣ <b>Opción: Preprocesamiento ML</b></h5>

  - Permitir seleccionar objetivo (`target`) y variables predictoras.
  - Opciones interactivas de preprocesamiento:
    - Manejo de nulos: imputación por media/mediana/moda.
    - Codificación de categóricas: `one-hot` o `ordinal`.
    - Escalado de numéricos: `StandardScaler` o `MinMaxScaler`.
    - Selección de features (filtro o métodos automáticos).
  - Configurar `train/test split` y semilla (seed).
  - Mostrar resumen del dataset preprocesado y permitir exportarlo como CSV.

<h5>9️⃣ <b>Opción: AutoML (Benchmark)</b></h5>

  - Cargar dataset preprocesado.
  - Inicializar experimento con PyCaret: `setup()` indicando `target`, `normalize`, `session_id`, etc.
  - Ejecutar `compare_models()` para obtener ranking por la métrica escogida (AUC/Accuracy/RMSE según caso).
  - Mostrar top-N modelos, métricas y gráficos comparativos.
  - Permitir guardar el mejor modelo y exportar su configuración.

<h5>1️⃣0️⃣ <b>Opción: Entrenamiento Manual (Random Forest)</b></h5>

  - Cargar dataset preprocesado.
  - Permitir ajuste interactivo de hiperparámetros (p. ej. `n_estimators`, `max_depth`, `class_weight`).
  - Entrenar modelo (clasificador o regresor según el objetivo).
  - Evaluar en conjunto de test: matriz de confusión, curva ROC, AUC, Accuracy, MAE/RMSE, reporte por clases.
  - Mostrar importancia de variables (`feature_importances_`) y curvas de aprendizaje.
  - Guardar modelo entrenado (`joblib`/`pickle`) y ofrecer descarga.

<h5>1️⃣1️⃣ <b>Opción: Dashboard Ejecutivo</b></h5>

  - Presentar KPIs principales en una vista ejecutiva: Ticket Promedio, Total de Ventas, Unidades vendidas, % Top10, Promedio móvil.
  - Ofrecer vistas por sección: 
      • Ventas: tendencia, ventas por categoría, ranking de productos
      • Clientes: ventas por ciudad, ticket promedio, clientes activos
      • Productos: rotación, stock crítico, top N por ventas
  - Añadir filtros globales: rango de fechas, categoría y ciudad (aplican a todas las vistas).
  - Permitir exportación: descargar CSV del dataset filtrado, descargar gráficos (PNG) y generar reporte (PDF/imagen).
  - Guardar imágenes y figuras en `assets/plots` y permitir descarga directa.

<h5>1️⃣2️⃣ <b>Opción: Ver Documentación</b></h5>

   - Lectura y procesamiento de `documentacion_tienda_aurelion.md`
   - Contenido organizado en expanders por secciones:
     • Contexto y objetivo
     • Datasets y metodología
     • Pseudocódigo
     • Diagrama de flujo
   - Visualización adaptativa del flujograma

<h5>1️⃣3️⃣ <b>Interactividad</b></h5>

   - Los **expanders** permiten ocultar o desplegar secciones para una interfaz más limpia.  
   - Los **selectboxes** ofrecen navegación dinámica entre datasets y apartados.  
   - La aplicación combina usabilidad y claridad visual para una exploración fluida de los datos.

---

### Pseudocódigo

```text
INICIO

1. Configurar la página de Streamlit:
    - Título: "Tienda Aurelion"
    - Ícono de la página
    - Layout: ancho completo ("wide")

2. Mostrar encabezado principal:
    - Crear dos columnas (1 y 4 proporciones)
    - Columna 1: mostrar logo de la tienda desde ./assets/logo_aurelion.png
    - Columna 2: mostrar título del proyecto y descripción general

3. Definir funciones de carga y unificación:
    FUNCIÓN get_dataset_paths():
        Retornar diccionario con rutas de:
            - clientes.xlsx
            - productos.xlsx
            - ventas.xlsx
            - detalle_ventas.xlsx
            - df_tienda_aurelion.csv

    FUNCIÓN load_dataset(nombre):
        - Obtener rutas mediante get_dataset_paths()
        - SI el nombre es "df_tienda_aurelion" y no existe:
            Llamar a load_and_merge_datasets()
        - SI es un archivo Excel:
            Leer con pandas.read_excel()
        - SI es un archivo CSV:
            Leer con pandas.read_csv()
        - Manejar errores y mostrar mensajes de advertencia

    FUNCIÓN load_and_merge_datasets():
        - Cargar los 4 datasets Excel
        - Realizar fusión progresiva:
            1. clientes + ventas
            2. ventas + clientes
            3. detalle_ventas + productos
            4. fusión final
        - Calcular total_venta y convertir fechas
        - Guardar como CSV
        - Retornar DataFrame unificado

4. Definir utilidades de visualización:
    FUNCIÓN save_fig_to_disk(figura, nombre, carpeta="assets/plots"):
        - Crear la carpeta si no existe
        - Limpiar nombre del archivo
        - Guardar figura con calidad apropiada

    FUNCIÓN mostrar_fig(figura, ancho=700):
        - Mostrar en Streamlit
        - Opcionalmente guardar en disco
        - Cerrar figura

5. Crear menú lateral con opciones:
    - "Información general"
    - "Estadísticas"
    - "EDA Automatizado"
    - "EDA Diagnóstico"
    - "Preprocesamiento ML"
    - "ML Automatizado"
    - "Entrenamiento Random Forest"
    - "Dashboard Ejecutivo"
    - "Ver documentación"

6. SI la opción es "Información general":
    - Mostrar selectbox con datasets disponibles
    - Para el dataset seleccionado mostrar:
        - Fecha y tamaño del archivo
        - Vista previa (head)
        - Estructura (tipos de columnas)
        - Cantidad de registros

7. SI la opción es "Estadísticas":
    - Permitir seleccionar dataset
    - Mostrar:
        - Información general del dataset
        - Valores nulos por columna
        - Valores únicos por columna
        - Estadísticas descriptivas (describe)
        - Matriz de correlación (si hay numéricas)
        - Visualizaciones específicas según el dataset

8. SI la opción es "EDA Automatizado":
    - Cargar/generar df_tienda_aurelion
    - Crear ProfileReport con ydata-profiling
    - Mostrar en Streamlit con st_profile_report

9. SI la opción es "EDA Diagnóstico":
    - Cargar df_tienda_aurelion
    - Verificar unificación exitosa
    - Realizar limpieza básica:
        • Convertir fechas a datetime
        • Renombrar columnas si necesario
        • Eliminar columnas duplicadas
    - Generar y guardar visualizaciones
    - Mostrar interpretación de resultados

10. SI la opción es "Preprocesamiento ML":
    - Seleccionar objetivo (target) y variables predictoras
    - Mostrar y aplicar opciones de preprocesamiento:
      • Manejo de nulos: imputación (media/mediana/moda)
      • Codificación de categóricas: one-hot / ordinal
      • Escalado de numéricos: StandardScaler / MinMax
      • Selección de características (opcional)
    - Mostrar split train/test configurable (p. ej. 80/20) y semilla
    - Retornar datasets: X_train, X_test, y_train, y_test

11. SI la opción es "AutoML (Benchmark)":
    - Usar PyCaret (o librería similar) para benchmarking automático
    - Pasos:
      - Cargar dataset preprocesado
      - Inicializar setup con target y métricas relevantes
      - Comparar modelos (compare_models)
      - Mostrar top N modelos y métricas (AUC, Accuracy, RMSE según caso)
      - Permitir seleccionar mejor modelo y guardar configuración

12. SI la opción es "Entrenamiento Manual (Random Forest)":
    - Cargar dataset preprocesado
    - Permitir selección de hiperparámetros (n_estimators, max_depth, random_state)
    - Entrenar modelo RandomForestClassifier/Regressor según el caso
    - Evaluar modelo en test set (matriz de confusión, AUC, accuracy, MAE/RMSE)
    - Mostrar interpretación de importancia de características (feature_importances_)
    - Guardar modelo entrenado (`joblib` / `pickle`) y permitir descarga

13. SI la opción es "Dashboard Ejecutivo":
    - Cargar datasets y/o df_tienda_aurelion agregados
    - Generar KPIs principales: Ticket Promedio, Total Ventas, Unidades, % Top10, Promedio móvil
    - Crear vistas por sección:
        • Ventas: tendencia, ventas por categoría, ranking de productos
        • Clientes: ventas por ciudad, ticket promedio, clientes activos
        • Productos: rotación, stock crítico, top N por ventas
    - Añadir filtros globales (rango de fechas, categoría, ciudad)
    - Implementar opciones de exportación (descarga de gráficos, exportar CSV, generar reporte PDF/imagen)
    - Ofrecer réplica de vistas principales del Dashboard de Power BI (KPIs + vistas principales)
    - Guardar imágenes y figuras en `assets/plots` y permitir descarga

14. SI la opción es "Ver documentación":
    - Verificar existencia de documentacion_tienda_aurelion.md
    - SI existe:
        - Leer contenido y dividir en secciones
        - Mostrar cada sección en expander
        - Mostrar diagrama de flujo centrado
    - SINO:
        - Mostrar advertencia

15. Mostrar pie de página (footer):
    - Información del Sprint
    - Autor y enlace a LinkedIn

FIN

```

---


### Diagrama del flujo

A continuación, se presenta el flujograma del proceso general del proyecto **Tienda Aurelion**.  
Este diagrama ilustra las principales etapas del flujo del programa, desde la carga de los datasets hasta la visualización interactiva de la información en la aplicación web.

<p align="center">
  <img src="../assets/flujograma_aurelion.png" alt="Flujograma Tienda Aurelion" width="600">
</p>

---

### Interpretaciones EDA – Visualizaciones

Esta sección describe las principales visualizaciones generadas automáticamente por la aplicación, junto con su interpretación.
Cada gráfico se encuentra guardado en la carpeta plots/ y se muestra en la sección de estadísticas del dashboard.

#### 🔸 Gráfica: distribucion_numericas

A continuación, se detallan las explicaciones correspondientes a cada una de las variables analizadas.

| Variable            | Descripción visual                                                  | Patrón observado                                                                                                                                             | Interpretación                                                                                                               |
| ------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **cantidad**        | Eje X: cantidad (1 a 5) <br> Eje Y: frecuencia (hasta ~85)          | • Las cantidades más frecuentes son 2 y 4, con picos cercanos a 80 y 70 respectivamente. <br> • Las demás cantidades (1, 3 y 5) tienen frecuencias similares, alrededor de 60. | Distribución discreta y relativamente uniforme, con un pico notable en **cantidad = 2**. La dispersión es baja.               |
| **precio_unitario** | Eje X: precio_unitario (0 a 5000) <br> Eje Y: frecuencia (hasta 60) | • Asimétrica, con concentración entre **1500 y 2500**. <br> • Pico cerca de **2000**. <br> • Pocos valores en extremos (<500 y >4000).                       | La mayoría de los productos se venden en un rango medio de precios, con pocos productos en rangos muy altos.         |
| **total_venta**     | Eje X: total_venta (0 a 25000) <br> Eje Y: frecuencia (hasta 60)    | • Distribución **sesgada a la derecha**. <br> • Alta concentración entre **0 y 10,000**, con pico entre **3,000–5,000**. <br> • Pocos casos >20,000.         | La mayoría de las ventas son bajas o moderadas; las muy altas son raras, indicando posibles *outliers* en el extremo derecho. |


#### 🔸 Gráfica: correlacion

**Variables analizadas:**
* cantidad
* precio_unitario
* total_venta

**Principales resultados:**
1. cantidad vs precio_unitario
- Correlación: -0.074 (muy baja y negativa). No existe relación significativa entre la cantidad vendida y el precio unitario. Es decir, vender más unidades no implica que el precio sea mayor o menor.

2. cantidad vs total_venta:
- Correlación: 0.6 (moderada y positiva). A mayor cantidad, tiende a aumentar el total de venta, lo cual es lógico porque más unidades generan más ingresos, aunque no es una relación perfecta.

3. precio_unitario vs total_venta:
- Correlación: 0.68 (moderada-alta y positiva). El precio unitario tiene una influencia importante en el total de venta. Productos más caros tienden a generar ventas totales más altas, incluso si la cantidad no varía mucho.

#### 🔸 Gráfica: ventas_total_por_mes

El gráfico muestra la evolución de las ventas mensuales entre enero 2024 y junio 2024.
Se observa una tendencia fluctuante, con una caída marcada en abril y una recuperación fuerte en mayo.

Resultados clave:

* **Máximo**
  - Mes: mayo 2024 - Valor: 561,832
  - Este fue el mejor mes en ventas, superando el promedio por un amplio margen.

* **Mínimo**
  - Mes: abril 2024 - Valor: 251,524
  - Abril fue el peor mes, con ventas muy por debajo del promedio.

* **Promedio**
  - Línea horizontal: 441,903 
  - Tres meses (enero, mayo y junio) estuvieron por encima del promedio, mientras que febrero, marzo y abril quedaron por debajo.

Tendencias específicas:
- Enero (529,840): Buen inicio, por encima del promedio.
- Febrero y Marzo: Descenso progresivo (407,041 → 388,263).
- Abril: Caída abrupta al mínimo (251,524).
- Mayo: Recuperación fuerte al máximo (561,832).
- Junio: Ligera baja respecto a mayo, pero sigue alto (512,917).

> Las ventas son volátiles, con un mínimo crítico en abril y un máximo en mayo.
El promedio indica que la tienda tiene un buen desempeño general, pero necesita analizar qué causó la caída en abril y el repunte en mayo (promociones, estacionalidad, campañas).

#### 🔸 Gráfica: relacion_cantidad

Diagrama de dispersión con:
- Eje X: cantidad (de 1 a 5 unidades).
- Eje Y: total_venta (hasta 25,000).
- Incluye una línea de tendencia ascendente y un valor de correlación: 0.60.

Resultados clave:
1. Correlación positiva moderada (0.60): Indica que a mayor cantidad vendida, mayor es el total de venta, aunque no es una relación perfecta.
Esto es lógico: más unidades generan más ingresos, pero hay variabilidad por el precio unitario.

2. Patrón de dispersión: Para cada cantidad (1 a 5), hay una amplia dispersión en el total de venta.
Ejemplo:
   - Cantidad = 1 → ventas entre ~1,000 y ~5,000.
   - Cantidad = 5 → ventas entre ~5,000 y >20,000.
El precio unitario influye mucho en el total, incluso con la misma cantidad.

3. Tendencia general: La línea de regresión muestra un incremento consistente: más cantidad tiende a aumentar el total de venta.

> Existe una relación clara entre cantidad y total de venta, pero no es determinante por sí sola.
El precio unitario es un factor adicional que explica la dispersión.
Para aumentar ventas totales, incrementar la cantidad ayuda, pero también es clave considerar el mix de productos y precios.

#### 🔸 Gráfica: outliers

A continuación se resumen los resultados de los gráficos de outliers agrupados por tipo de variable.

| Variable            | Rango observado                     | Mediana / Forma de la distribución                                                    | Interpretación                                                                                          |
|--------------------|--------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **cantidad**        | 1 a 5                                | Mediana ≈ 3; distribución simétrica; sin outliers relevantes                           | Las cantidades vendidas suelen estar entre 2 y 4; pedidos consistentes sin valores atípicos significativos. |
| **precio_unitario** | ~500 a 5000                          | Mediana ≈ 2500; distribución equilibrada; algunos puntos fuera del rango               | Los precios se concentran en el rango medio, aunque existen productos con precios extremos.              |
| **total_venta**     | 0 a >20,000                          | Mediana ≈ 8000; distribución sesgada a la derecha; múltiples outliers                  | La mayoría de las ventas son bajas o medias, pero existen transacciones extraordinarias que elevan el máximo. |


---

### Preprocesamiento para Machine Learning

1️⃣ **Objetivo**
    
Preparar el dataset para entrenar modelos de clasificación que predigan el nivel de demanda de cada producto a partir de métricas agregadas de ventas.

2️⃣ **Metodología aplicada**

🔸 Agrupación por producto
  - Dataset original: 343 transacciones individuales
  - Dataset agrupado: 95 productos únicos

🔸 Variables creadas:
  - `total_unidades`: Suma de unidades vendidas por producto
  - `total_ventas`: Ingreso total generado por producto
  - `cant_transacciones`: Número de ventas únicas
  - `precio_promedio`: Precio unitario promedio
  - `ventas_por_transaccion`: Ingreso promedio por transacción
  - `unidades_por_transaccion`: Unidades promedio por transacción

🔸 **Variable objetivo**: `Nivel de demanda`

  Basada en percentiles de `total_unidades`:

  | Categoría     | Rango         | Cantidad de productos |
  | ------------- | ------------- | --------------------- |
  | **Baja (0)**  | ≤ 8 unidades  | 38                    |
  | **Media (1)** | 8–12 unidades | 27                    |
  | **Alta (2)**  | > 12 unidades | 30                    |

  Distribución balanceada y adecuada para clasificación multiclase.

🔸 Transformaciones aplicadas
  - One-Hot Encoding de `categoria_corregida` (10 categorías)
  - Eliminación de `nombre_producto` por alta cardinalidad
  - Mapping del target:
     - baja → 0
     - media → 1
     - alta → 2

3️⃣ **Resultados del preprocesamiento**
   
  🔹 Consistencia verificada: la suma original (1016) coincide con la suma agrupada (1016).

  🔹 Balance de clases: Distribución equilibrada (30 / 27 / 38 productos por categoría)

  🔹 Dataset final: 95 productos × 18 variables listas para el modelado.

---

### AutoML: Benchmarking con PyCaret

1️⃣ **Objetivo**
  
Identificar automáticamente el modelo de clasificación con mejor desempeño para predecir el nivel de demanda de productos.

2️⃣ **Configuración del experimento**

El experimento se ejecutó con PyCaret utilizando las siguientes configuraciones:
  - **Normalización**: Activada
  - **Remoción de multicolinealidad**: Activada  
  - **Split train/test**: 69%/31%
  - **Cross-validation**: 10 folds
  - **Seed (session_id)**: 789
  - **Métrica principal (sort)**: AUC

3️⃣ **Resultados de la comparación**

Los modelos fueron ordenados por AUC (métrica seleccionada en `compare_models`).

  🔸 **Top 5 modelos según AUC**

  | Modelo | Accuracy | AUC | F1-Score | Tiempo (s) |
  |--------|----------|-----|----------|------------|
  | Random Forest | 0.9857 | 0.9971 | 0.9848 | 0.120 |
  | AdaBoost | 0.9857 | 0.9943 | 0.9848 | 0.070 |
  | Gradient Boosting | 0.9857 | 0.9943 | 0.9848 | 0.119 |
  | Decision Tree | 0.9857 | 0.9900 | 0.9848 | 0.023 |
  | LightGBM | 0.9381 | 0.9943 | 0.9270 | 0.127 |

4️⃣ **Modelo seleccionado**
   
  **Random Forest Classifier** - Mejor desempeño general con:
    
  - **Accuracy**: 98.57%
  - **AUC**: 99.71% 
  - **F1-Score**: 98.48%

  🔸 **Interpretación**
    
  - Los modelos de ensemble (Random Forest, AdaBoost, Gradient Boosting) dominan el ranking
  - El desempeño general es excelente, con valores de AUC superiores al 99%.
  - Los tiempos de entrenamiento fueron muy bajos, adecuados para datasets pequeños como este.
  - El modelo seleccionado presenta una excelente capacidad predictiva y estabilidad.

---

### Entrenamiento Manual: Random Forest

<h5>1️⃣ <b>Objetivo</b></h5>
    
Implementar manualmente un modelo Random Forest Classifier para predecir el nivel de demanda de productos, evaluando su desempeño mediante validación cruzada, métricas de test, curva ROC multiclase, matriz de confusión, curva de aprendizaje e importancia de variables.

Este enfoque permite obtener un modelo transparente, reproducible y completamente controlado por el analista, ideal para evaluar real capacidad de generalización.

<h5>2️⃣ <b>Configuración del modelo</b></h5>

El modelo fue configurado manualmente en la aplicación Streamlit con los siguientes parámetros:

🔹 Algoritmo

- **Random Forest Classifier**

🔹 Hiperparámetros seleccionados

- **n_estimators**: 200
- **max_depth**: 15
- **min_samples_split**: 5
- **min_samples_leaf**: 2
- **max_features**: "sqrt"
- **class_weight**: "balanced"
- **random_state**: 789

🔹 Configuración del entrenamiento

- **Test size**: 31% (idéntico a PyCaret para una comparación justa)
- **Balanceo de clases**: Activado
- **Validación cruzada**: 5 folds (definido dinámicamente según el tamaño del dataset)
- **Dataset usado**: 95 productos procesados

<h5>3️⃣ <b>Métricas de evaluación</b></h5>

  🔸 **Validación Cruzada (5 folds)**
  
  Durante la validación cruzada, el modelo obtuvo:

  - **Accuracy promedio**: 0.6526
  - **F1-Score promedio**: 0.6320

  Estos valores reflejan un rendimiento moderado, adecuado para un dataset pequeño.
  
  🔸 **Métricas en el Conjunto de Test**
    
  | Métrica | Valor |
  |---------|-------|
  | Accuracy | 0.6000 |
  | Precision | 0.5857 |
  | Recall | 0.6000 |
  | F1-Score | 0.5900 |

  El modelo mantiene consistencia entre validación cruzada y test, indicando  comportamiento estable, aunque con margen de mejora.
  
  🔸 **Curva ROC Multiclase (One-vs-Rest)**
  
  - **AUC Macro**: 0.8433
  - **Clase 0 (Baja demanda)**: AUC = 0.92
  - **Clase 1 (Media demanda)**: AUC = 0.75  
  - **Clase 2 (Alta demanda)**: AUC = 0.86 

  La clase “Media” es la más difícil de separar, algo esperable por su posición   intermedia entre “Baja” y “Alta”.

<h5>4️⃣ <b>Análisis de resultados</b></h5>

  🔸 **Matriz de Confusión**
  
  La matriz evidencia:

  - Buen desempeño en clase 0 (baja) y clase 2 (alta).
  - Alta confusión en la clase 1 (media), consistente con el Recall=0.333 observado.

  Este comportamiento se debe a la naturaleza del problema: la clase media es más ambigua y con menor soporte.

  🔸 **Importancia de variables**
    
  **Top 5 features más importantes**:
    
  1. `cant_transacciones` (0.4151)
  2. `id_producto` (0.1534) 
  3. `precio_promedio` (0.1517)
  4. `ventas_por_transaccion` (0.1355)
  5. `categoria_Higiene personal` (0.0224)

  Los resultados destacan la importancia del volumen de operaciones y precio promedio, variables clave para entender la demanda.

<h5><b>Classification Report por clase</b></h5>

  | Clase | Precision | Recall | F1-Score |
  |-------|-----------|--------|----------|
  | Baja (0) | 0.714 | 0.833 | 0.769 |
  | Media (1) | 0.375 | 0.333 | 0.353 |
  | Alta (2) | 0.625 | 0.556 | 0.588 |

  La clase “Media” continúa siendo la más débil; se beneficiaría de más datos o técnicas de oversampling futuro.

<h5><b>Curva de aprendizaje</b></h5>

La curva de aprendizaje muestra:
- Brecha moderada entre entrenamiento y validación
- Sin señales de overfitting extremo
- Mejoras observables al aumentar el tamaño del dataset

Conclusión: el modelo generaliza razonablemente bien, pero sería beneficioso entrenarlo con más datos.

<h5>5️⃣ <b>Conclusiones generales</b></h5>

**Comparativa: AutoML vs Random Forest Manual**
  
  | Aspecto | AutoML (PyCaret) | RF Manual |
  |---------|------------------|-----------|
  | Accuracy Test | 98.57% | 60.00% |
  | AUC Macro | 99.71% | 84.33% |
  | Configuración | Automática | Manual optimizado |
  | Interpretabilidad | Media | Alta |
  | Generalización | Potencial overfitting | Más Realista |

 Interpretación

- PyCaret logra métricas extremadamente altas gracias a un preprocesamiento y tuning intensivo.
- El RF Manual, aunque menos preciso, es más interpretable y más honesto respecto a la generalización real.
- En datasets pequeños como este, el modelo manual suele reflejar mejor el rendimiento esperado en producción.

<h5>6️⃣ <b>Recomendaciones para producción</b></h5>
    
1. **Modelo sugerido**: 
    - Random Forest Manual → Mayor generalización y transparencia.
    - PyCaret puede usarse como benchmark o para análisis exploratorio.
2. **Variables clave**:
    - Cantidad de transacciones
    - Precio promedio
    - Ventas por transacción

3. **Puntos a monitorear**:
    - Desempeño sobre la clase Media
    - Distribuciones de demanda ante cambios estacionales

4. **Mejoras futuras**
    - Recolectar más datos
    - Aplicar oversampling (SMOTE)
    - Probar embeddings o técnicas de reducción de dimensionalidad
    - Ajustar hiperparámetros adicionales

<h5>7️⃣ <b>Impacto para el Negocio</b></h5>

El modelo desarrollado permite:

- Identificar productos de alta rotación para evitar ruptura de stock
- Detectar baja demanda para optimizar compras e inventario
- Planificar abastecimiento con mayor precisión
- Incrementar rentabilidad ajustando órdenes según nivel de demanda esperado

Este enfoque ayuda a tomar decisiones estratégicas en gestión de inventario, compras y planificación comercial.

---



### Dashboard Ejecutivo

#### 🔸 Dashboard

1️⃣ **Objetivo**

Se desarrolló un Dashboard Ejecutivo con el objetivo de replicar funcional y visualmente el dashboard previamente construido en Power BI, manteniendo los mismos indicadores clave (KPIs), estructura analítica y lógica de navegación, pero implementado dentro del ecosistema de la aplicación Tienda Aurelion.

El propósito principal de este dashboard es brindar una visión sintética y estratégica del desempeño del negocio, orientada a la toma de decisiones gerenciales, permitiendo analizar ventas, clientes y productos durante el primer semestre de 2024 (Enero–Junio).

2️⃣ **Enfoque y criterios de diseño**

El dashboard fue diseñado bajo los siguientes lineamientos:

- Replicar los KPIs definidos en Power BI, asegurando consistencia en métricas, cálculos y resultados.
- Mantener una estructura modular, separando el análisis en tres vistas principales:
  - Análisis de Ventas
  - Análisis de Clientes
  - Análisis de Productos
- Priorizar una lectura ejecutiva, con indicadores agregados, gráficos claros y mensajes de insight destacados.
- Incorporar filtros globales (mes, categoría) para facilitar el análisis dinámico.
- Utilizar una navegación simple e intuitiva, simulando la experiencia de un dashboard corporativo.

3️⃣ **Valor del Dashboard Ejecutivo**

El Dashboard Ejecutivo consolida información crítica del negocio en un único entorno visual, logrando:

- Reproducir fielmente el dashboard de Power BI en términos de métricas y análisis.
- Facilitar la toma de decisiones estratégicas a partir de información clara y accionable.
- Integrar análisis descriptivo con indicadores de gestión y alertas operativas.
- Servir como base para futuras extensiones analíticas y modelos predictivos.

#### 🔸 Réplicas de Vistas

1️⃣ **Vista Principal del Dashboard en Power BI**

En el dashboard original desarrollado en Power BI, la vista principal funciona como un contenedor de navegación, desde el cual se accede a distintas páginas analíticas (Ventas, Clientes y Productos), todas ellas compartiendo filtros y contexto temporal.

La cual incluía:
- Identidad visual de la marca Aurelion Retail Supermarket.
- Título general del informe: “Diagnóstico de rotación y comportamiento del mercado – H1 2024”
- Accesos directos a las tres secciones analíticas:
  - Análisis de Ventas
  - Análisis de Clientes
  - Análisis de Productos

Esta vista permitía al usuario comprender rápidamente el alcance del análisis y navegar hacia el nivel de detalle requerido.

En la aplicación Tienda Aurelion, esta lógica fue replicada conceptualmente, pero adaptada al paradigma de navegación de Streamlit, donde:
- No existe una “portada visual” única con KPIs consolidados.
- La vista principal se materializa como un conjunto de páginas analíticas independientes, accesibles desde el sidebar, cada una equivalente a una página del dashboard de Power BI.

De esta forma, la aplicación mantiene la misma estructura analítica, pero distribuida en tres páginas funcionales.

2️⃣ **Análisis de Ventas**

La sección de Análisis de Ventas presenta los principales indicadores de desempeño comercial:

KPIs principales:
- Ticket Promedio (con variación porcentual)
- Cantidad de Transacciones (con variación porcentual)
- Total de Ventas
- Promedio Móvil de Ventas (3 meses)

Visualizaciones incluidas:
- Tendencia de ventas mensuales con promedio móvil.
- Ventas totales por categoría de producto.
- Ranking de productos por total de ventas.

Mensajes de insight automático, como:
- “El mes con mayor crecimiento fue mayo”
- “Alimentos secos representa la categoría de mayor impacto”

Esta vista permite identificar patrones temporales, categorías dominantes y productos de mayor contribución al revenue.

3️⃣ **Análisis de Clientes**

La sección de Análisis de Clientes está orientada a comprender el comportamiento de compra y la distribución geográfica de las ventas.

KPIs principales:
- Total de clientes
- Ticket promedio
- Unidades promedio por transacción

Visualizaciones incluidas:
- Ventas totales por ciudad.
- Tabla comparativa por ciudad con:
  - Cantidad de clientes
  - Ticket promedio
  - Total de ventas
- Distribución de ventas por medio de pago (efectivo, QR, transferencia y tarjeta).

Esta vista permite detectar diferencias regionales, hábitos de consumo y preferencias de pago.

4️⃣ **Análisis de Productos**

La sección de Análisis de Productos se enfoca en la rotación, concentración de ventas y riesgo de stock.

KPIs principales:
- Total de unidades vendidas
- Ventas promedio por producto
- Precio unitario promedio
- Porcentaje de concentración del Top 10 de productos
- KPI de concentración de valor con meta definida (0,40)

Elementos clave:
- Identificación del producto TOP en unidades vendidas.
- Clasificación de productos según:
  - Alta rotación
  - Riesgo de exceso de stock
- Tabla de productos con alerta de stock (alta demanda, normal, riesgo de exceso).
- Ranking de productos más vendidos.

Esta vista permite apoyar decisiones relacionadas con abastecimiento, optimización de inventario y foco comercial.

#### 🔸 Conclusiones

**Interpretación del Dashboard**

El Dashboard Ejecutivo fue diseñado como una herramienta de apoyo a la toma de decisiones operativas, con foco en el equilibrio entre demanda y stock, principal problemática identificada en la Tienda Aurelion.

1️⃣ **Ventas**

El análisis de ventas permite comprender la dinámica general del negocio y validar la estabilidad de la demanda.
La tendencia mensual muestra un comportamiento variable, con una caída puntual en abril y una recuperación sostenida en mayo y junio, lo que evidencia la necesidad de ajustes dinámicos de reposición según el período.

El predominio de categorías de consumo masivo confirma que el negocio depende del volumen de ventas más que de márgenes unitarios elevados, reforzando la importancia de evitar rupturas de stock en productos clave.

2️⃣ **Clientes**

El análisis de clientes aporta contexto para segmentar decisiones comerciales y de reposición.
Las ventas por ciudad muestran diferencias claras tanto en volumen como en ticket promedio, lo que habilita estrategias diferenciadas para mover stock excedente hacia zonas con mayor capacidad de gasto.

El análisis de medios de pago complementa esta visión, aportando información relevante sobre liquidez y costos operativos, sin afectar el foco principal del sistema.

3️⃣ **Productos**

El análisis de productos es central para el objetivo de la aplicación. El volumen total vendido y la venta promedio por producto indican una alta rotación general, aunque no homogénea entre todos los ítems.

La concentración de ventas del Top 10, junto con el KPI de concentración de valor por debajo del umbral recomendado, muestra una cartera diversificada, lo que reduce el riesgo comercial. Sin embargo, la detección de 43 productos en riesgo de exceso de stock, incluyendo productos sin ventas durante el semestre, expone un problema concreto de sobreabastecimiento.

Esta información permite priorizar productos críticos, ajustar niveles de compra y definir acciones específicas sobre los ítems de baja rotación, alineándose directamente con el objetivo de reducir costos de inventario.

4️⃣ **Conclusión**

En conjunto, el dashboard cumple el objetivo de transformar datos históricos en información accionable, permitiendo:
- Detectar productos con riesgo de ruptura o exceso de stock.
- Priorizar productos de alta rotación.
- Ajustar decisiones de compra y reposición según demanda real y contexto geográfico.
- Reducir costos asociados al inventario inmovilizado.

De  esta manera, la aplicación funciona como un soporte analítico integral para mejorar la eficiencia operativa y la rentabilidad del negocio.