# src/utils/validation.py

from src.utils.rules import RULES
import re
import pandas as pd
import streamlit as st  


def verificar_fallbacks(df):
    """
    Identifica productos clasificados como 'Alimentos secos' que quedaron
    asignados por fallback y no coinciden con ningún patrón regex válido
    definido para esa categoría.

    La función valida los nombres de producto contra las keywords reales
    configuradas en RULES["Alimentos secos"] para detectar clasificaciones
    potencialmente incorrectas.

    Parámetros
    ----------
    df : pd.DataFrame
        Dataset con al menos las columnas 'nombre_producto' y
        'categoria_corregida'.

    Retorna
    -------
    alimentos_reales : pd.DataFrame
        Productos clasificados como 'Alimentos secos'.
    fallas : pd.DataFrame
        Subconjunto de productos que no matchean ninguna keyword válida
        (verdaderos casos de fallback).
    """
    
    alimentos_keywords = RULES["Alimentos secos"]
    
    alimentos_reales = df[df["categoria_corregida"] == "Alimentos secos"]
    
    def tiene_keyword_valida(nombre):
        """Verifica si el nombre coincide con algún patrón regex"""
        texto = nombre.lower()
        for patron in alimentos_keywords:
            if re.search(patron, texto):
                return True
        return False
    
    # Productos que NO tienen ninguna keyword válida (verdadero fallback)
    fallas = alimentos_reales[
        ~alimentos_reales["nombre_producto"].apply(tiene_keyword_valida)
    ]
    
    return alimentos_reales, fallas


def mostrar_validaciones_fallback(alimentos_reales: pd.DataFrame, fallas: pd.DataFrame):
    """
    Visualiza en Streamlit el resultado de la validación de fallbacks para
    la categoría 'Alimentos secos', mostrando métricas y listados de casos
    inconsistentes.

    Presenta indicadores resumen y mensajes contextuales según el nivel
    de fallas detectadas, permitiendo evaluar rápidamente la calidad de
    las reglas de clasificación.
    """
    
    st.write("### 🔸 Validación de fallbacks")

    # Métricas
    col1, col2 = st.columns(2)
    col1.metric("Alimentos secos detectados", len(alimentos_reales))
    col2.metric("Productos en fallback", len(fallas))

    # Mensajes
    if len(fallas) == 0:
        st.success("✅ Todos los productos en 'Alimentos secos' tienen keywords válidas")
        return

    if len(alimentos_reales) == 0:
        st.info("ℹ️ No hay productos clasificados como 'Alimentos secos'.")
        return

    if len(fallas) == len(alimentos_reales):
        st.error("❌ TODOS los productos en 'Alimentos secos' están en fallback (sin keywords reales)")
        st.dataframe(fallas[["nombre_producto", "categoria_corregida"]], use_container_width=True)
    else:
        reales_validos = len(alimentos_reales) - len(fallas)
        st.warning(f"⚠️ {len(fallas)} de {len(alimentos_reales)} productos en 'Alimentos secos' están en fallback")
        st.info(f"ℹ️ {reales_validos} productos en 'Alimentos secos' SÍ tienen keywords válidas")
        st.dataframe(fallas[["nombre_producto", "categoria_corregida"]], use_container_width=True)
