import streamlit as st
import os
from pathlib import Path
from src.utils.eda_sections import mostrar_seccion_md, mostrar_graficos


def mostrar_documentacion():
    st.subheader("📘 Documentación del proyecto")

    # Ruta al proyecto raíz y al archivo de documentación
    ruta_md = Path(__file__).resolve().parents[2] / "docs" / "documentacion_tienda_aurelion.md"
    ruta_flujo = Path(__file__).resolve().parents[2] / "assets" / "flujograma_aurelion.jpg"

    if ruta_md.exists():
        contenido_md = ruta_md.read_text(encoding="utf-8")

        # 🟡 --- Contexto y objetivo ---
        st.markdown("### Contexto y objetivo")
                 
        # ◽ Tema
        with st.expander("🔸 Tema"):
            inicio = contenido_md.find("### Tema") + len("### Tema")
            fin = contenido_md.find("### Problema")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)
            
        # ◽ Problema
        with st.expander("🔸 Problema"):
            inicio = contenido_md.find("### Problema") + len("### Problema")
            fin = contenido_md.find("### Solución")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)
            
        # ◽ Solución propuesta
        with st.expander("🔸 Solución propuesta"):
            inicio = contenido_md.find("### Solución") + len("### Solución")
            fin = contenido_md.find("### Fuente")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)             
            
        # 🟡 --- Datasets de referencia ---
        st.markdown("### Datasets de referencia")
            
        # ◽ Tema
        with st.expander("🔸 Fuente"):
            inicio = contenido_md.find("### Fuente") + len("### Fuente")
            fin = contenido_md.find("### Datasets: definición, columnas y tipos")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)
            
        # ◽ Problema
        with st.expander("🔸 Descripción del dataset"):
            inicio = contenido_md.find("### Datasets: definición, columnas y tipos")
            fin = contenido_md.find("### Estructura")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)
            
        # ◽ Estructura del dataset
        with st.expander("🔸 Estructura del dataset"):
            inicio = contenido_md.find("### Estructura") + len("### Estructura")
            fin = contenido_md.find("### Información")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)
                        

        # 🟡 --- Metodología ---
        st.markdown("### Metodología e implementación")
            
        # ◽ Información
        with st.expander("🔸 Información de la aplicación"):
            inicio = contenido_md.find("### Información") + len("### Información")
            fin = contenido_md.find("### Pasos")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)
            
        # ◽ Pasos 
        with st.expander("🔸 Pasos de la metodología"):
            inicio = contenido_md.find("### Pasos") + len("### Pasos")
            fin = contenido_md.find("### Pseudocódigo")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # 🟡 --- Pseudocódigo ---
        st.markdown("### Pseudocódigo")
        with st.expander("🔸 Ver Pseudocódigo"):
            inicio = contenido_md.find("### Pseudocódigo") + len("### Pseudocódigo")
            fin = contenido_md.find("### Diagrama del flujo")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # 🟡 --- Diagrama del flujo ---
        st.markdown("### Diagrama del flujo")

        with st.expander("🔸 Ver Diagrama"):
            mostrar_graficos([
                "assets/flujograma_aurelion.png",
            ], columnas=1)

                
        # 🟡 --- Interpretaciones EDA – Visualizaciones ---
        st.markdown("### Interpretaciones EDA – Visualizaciones")

        # ◽ Distribución de variables
        with st.expander("🔸 Gráfica: Distribuciones de Variables numéricas"):
            mostrar_graficos([
                "assets/plots/Distribucion_de_cantidad.png",
                "assets/plots/Distribucion_de_precio_unitario.png",
                "assets/plots/Distribucion_de_total_venta.png",
            ], columnas=3)           
            mostrar_seccion_md(
                contenido_md,
                inicio_str="# Interpretaciones EDA – Visualizaciones",
                fin_str="#### 🔸 Gráfica: correlacion"
            )

        # ◽ Correlación
        with st.expander("🔸 Gráfica: Matriz de Correlación"):
            mostrar_graficos([
                "assets/plots/Matriz_de_Correlacion.png",
            ], columnas=1)
            mostrar_seccion_md(
                contenido_md,
                inicio_str="#### 🔸 Gráfica: correlacion",
                fin_str="#### 🔸 Gráfica: ventas_total_por_mes"
            )

        # ◽ Ventas por mes
        with st.expander("🔸 Gráfica: Ventas Totales por mes"):
            mostrar_graficos([
                "assets/plots/Ventas_totales_por_mes.png",
            ], columnas=1)
            mostrar_seccion_md(
                contenido_md,
                inicio_str="#### 🔸 Gráfica: ventas_total_por_mes",
                fin_str="#### 🔸 Gráfica: relacion_cantidad"
            )

        # ◽ Relación cantidad
        with st.expander("🔸 Gráfica: Relación Cantidad - Total Ventas"):
            mostrar_graficos([
                "assets/plots/Relacion_Cantidad_-_Total_Venta.png",
            ], columnas=1)
            mostrar_seccion_md(
                contenido_md,
                inicio_str="#### 🔸 Gráfica: relacion_cantidad",
                fin_str="#### 🔸 Gráfica: outliers"
            )

        # ◽ Outliers
        with st.expander("🔸 Gráfica: Outliers y Distribución"):
            mostrar_graficos([
                "assets/plots/outliers_cantidad.png",
                "assets/plots/outliers_precio_unitario.png",
                "assets/plots/outliers_total_venta.png",
            ], columnas=3)
            mostrar_seccion_md(
                contenido_md,
                inicio_str="#### 🔸 Gráfica: outliers"
            )                         
                    
                    
        # 🟡 --- Modelado de Machine Learning ---
        st.markdown("### Modelado de Machine Learning")

        # ◽ Preprocesamiento
        with st.expander("🔸 Preprocesamiento"):
            inicio = contenido_md.find("### Preprocesamiento para Machine Learning") 
            fin = contenido_md.find("### AutoML: Benchmarking con PyCaret")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # ◽ AutoML
        with st.expander("🔸 Auto Machine Learning"):
            inicio = contenido_md.find("### AutoML: Benchmarking con PyCaret") 
            fin = contenido_md.find("### Entrenamiento Manual: Random Forest")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)
           
        # ◽ Random Forest Manual           
        with st.expander("🔸 Entrenamiento Manual"):      
                
            inicio = contenido_md.find("### Entrenamiento Manual: Random Forest") 

            # 🔥 si no encuentra otro título, usa el final del archivo
            fin = contenido_md.find("\n### ", inicio)
            if fin == -1:
                fin = len(contenido_md)
               
            texto = contenido_md[inicio:fin]

            # ---- Dividir por marcadores ----
            partes = texto.split("🔸 **Curva ROC Multiclase (One-vs-Rest)**")
            st.markdown(partes[0], unsafe_allow_html=True)

            # ---- 🔸 Gráfico ROC ----
            st.markdown(
                '<p style="font-size:18px; font-weight:600; margin-bottom:0;">Curva ROC Multiclase</p>',
                unsafe_allow_html=True
            )
            mostrar_graficos([
                "assets/plots/Curvas_ROC__Multiclase_-_One_vs_Rest.png",
            ], columnas=1)

            # ---- Resto del texto hasta la matriz ----
            partes = partes[1].split("🔸 **Matriz de Confusión**")
            st.markdown(partes[0], unsafe_allow_html=True)

            # ---- 🔸 Matriz de confusión ----
            st.markdown(
                '<p style="font-size:18px; font-weight:600; margin-bottom:0;">Matriz de Confusión</p>',
                unsafe_allow_html=True
            )
            mostrar_graficos([
                "assets/plots/Matriz_de_Confusion.png",
            ], columnas=1)

            # ---- Resto hasta importancia variables ----
            partes = partes[1].split("🔸 **Importancia de variables**")
            st.markdown(partes[0], unsafe_allow_html=True)

            # ---- 🔸 Importancia de variables ----
            st.markdown(
                '<p style="font-size:18px; font-weight:600; margin-bottom:0;">Importancia de Variables</p>',
                unsafe_allow_html=True
            )
            mostrar_graficos([
                "assets/plots/Importancia_de_Variables.png",
            ], columnas=1)

            # ---- Resto hasta classification report ----
            partes = partes[1].split("<h5><b>Classification Report por clase</b></h5>")
            st.markdown(partes[0], unsafe_allow_html=True)

            # ---- 🔸 Classification Report ----
            st.markdown(
                '<p style="font-size:18px; font-weight:600; margin-bottom:0;">Reporte de Métricas por Clase</p>',
                unsafe_allow_html=True
            )
            mostrar_graficos([
                "assets/plots/Classification_Report_-_Metricas_por_Clase.png",
            ], columnas=1) 

            # ---- Resto hasta learning curve ----
            partes = partes[1].split("<h5><b>Curva de aprendizaje</b></h5>")
            st.markdown(partes[0], unsafe_allow_html=True)

            # ---- 🔸 Learning curve ----
            st.markdown(
                '<p style="font-size:18px; font-weight:600; margin-bottom:0;">Curva de Aprendizaje</p>',
                unsafe_allow_html=True
            )
            mostrar_graficos([
                "assets/plots/Learning_Curve_-_Accuracy.png",
            ], columnas=1) 

            # ---- Última parte del texto ----
            st.markdown(partes[1], unsafe_allow_html=True)

                    
    else:
        st.warning("El archivo de documentación no se encontró.")
