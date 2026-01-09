#utils/eda_sections.py

import os
import streamlit as st

def mostrar_seccion_md(contenido_md: str, inicio_str: str, fin_str: str = None):
    """
    Extrae y renderiza en Streamlit un fragmento de texto Markdown delimitado
    por cadenas de inicio y fin.

    Parámetros:
    - contenido_md (str): Contenido completo del archivo Markdown.
    - inicio_str (str): Texto que marca el inicio de la sección a mostrar.
    - fin_str (str, opcional): Texto que marca el fin de la sección.
      Si no se especifica, se muestra hasta el final del contenido.
    """
    
    inicio = contenido_md.find(inicio_str)
    if inicio == -1:
        st.warning(f"No se encontró el texto de inicio: {inicio_str}")
        return

    inicio += len(inicio_str)

    if fin_str:
        fin = contenido_md.find(fin_str)
        if fin == -1:
            fin = len(contenido_md)
    else:
        fin = len(contenido_md)

    st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

def mostrar_graficos(rutas: list, columnas: int = 1):
    """
    Renderiza en Streamlit una colección de imágenes de gráficos,
    distribuyéndolas en una o más columnas.

    Parámetros:
    - rutas (list): Lista de rutas a archivos de imagen.
    - columnas (int): Cantidad de columnas para la disposición visual.
      Si es 1, centra cada gráfico; si es mayor, distribuye en grilla.

    Notas:
    - Si una imagen no existe, se muestra una advertencia indicando
      que debe generarse previamente desde la sección de EDA.
    """
    
    if columnas == 1:
        for ruta in rutas:
            if os.path.exists(ruta):
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.image(ruta, use_container_width=True)
            else:
                st.warning(f"No se encontró la imagen: {ruta}\n"
                           "- Para generarla, primero debes ejecutar la página 👉🏻 **EDA Diagnóstico**."
                )
    else:
        cols = st.columns(columnas)
        for col, ruta in zip(cols, rutas):
            if os.path.exists(ruta):
                with col:
                    st.image(ruta, use_container_width=True)
            else:
                st.warning(f"No se encontró la imagen: {ruta}\n"
                           "- Para generarla, primero debes ejecutar la página 👉🏻 **EDA Diagnóstico**."
                )