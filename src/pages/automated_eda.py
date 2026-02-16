# # src/pages/automated_eda.py

# """
# Archivo deshabilitado temporalmente.
# Se eliminó ydata_profiling por compatibilidad.
# """

# import streamlit as st
# from ydata_profiling import ProfileReport
# from src.data_loader import load_and_merge_datasets

# def show_automated_eda():
#     """
#     Interfaz de Streamlit para realizar un Análisis Exploratorio de Datos (EDA)
#     automatizado utilizando la librería ydata-profiling.

#     Flujo de la función:
#     1. Carga y unifica los datasets necesarios mediante la función
#        `load_and_merge_datasets()`.
#     2. Genera un reporte exploratorio automático que incluye estadísticas
#        descriptivas, análisis de valores faltantes, correlaciones y
#        distribución de variables.
#     3. Renderiza el reporte completo en formato HTML dentro de la aplicación
#        Streamlit para su visualización interactiva.

#     Requisitos:
#     - La función `load_and_merge_datasets()` debe estar correctamente definida
#       y retornar un DataFrame válido.
#     - La librería ydata-profiling debe estar instalada y ser compatible con la
#       versión de Python utilizada.
#     - Streamlit debe permitir la renderización de componentes HTML.

#     Comportamiento ante errores:
#     - Si el dataset no puede cargarse o unificarse, se muestra un mensaje
#       de advertencia indicando el problema al usuario.

#     Uso:
#     Esta función se integra como una página del dashboard que permite obtener
#     rápidamente una visión general de la calidad y estructura de los datos,
#     sirviendo como punto de partida para análisis exploratorios manuales
#     o etapas posteriores de modelado.
#     """
           
#     st.markdown(
#         "<h3 style='color:#f1c40f;'>EDA Automatizado con librería <span style='color:#5dade2;'>ydata</span></h3>",
#         unsafe_allow_html=True
#     )
    
#     df = load_and_merge_datasets()
    
#     if df is not None:
#         # Crear el perfil con ydata-profiling
#         profile = ProfileReport(df, title="EDA - Dataset Unificado", explorative=True)
#         # Mostrarlo en Streamlit
#         st.components.v1.html(profile.to_html(), height=1000, scrolling=True)

#     else:
#         st.warning("⚠️ No se pudo cargar el dataset unificado.")


