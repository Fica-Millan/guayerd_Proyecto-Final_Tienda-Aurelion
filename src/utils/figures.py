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
    folder_path = Path(folder)
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path

def clean_filename(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9_-]", "_", text)
    return text.strip("_")

# ==============================================================
# 🟦 Guardar figuras
# ==============================================================
def save_fig_to_disk(fig, name=None, folder="assets/plots", dpi=120, fmt="png"):
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
