import streamlit as st
import os
from pathlib import Path
from src.utils.eda_sections import mostrar_seccion_md, mostrar_graficos

def mostrar_vista_con_imagen(contenido_md, inicio_str, fin_str, imagen, caption):
    """
    Muestra una sección de la documentación del dashboard asociada a una vista específica,
    combinando una imagen representativa del dashboard con su descripción textual.

    La función extrae dinámicamente un fragmento del contenido Markdown en base a strings
    delimitadores, y lo renderiza junto a la imagen correspondiente, manteniendo alineadas
    la explicación conceptual y la representación visual de cada vista replicada.

    Args:
        contenido_md (str): Contenido completo del archivo Markdown de documentación.
        inicio_str (str): Cadena que indica el inicio de la sección a mostrar dentro del Markdown.
        fin_str (str): Cadena que indica el final de la sección a mostrar dentro del Markdown.
        imagen (str): Ruta al archivo de imagen asociado a la vista del dashboard.
        caption (str): Texto descriptivo que se muestra como leyenda de la imagen.

    Returns:
        None
    """
    st.image(imagen, caption=caption, width="content")
    st.markdown(
        contenido_md[
            contenido_md.find(inicio_str) + len(inicio_str):
            contenido_md.find(fin_str)
        ],
        unsafe_allow_html=True
    )
    
