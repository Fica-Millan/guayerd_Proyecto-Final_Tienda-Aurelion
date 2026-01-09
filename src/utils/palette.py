# src/utils/palette.py

"""
palette.py
----------

Definición de la paleta de colores corporativa de la aplicación.

Este módulo centraliza los colores utilizados en visualizaciones
(gráficos de barras, líneas y tortas) para garantizar consistencia
visual y facilitar cambios globales de estilo.
"""

# --- Paleta de colores global para la app ---
PALETA = {
    "principal": "#05E8CC",     
    "secundario": "#05BAE8",   
    "acento1": "#91BCEB",      
    "acento2": "#05E87F",      
    "claro": "#2244EB",        
    "suave": "#52CAE8"         
}

COLORES_BARRAS = [PALETA["acento2"], PALETA["principal"], PALETA["claro"], PALETA["secundario"], PALETA["acento1"], PALETA["suave"]]
COLORES_LINEAS = [PALETA["principal"], PALETA["secundario"]]
COLORES_PIE = [PALETA["principal"], PALETA["claro"], PALETA["suave"], PALETA["acento1"]]