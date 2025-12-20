# Proyecto Tienda Aurelion

## 📝 Descripción
Este proyecto consiste en una aplicación interactiva llamada **Tienda Aurelion**, desarrollada en Python utilizando **Streamlit**. La app permite realizar análisis exploratorio de datos (EDA) sobre las ventas, productos y clientes de la tienda, ofreciendo visualizaciones interactivas, EDA automatizado y funcionalidades de Machine Learning (preprocesamiento, AutoML y entrenamiento manual con Random Forest).

## 🌟 Características principales

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
- **Documentación**: Acceso a la documentación técnica del proyecto.

## 📁 Estructura del proyecto

```
├── main.py                       # Entrada de la app Streamlit y routing de páginas
│
├── assets/                       # Recursos estáticos (imágenes, logos, iconos)
│   └── plots/                    # Visualizaciones generadas por la app (PNG)
│
├── data/                         # Datasets del proyecto
│   ├── clientes.xlsx             # Datos maestros de clientes
│   ├── productos.xlsx            # Catálogo y atributos de productos
│   ├── ventas.xlsx               # Registro de ventas por transacción
│   ├── detalle_ventas.xlsx       # Detalle por línea de venta (productos por venta)
│   ├── df_tienda_aurelion.csv    # Dataset unificado (generado automáticamente)
│   ├── df_tienda_aurelion_modificado.csv  # Versión limpiada / transformada del unificado
│   └── dataset_ml_productos.csv  # Dataset preprocesado para ML (features agregados + target)
│
├── docs/                         # Documentación del proyecto (MD y notebooks)
│   ├── documentacion_tienda_aurelion.md  # Documentación técnica completa
│   ├── instrucciones.md          # Instrucciones y notas del proyecto
│   └── Sprint02_GrupoA.ipynb     # Notebook del Sprint 02 (trabajo grupal presentado en clase)
│
├── models/                       # Modelos entrenados y serializados
│   ├── auto_ml_model.pkl         # Modelo exportado desde AutoML (PyCaret)
│   └── random_forest_manual.pkl  # Modelo exportado desde entrenamiento manual
│
├── src/                          # Módulos Python del proyecto
│   ├── __init__.py
│   ├── data_loader.py            # Funciones para cargar y unificar los datasets
│   │
│   ├── pages/                    # Páginas de la aplicación (Streamlit)
│   │   ├── __init__.py
│   │   ├── automated_eda.py      # Página: EDA automatizado (ydata-profiling)
│   │   ├── automated_ml.py       # Página: AutoML / benchmarking con PyCaret
│   │   ├── diagnostic_eda.py     # Página: EDA diagnóstico y visualizaciones detalladas
│   │   ├── documentacion.py      # Página: muestra la documentación técnica (MD)
│   │   ├── general_info.py       # Página: información general y vistas previas de datasets
│   │   ├── ml_preprocessing.py   # Página: interfaz de preprocesamiento para ML
│   │   ├── random_forest_manual.py # Página: entrenamiento manual y evaluación (Random Forest)
│   │   └── statistics.py         # Página: estadísticas descriptivas y gráficos
│   │
│   └── utils/                    # Utilidades y helpers reutilizables
│       ├── __init__.py
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

## ⚙️ Preparación del entorno

1. Clonar o descargar el repositorio.

2. Crear un entorno virtual (opcional pero recomendado):

```powershell
python -m venv venv39
```

3. Activar el entorno virtual:

```powershell
# PowerShell (Windows)
.\venv39\Scripts\Activate.ps1

# CMD (Windows)
venv39\Scripts\activate.bat

# macOS / Linux
source venv39/bin/activate
```

4. Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

## 🚀 Ejecución de la aplicación

Con el entorno virtual activo, ejecutar:

```powershell
streamlit run main.py
```

La aplicación se abrirá en el navegador (por defecto http://localhost:8501). Si tu archivo principal tiene otro nombre, reemplázalo en el comando anterior.

## 📊 Datasets

La aplicación trabaja con los siguientes datasets:

- `clientes.xlsx`: Información de clientes
- `productos.xlsx`: Catálogo de productos
- `ventas.xlsx`: Registro de ventas
- `detalle_ventas.xlsx`: Detalle de productos vendidos
- `df_tienda_aurelion.csv`: Dataset unificado (generado automáticamente en la primera ejecución)
 
Adicionalmente el proyecto incluye los siguientes archivos derivados/auxiliares en `data/`:

- `df_tienda_aurelion_modificado.csv`: Versión modificada/limpia del dataset unificado (usada en análisis posteriores).
- `dataset_ml_productos.csv`: Dataset preprocesado y preparado específicamente para modelado (features agregados y target `nivel_demanda`).

Notas:
- Si `df_tienda_aurelion.csv` no existe en la primera ejecución, la aplicación lo creará al ejecutar la opción de carga/unificación.
- `dataset_ml_productos.csv` es el archivo utilizado por las páginas de AutoML y Entrenamiento Manual; si no existe, ejecutar la sección de Preprocesamiento ML para generarlo.

## 🛠️ Tecnologías utilizadas

- Python 3.9
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

Nota: el archivo `requirements.txt` contiene las dependencias pinneadas usadas en el entorno de desarrollo (`venv39`).
   