def mostrar_documentacion():
    """
    Página de Streamlit que presenta la documentación integral del proyecto
    de la tienda Aurelion directamente dentro del dashboard.

    Objetivo:
    Centralizar y visualizar la documentación funcional, metodológica y técnica
    del proyecto, permitiendo comprender el contexto del negocio, los datos,
    el análisis exploratorio y el modelado de Machine Learning sin salir
    de la aplicación.

    Funcionalidad principal:
    - Carga y renderiza el archivo Markdown de documentación del proyecto.
    - Estructura el contenido en secciones navegables mediante expanders.
    - Integra texto explicativo con gráficos, diagramas e interpretaciones EDA.
    - Presenta el flujo completo del proyecto desde el problema hasta el modelo.

    Secciones incluidas:
    1. Contexto y objetivo del proyecto:
       - Tema.
       - Problema de negocio.
       - Solución propuesta.
    2. Datasets de referencia:
       - Fuente de los datos.
       - Descripción, estructura y variables.
    3. Metodología e implementación:
       - Información general de la aplicación.
       - Pasos de la metodología aplicada.
       - Pseudocódigo del proceso.
    4. Diagrama del flujo:
       - Visualización del flujo general del sistema.
    5. Interpretaciones EDA:
       - Distribución de variables numéricas.
       - Matriz de correlación.
       - Evolución de ventas.
       - Relación entre variables.
       - Análisis de outliers.
    6. Modelado de Machine Learning:
       - Preprocesamiento para ML.
       - AutoML con PyCaret.
       - Entrenamiento manual con Random Forest.
       - Métricas, curvas ROC, matriz de confusión,
         importancia de variables y curvas de aprendizaje.

    Recursos utilizados:
    - Archivo Markdown: `docs/documentacion_tienda_aurelion.md`.
    - Imágenes y gráficos almacenados en la carpeta `assets/`.

    Comportamiento:
    - Si el archivo de documentación existe, se muestra su contenido
      de forma estructurada e interactiva.
    - Si el archivo no se encuentra, se informa al usuario mediante
      un mensaje de advertencia.

    Uso:
    Esta función se integra como la página de documentación del dashboard,
    funcionando como soporte explicativo del proyecto para evaluadores,
    usuarios finales o revisiones técnicas.
    """
    
    st.markdown(
        "<h3 style='color:#f1c40f;'>Documentación del proyecto</h3>",
        unsafe_allow_html=True
    )

    # Ruta al proyecto raíz y al archivo de documentación
    ruta_md = Path(__file__).resolve().parents[2] / "docs" / "documentacion_tienda_aurelion.md"
    ruta_flujo = Path(__file__).resolve().parents[2] / "assets" / "flujograma_aurelion.jpg"

    if ruta_md.exists():
        contenido_md = ruta_md.read_text(encoding="utf-8")

        # 🟡 --- Contexto y objetivo ---
        st.markdown(
            "<h4 style='color:#f1c40f;'>Contexto y objetivo</h4>",
            unsafe_allow_html=True
        )
                 
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
        st.markdown(
            "<h4 style='color:#f1c40f;'>Datasets de referencia</h4>",
            unsafe_allow_html=True
        )
            
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
        st.markdown(
            "<h4 style='color:#f1c40f;'>Metodología e implementación</h4>",
            unsafe_allow_html=True
        )
            
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
        st.markdown(
            "<h4 style='color:#f1c40f;'>Pseudocódigo</h4>",
            unsafe_allow_html=True
        )
        
        with st.expander("🔸 Ver Pseudocódigo"):
            inicio = contenido_md.find("### Pseudocódigo") + len("### Pseudocódigo")
            fin = contenido_md.find("### Diagrama del flujo")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # 🟡 --- Diagrama del flujo ---
        st.markdown(
            "<h4 style='color:#f1c40f;'>Diagrama del flujo</h4>",
            unsafe_allow_html=True
        )

        with st.expander("🔸 Ver Diagrama"):
            mostrar_graficos([
                "assets/flujograma_aurelion.png",
            ], columnas=1)

                
        # 🟡 --- Interpretaciones EDA – Visualizaciones ---
        st.markdown(
            "<h4 style='color:#f1c40f;'>Interpretaciones EDA – Visualizaciones</h4>",
            unsafe_allow_html=True
        )

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
        st.markdown(
            "<h4 style='color:#f1c40f;'>Modelado de Machine Learning</h4>",
            unsafe_allow_html=True
        )

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

              
        # 🟡 --- Dashboard Ejecutivo ---
        st.markdown(
            "<h4 style='color:#f1c40f;'>Dashboard Ejecutivo</h4>",
            unsafe_allow_html=True
        )

        inicio = contenido_md.find("### Dashboard Ejecutivo") + len("### Dashboard Ejecutivo")
        dashboard_md = contenido_md[inicio:]

        # ◽ Dashboard 
        with st.expander("🔸 Dashboard"):
            st.markdown(
                dashboard_md[
                    dashboard_md.find("#### 🔸 Dashboard")+ len("#### 🔸 Dashboard"):
                    dashboard_md.find("#### 🔸 Réplicas de Vistas")
                ],
                unsafe_allow_html=True
            )

        # ◽ Réplicas de Vistas
        with st.expander("🔸 Réplicas de Vistas"):

            # 1️⃣ Vista Principal
            st.markdown("##### 1️⃣ Vista Principal del Dashboard en Power BI")
            mostrar_vista_con_imagen(
                contenido_md,
                inicio_str="1️⃣ **Vista Principal del Dashboard en Power BI**",
                fin_str="2️⃣ **Análisis de Ventas**",
                imagen="assets/Dasboard-vista-principal.png",
                caption="Vista principal del Dashboard en Power BI"
            )

            # 2️⃣ Análisis de Ventas
            st.markdown("##### 2️⃣ Análisis de Ventas")
            mostrar_vista_con_imagen(
                contenido_md,
                inicio_str="2️⃣ **Análisis de Ventas**",
                fin_str="3️⃣ **Análisis de Clientes**",
                imagen="assets/Dasboard-analisis-de-ventas.png",
                caption="Vista de Análisis de Ventas"
            )

            # 3️⃣ Análisis de Clientes
            st.markdown("##### 3️⃣ Análisis de Clientes")
            mostrar_vista_con_imagen(
                contenido_md,
                inicio_str="3️⃣ **Análisis de Clientes**",
                fin_str="4️⃣ **Análisis de Productos**",
                imagen="assets/Dashboard-analisis-de-clientes.png",
                caption="Vista de Análisis de Clientes"
            )

            # 4️⃣ Análisis de Productos
            st.markdown("##### 4️⃣ Análisis de Productos")
            mostrar_vista_con_imagen(
                contenido_md,
                inicio_str="4️⃣ **Análisis de Productos**",
                fin_str="#### 🔸 Conclusiones",
                imagen="assets/Dashboard-analisis-de-productos.png",
                caption="Vista de Análisis de Productos"
            )

        # ◽ Conclusiones
        with st.expander("🔸 Conclusiones"):
            st.markdown(
                dashboard_md[
                    dashboard_md.find("#### 🔸 Conclusiones")+len ("#### 🔸 Conclusiones"):
                ],
                unsafe_allow_html=True
            )
                            
                                 
    else:
        st.warning("El archivo de documentación no se encontró.")





