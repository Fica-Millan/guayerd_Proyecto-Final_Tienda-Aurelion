# src/pages/ml_preprocessing.py

import streamlit as st
import pandas as pd
import plotly.express as px


def show_ml_preprocessing():
    """
    Ejecuta y visualiza en Streamlit el pipeline completo de preprocesamiento
    de datos para el entrenamiento de modelos de Machine Learning orientados
    a la predicción del nivel de demanda de productos.

    Objetivo:
    Transformar el dataset transaccional de la tienda Aurelion en un dataset
    tabular, consistente y apto para modelos de clasificación supervisada,
    incorporando validaciones, feature engineering y control de calidad.

    Flujo del preprocesamiento:
    1. Carga del dataset unificado previamente depurado.
    2. Análisis exploratorio inicial y validaciones de calidad:
       - Tipos de datos.
       - Valores nulos.
       - Distribuciones básicas.
    3. Agrupación por producto:
       - Cálculo de métricas agregadas (ventas, unidades, transacciones).
       - Verificación de consistencia entre totales originales y agregados.
    4. Feature engineering:
       - Variables derivadas por transacción.
    5. Creación de la variable objetivo:
       - Segmentación de productos en niveles de demanda (baja, media, alta)
         utilizando cuantiles.
       - Diagnóstico de distribución y rangos por categoría.
    6. Visualizaciones interactivas:
       - Distribución de la variable objetivo.
       - Ranking de productos por volumen de ventas.
    7. Transformaciones para Machine Learning:
       - One-Hot Encoding de variables categóricas.
       - Codificación numérica de la variable objetivo.
       - Eliminación de columnas de alta cardinalidad.
       - Validaciones post-transformación.
    8. Exportación del dataset final:
       - Guardado automático en formato CSV.
       - Descarga manual desde la interfaz.

    Resultados:
    - Genera el archivo `data/dataset_ml_productos.csv` listo para ser utilizado
      en procesos de AutoML (PyCaret) y entrenamiento manual de modelos.
    - Proporciona trazabilidad completa del proceso mediante visualizaciones
      y validaciones en la interfaz.

    Retorno:
    Esta función no retorna valores; presenta los resultados y métricas
    directamente en la interfaz de Streamlit y persiste el dataset procesado
    en disco.

    Uso:
    Se integra como la etapa previa obligatoria al modelado de Machine Learning
    dentro del dashboard analítico del proyecto.
    """
    st.markdown(
        "<h3 style='color:#f1c40f;'>Preprocesamiento para Machine Learning</h3>",
        unsafe_allow_html=True
    )
    st.write("Esta sección prepara el dataset para entrenar modelos de clasificación de demanda.")

    st.markdown("---")  
    
    # ==============================================================
    # 1️⃣ Cargar dataset unificado
    # ==============================================================
    st.markdown("### 1. Carga del dataset")

    try:
        df = pd.read_csv("data/df_tienda_aurelion_modificado.csv")
        st.success("Dataset cargado correctamente.")

        with st.expander("🔸 Ver primeras filas"):
            st.dataframe(df.head())

    except Exception as e:
        st.error("⚠️ No se pudo cargar el archivo `df_tienda_aurelion_modificado.csv`.")
        st.write(e)
        st.stop()

    st.markdown("---")

    # ==============================================================
    # 2️⃣ Información general
    # ==============================================================
    st.markdown("### 2. Información general del dataset")

    col1, col2, col3 = st.columns(3)
    col1.metric("Filas", df.shape[0])
    col2.metric("Columnas", df.shape[1])
    col3.metric("Valores nulos", df.isna().sum().sum())
    
    # 🔍 VALIDACIONES ADICIONALES (mostrar en Streamlit, no solo print)
    with st.expander("🔸 Validaciones de calidad de datos"):
        st.write("**Distribución de categorías:**")
        st.write(df['categoria_corregida'].value_counts())
        
        st.write("**Estadísticas de precios:**")
        st.write(df['precio_unitario'].describe())
        
        st.write("**Estadísticas de cantidades:**")
        st.write(df['cantidad'].describe())
        
        # Verificar nulos por columna
        st.write("**Valores nulos por columna:**")
        nulos_por_columna = df.isnull().sum()
        st.write(nulos_por_columna[nulos_por_columna > 0])
           
    with st.expander("🔸 Detalle por columna"):
        info = pd.DataFrame({
            "Tipo": df.dtypes.astype(str),
            "Nulos": df.isna().sum(),
            "Valores únicos": df.nunique(),
        })
        st.dataframe(info)

    st.markdown("---")
    
    
    # ==============================================================
    # 3️⃣ Agrupación por producto
    # ==============================================================
    st.markdown("### 3. Agrupación por producto")
    
    st.write("""
    Agrupamos el dataset para obtener métricas agregadas por producto.
    Esto reduce ruido, mejora la señal y vuelve el problema de clasificación más claro.
    """)

    df_prod = (
        df.groupby(["id_producto", "nombre_producto", "categoria_corregida"])
        .agg(
            total_unidades=("cantidad", "sum"),
            total_ventas=("total_venta", "sum"),
            cant_transacciones=("id_venta", "count"),
            precio_promedio=("precio_unitario", "mean"),
        )
        .reset_index()
    )

    # 🚀 FEATURE ENGINEERING - HACERLO AQUÍ ANTES DE LAS TRANSFORMACIONES
    df_prod['ventas_por_transaccion'] = df_prod['total_ventas'] / df_prod['cant_transacciones']
    df_prod['unidades_por_transaccion'] = df_prod['total_unidades'] / df_prod['cant_transacciones']

    st.markdown("#### 🔸 Vista previa del dataset agrupado")
    st.dataframe(df_prod.head(20))

    # Chequeo de consistencia
    total_original = df["cantidad"].sum()
    total_agrupado = df_prod["total_unidades"].sum()

    with st.expander("🔸 Chequeo de consistencia de agrupación"):
        c1, c2, c3 = st.columns(3)
        c1.metric("Suma original", total_original)
        c2.metric("Suma agrupada", total_agrupado)
        c3.metric("Coinciden", "✔️ Sí" if total_original == total_agrupado else "❌ No")

        if total_original == total_agrupado:
            st.success("✔️ La agrupación mantiene los totales correctamente.")
        else:
            st.error("❌ Las sumas NO coinciden. Revisar el proceso.")

    st.markdown("---")

    # ==============================================================
    # 4️⃣ Variable objetivo
    # ==============================================================
    st.markdown("### 4. Crear variable objetivo (nivel de demanda)")

    q1 = df_prod["total_unidades"].quantile(0.33)
    q2 = df_prod["total_unidades"].quantile(0.66)

    st.info(f"""
    Segmentación actual (percentiles):
    - Alta: > {q2:.2f} unidades
    - Media: {q1:.2f} < x ≤ {q2:.2f} unidades  
    - Baja: ≤ {q1:.2f} unidades

    """)

    def clasificar_demanda(x):
        if x <= q1:
            return "baja"
        elif x <= q2:
            return "media"
        else:
            return "alta"

    df_prod["nivel_demanda"] = df_prod["total_unidades"].apply(clasificar_demanda)

    # Diagnóstico rápido
    orden = ["alta", "media", "baja"]

    conteos = (
        df_prod["nivel_demanda"]
        .value_counts()
        .reindex(orden)
    )

    proporciones = (conteos / conteos.sum() * 100).round(2)

    col1, col2 = st.columns(2)
    with col1:
        st.write("Cantidad por categoría:")
        st.write(conteos)
    with col2:
        st.write("Porcentaje:")
        st.write(proporciones.astype(str) + "%")

    with st.expander("🔸 Diagnóstico detallado"):
        orden = ["alta", "media", "baja"]
        rangos = df_prod.groupby("nivel_demanda")["total_unidades"].agg(["min", "max", "count"]).reindex(orden)
        st.write("Rangos por categoría:")
        st.dataframe(rangos)

    st.markdown("---")
    
    # ==============================================================
    # 5️⃣ Visualización
    # ==============================================================
    st.markdown("### 5. Visualización")

    colores = {
        "alta": "#05E8CC",
        "media": "#52CAE8",
        "baja": "#91BCEB",
    }

    fig = px.histogram(
        df_prod, x="nivel_demanda", color="nivel_demanda",
        title="Distribución por nivel de demanda",
        color_discrete_map=colores,
        category_orders={"nivel_demanda": ["alta", "media", "baja"]}
    )
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(
        df_prod.sort_values("total_unidades", ascending=False).head(20),
        x="nombre_producto", y="total_unidades",
        color="nivel_demanda",
        title="Top 20 - Unidades vendidas por producto",
        color_discrete_map=colores
    )
    fig2.update_layout(xaxis_tickangle=-45) 
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ==============================================================
    # 6️⃣ Transformaciones (OHE, mapping, eliminación)
    # ==============================================================
    st.markdown("### 6. Transformaciones del dataset")

    columnas_iniciales = set(df_prod.columns)
    columnas_eliminadas = {}
    columnas_transformadas = {}

    # One-Hot Encoding
    df_prod = pd.get_dummies(
        df_prod,
        columns=["categoria_corregida"],
        prefix="categoria",
        drop_first=False,
    )
    columnas_transformadas["categoria_corregida"] = "One-Hot Encoding aplicado"

    # Mapping del target
    mapa = {"baja": 0, "media": 1, "alta": 2}
    df_prod["nivel_demanda"] = df_prod["nivel_demanda"].map(mapa)

    st.info("""
    La variable **nivel_demanda** se convirtió en:
    - alta → 2  
    - media → 1  
    - baja → 0  
    """)

    # Eliminación de columnas
    df_final = df_prod.copy()

    if "nombre_producto" in df_final:
        df_final = df_final.drop(columns=["nombre_producto"])
        columnas_eliminadas["nombre_producto"] = "Eliminada por alta cardinalidad"

    nuevas_columnas = list(set(df_final.columns) - columnas_iniciales)

    with st.expander("🔸 Detalle de transformaciones aplicadas"):
        st.subheader("Columnas nuevas")
        st.dataframe({"Nueva columna": nuevas_columnas})

        st.subheader("Columnas eliminadas")
        st.dataframe(pd.DataFrame.from_dict(columnas_eliminadas, orient="index", columns=["Motivo"]))

        st.subheader("Columnas transformadas")
        st.dataframe(pd.DataFrame.from_dict(columnas_transformadas, orient="index", columns=["Transformación"]))


    # 🔍 VALIDACIÓN FINAL DE CATEGORÍAS OHE
    with st.expander("🔸 Validación de categorías OHE"):
        categoria_cols = [col for col in df_final.columns if col.startswith('categoria_')]
        if categoria_cols:
            st.write("**Distribución de categorías (One-Hot Encoding):**")
            st.write(df_final[categoria_cols].sum())
        else:
            st.write("No se generaron columnas de categoría")
            
    st.markdown("---")
     
    # ==============================================================
    # 7️⃣ Exportación final
    # ==============================================================
    st.markdown("### 7 Exportar dataset final")

    st.write("Vista previa del dataset final:")
    st.dataframe(df_final.head())

    # OPCIÓN 1: Exportación automática
    df_final.to_csv("data/dataset_ml_productos.csv", index=False)
    st.success("Archivo exportado automáticamente: `data/dataset_ml_productos.csv`")

    # OPCIÓN 2: Botón de descarga (opcional)
    csv = df_final.to_csv(index=False)
    st.download_button(
        label="📥 Descargar dataset final como CSV",
        data=csv,
        file_name="dataset_ml_productos.csv",
        mime="text/csv"
    )

    st.markdown("---")
    st.success("✅ Preprocesamiento completado. Dataset listo para entrenar modelos de ML.")
