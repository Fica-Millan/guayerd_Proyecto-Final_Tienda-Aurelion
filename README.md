<p align="center">
  <img src="assets/logo_aurelion.png" width="60%" />
</p>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)

![Status](https://img.shields.io/badge/Status-Terminado-green)
![Author](https://img.shields.io/badge/Autor-Yesica%20Fica%20Mill%C3%A1n-purple)

</div>


# Proyecto Tienda Aurelion

## 🟧 Descripción
Este proyecto consiste en una aplicación interactiva llamada **Tienda Aurelion**, desarrollada en Python utilizando **Streamlit**. La app permite realizar análisis exploratorio de datos (EDA) sobre las ventas, productos y clientes de la tienda y cuenta con un **Dashboard Ejecutivo** (réplica interactiva tipo Power BI) que muestra KPIs clave (ventas, ticket promedio, transacciones y clientes), filtros globales y visualizaciones interactivas construidas con **Plotly**, además de opciones para exportar imágenes y datos. Complementa esto con EDA automatizado y funcionalidades de Machine Learning (preprocesamiento, AutoML y entrenamiento manual con Random Forest).

## 🟧 Características principales

- **Información General**: Vista previa y detalles de cada dataset.
- **Estadísticas**: Análisis descriptivo con visualizaciones personalizadas.
- **EDA Automatizado**: Perfilado completo del dataset unificado usando `ydata-profiling`.
- **EDA Diagnóstico**: Análisis detallado con:
  - Detección de outliers
  - Matrices de correlación
  - Series temporales de ventas
  - Top productos por categoría
  - Visualizaciones guardadas automáticamente
- **Preprocesamiento ML**: Interfaz para preparar datos (imputación, codificación, escalado, selección de features y exportación).
- **AutoML (PyCaret)**: Benchmark automático de modelos y exportación del mejor modelo.
- **Entrenamiento Manual (Random Forest)**: Entrenamiento, evaluación y exportación de modelos.
- - **Dashboard Ejecutivo**: Panel interactivo (tipo Power BI) con KPIs clave (ventas, ticket promedio, transacciones y clientes), filtros globales (fechas, ciudades, categorías, medios de pago y rango de ticket), y visualizaciones interactivas.
- **Documentación**: Acceso a la documentación técnica del proyecto.

## 🟧 Estructura del proyecto

```
├── main.py                       # Entrada de la app Streamlit y routing de páginas
│
├── assets/                       # Recursos estáticos (imágenes, logos, iconos)
│   └── plots/                    # Visualizaciones generadas por la app (PNG)
│
├── data/                         # Datasets del proyecto
│   ├── clientes.xlsx             # Datos maestros de clientes
│   ├── productos.xlsx            # Catálogo y atributos de productos
│   ├── productos_corregidos.xlsx # 
│   ├── ventas.xlsx               # Registro de ventas por transacción
│   ├── detalle_ventas.xlsx       # Detalle por línea de venta (productos por venta)
│   ├── df_tienda_aurelion.csv    # Dataset unificado (generado automáticamente)
│   ├── df_tienda_aurelion_modificado.csv  # Versión limpiada / transformada del unificado
│   └── dataset_ml_productos.csv  # Dataset preprocesado para ML (features agregados + target)
│
├── docs/                         # Documentación del proyecto 
│   ├── documentacion_tienda_aurelion.md  # Documentación técnica completa
│   ├── instrucciones.md          # Instrucciones y notas del proyecto
│   └── Sprint02_GrupoA.ipynb     # Notebook del Sprint 02 (trabajo grupal presentado en clase)
│
├── models/                       # Modelos entrenados y serializados
│   ├── auto_ml_model.pkl         # Modelo exportado desde AutoML (PyCaret)
│   └── random_forest_manual.pkl  # Modelo exportado desde entrenamiento manual
│
├── scripts/                      # Scripts auxiliares y utilidades
│   └── preparar_para_powerbi.py  # Script para preparar datos y exportar a Power BI
│
├── src/                          # Módulos Python del proyecto
│   ├── data_loader.py            # Funciones para cargar y unificar los datasets
│   │
│   ├── pages/                    # Páginas de la aplicación (Streamlit)
│   │   ├── automated_eda.py      # Página: EDA automatizado (ydata-profiling)
│   │   ├── automated_ml.py       # Página: AutoML / benchmarking con PyCaret
│   │   ├── dashboard.py          # Página: dashboard ejecutivo con KPIs y visualizaciones interactivas (Plotly)
│   │   ├── diagnostic_eda.py     # Página: EDA diagnóstico y visualizaciones detalladas
│   │   ├── documentacion.py      # Página: muestra la documentación técnica (MD)
│   │   ├── general_info.py       # Página: información general y vistas previas de datasets
│   │   ├── ml_preprocessing.py   # Página: interfaz de preprocesamiento para ML
│   │   ├── random_forest_manual.py # Página: entrenamiento manual y evaluación (Random Forest)
│   │   └── statistics.py         # Página: estadísticas descriptivas y gráficos
│   │
│   └── utils/                    # Utilidades y helpers reutilizables
│       ├── classification.py     # Funciones auxiliares para clasificación y métricas
│       ├── docs_loader.py        # Helpers para leer y dividir documentación MD
│       ├── eda_sections.py       # Componentes y funciones para secciones EDA
│       ├── figures.py            # Generación y guardado de figuras (matplotlib/seaborn)
│       ├── palette.py            # Definición de paleta de colores corporativa
│       ├── rules.py              # Reglas de validación y checks de calidad
│       └── validation.py         # Funciones de validación de datos
│
├── README.md                     # Documentación principal (este archivo)
└── requirements.txt              # Dependencias del proyecto
```

## 🟧 Preparación del entorno

1. Clonar o descargar el repositorio.

2. Crear un entorno virtual (opcional pero recomendado):

```powershell
python -m venv venv
```

3. Activar el entorno virtual:

```powershell
# PowerShell (Windows)
.\venv\Scripts\Activate.ps1

# CMD (Windows)
venv\Scripts\activate.bat

# macOS / Linux
source venv/bin/activate
```

4. Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

## 🟧 Ejecución de la aplicación

Con el entorno virtual activo, ejecutar:

```powershell
streamlit run main.py
```

La aplicación se abrirá en el navegador (por defecto http://localhost:8501). Si tu archivo principal tiene otro nombre, reemplázalo en el comando anterior.

## 🟧 Datasets

La aplicación trabaja con los siguientes datasets:

- `clientes.xlsx`: Información de clientes
- `productos.xlsx`: Catálogo de productos
- `ventas.xlsx`: Registro de ventas
- `detalle_ventas.xlsx`: Detalle de productos vendidos
- `df_tienda_aurelion.csv`: Dataset unificado (generado automáticamente en la primera ejecución)
 
Adicionalmente el proyecto incluye los siguientes archivos derivados/auxiliares en `data/`:

- `productos_corregidos.xlsx`: Archivo corregido y recategorizado (generado por `scripts/preparar_para_powerbi.py`). Para regenerarlo: `python scripts/preparar_para_powerbi.py`.
- `df_tienda_aurelion_modificado.csv`: Versión modificada/limpia del dataset unificado (usada en análisis posteriores).
- `dataset_ml_productos.csv`: Dataset preprocesado y preparado específicamente para modelado (features agregados y target `nivel_demanda`).

Notas:
- Si `df_tienda_aurelion.csv` no existe en la primera ejecución, la aplicación lo creará al ejecutar la opción de carga/unificación.
- `dataset_ml_productos.csv` es el archivo utilizado por las páginas de AutoML y Entrenamiento Manual; si no existe, ejecutar la sección de Preprocesamiento ML para generarlo.

## 🟧 Tecnologías utilizadas

- Python 3.13
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- ydata-profiling (EDA automatizado)
- streamlit-pandas-profiling (integración en Streamlit)
- PyCaret (AutoML / benchmarking)
- scikit-learn (preprocesamiento y modelos)
- Pillow (PIL) para imágenes
- joblib / pickle (serialización de modelos)
- Plotly (dashboard)

Nota: el archivo `requirements.txt` contiene las dependencias pinneadas usadas en el entorno de desarrollo (`venv`).
   
