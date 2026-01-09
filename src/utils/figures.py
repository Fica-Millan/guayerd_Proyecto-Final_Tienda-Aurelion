# src/utils/figures.py

import io
from pathlib import Path
import matplotlib.pyplot as plt
import streamlit as st
import unicodedata
import re

# ==============================================================
# 🟦 Funciones auxiliares
# ==============================================================
def ensure_dir(folder):
    """
    Garantiza la existencia de un directorio en el sistema de archivos.

    Si el directorio no existe, lo crea junto con cualquier subcarpeta
    necesaria.

    Parámetros:
    - folder (str | Path): Ruta del directorio a crear o validar.

    Retorna:
    - Path: Objeto Path correspondiente al directorio.
    """
    folder_path = Path(folder)
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path

def clean_filename(text):
    """
    Normaliza un texto para su uso seguro como nombre de archivo.

    Elimina acentos y caracteres especiales, y reemplaza caracteres
    no válidos por guiones bajos.

    Parámetros:
    - text (str): Texto original a normalizar.

    Retorna:
    - str: Nombre de archivo limpio y compatible con sistemas de archivos.
    """
    
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9_-]", "_", text)
    return text.strip("_")

# ==============================================================
# 🟦 Guardar figuras
# ==============================================================
def save_fig_to_disk(fig, name=None, folder="assets/plots", dpi=120, fmt="png"):
    """
    Guarda una figura de Matplotlib en disco con un nombre normalizado.

    Si no se especifica un nombre, se utiliza el título del gráfico
    como identificador del archivo.

    Parámetros:
    - fig (matplotlib.figure.Figure): Figura a guardar.
    - name (str, opcional): Nombre base del archivo (sin extensión).
    - folder (str): Directorio de destino.
    - dpi (int): Resolución de la imagen.
    - fmt (str): Formato de salida (por ejemplo, 'png').

    Retorna:
    - Path: Ruta completa del archivo guardado.
    """
    
    folder_path = ensure_dir(folder)

    if name is None:
        ax = fig.axes[0] if fig.axes else None
        name = ax.get_title() if ax and ax.get_title() else "plot"
    
    name = clean_filename(name)
    filename = f"{name}.{fmt}"
    filepath = folder_path / filename
    
    fig.savefig(filepath, format=fmt, dpi=dpi, bbox_inches="tight")
    return filepath

# ==============================================================
# 🟦 Mostrar figuras 
# ==============================================================
def mostrar_fig(fig, ancho=700, save=False, name=None, folder="assets/plots"):
    """
    Renderiza una figura de Matplotlib en Streamlit y libera recursos.

    Opcionalmente, permite guardar la visualización en disco para
    reutilización posterior.

    Parámetros:
    - fig (matplotlib.figure.Figure): Figura a mostrar.
    - ancho (int): Ancho de la imagen renderizada en píxeles.
    - save (bool): Indica si la figura debe guardarse en disco.
    - name (str, opcional): Nombre base del archivo si se guarda.
    - folder (str): Directorio de destino para el guardado.
    """
    
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=120, bbox_inches='tight')
    buf.seek(0)
    st.image(buf, width=ancho)

    if save:
        try:
            st.caption("💾 Vizualizacion guardada")
        except Exception as e:
            st.warning(f"No se pudo guardar el gráfico: {e}")

    plt.close(fig)
