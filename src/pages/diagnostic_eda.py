# src/pages/eda_diagnostico.py

import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.utils.docs_loader import cargar_interpretacion
from src.data_loader import load_dataset, verificar_unificacion_streamlit
from src.utils.figures import mostrar_fig, save_fig_to_disk
from src.utils.classification import clasificar_producto
from src.utils.validation import verificar_fallbacks, mostrar_validaciones_fallback
from src.utils.palette import PALETA

INTERPRETACIONES_PATH = "docs/documentacion_tienda_aurelion.md"

def show_diagnostic_eda():      
    st.markdown(
        "<h3 style='color:#f1c40f;'>EDA Diagnóstico del negocio</h3>",
        unsafe_allow_html=True
    )

    # ==============================================================
    # 1️⃣ Carga del dataset
    # ==============================================================

    df = load_dataset("df_tienda_aurelion")

    if df is None or df.empty:
        st.error("❌ No se pudo cargar el dataset unificado.")
        return

    # ==============================================================
    # 2️⃣ Recategorización de productos
    # ==============================================================

    with st.expander("🟠 Recategorización de Productos", expanded=False):

        # Validación de columna requerida
        if "nombre_producto" not in df.columns:
            st.error("❌ No se encontró la columna 'nombre_producto' en el dataset")
            st.stop()

        # Aplicar recategorización una sola vez
        df = df.copy()
        df["categoria_corregida"] = df["nombre_producto"].apply(clasificar_producto)
        st.success("✅ Columna 'categoria_corregida' creada correctamente.")

        # Métricas globales (una sola vez)
        total_productos = len(df)
        categorias_unicas = df["categoria_corregida"].nunique()
        categoria_counts = df["categoria_corregida"].value_counts()

        # Resumen de categorías
        st.write("### 🔸 Resumen de categorías")
        c1, c2 = st.columns(2)
        c1.metric("Total de productos", total_productos)
        c2.metric("Categorías distintas", categorias_unicas)

        st.write("#### Distribución por categoría:")
        st.dataframe(
            categoria_counts.reset_index().rename(columns={'index': 'Categoría', 'categoria_corregida': 'Cantidad'}),
            use_container_width=True
        )

        # Validación de fallbacks (encapsulada)
        alimentos_reales, fallas = verificar_fallbacks(df)
        mostrar_validaciones_fallback(alimentos_reales, fallas)

        st.divider()

        # ============================================================
        # 🔎 FILTRO POR CATEGORÍA
        # ============================================================
        st.subheader("🔸 Explorar productos por categoría")

        categorias = sorted(df["categoria_corregida"].dropna().unique())
        if len(categorias) == 0:
            st.info("No hay categorías disponibles para filtrar.")
            st.stop()

        categoria_sel = st.selectbox(
            "Seleccioná una categoría para ver sus productos:",
            options=categorias,
            index=0
        )

        # Filtrar productos de la categoría seleccionada
        df_filtrado = df[df["categoria_corregida"] == categoria_sel]

        # Métricas rápidas del filtrado
        f1, f2 = st.columns(2)
        f1.metric("Productos en esta categoría", len(df_filtrado))
        porcentaje = (len(df_filtrado) / total_productos * 100) if total_productos else 0
        f2.metric("% del total", f"{porcentaje:.1f}%")

        # Tabla filtrada
        st.dataframe(
            df_filtrado[["nombre_producto", "categoria_corregida"]],
            use_container_width=True,
            height=400
        )

    # ==============================================================
    # 3️⃣ Verificación del dataset unificado
    # ==============================================================

    with st.expander("🟠 Verificación del Dataset Unificado", expanded=False):
        verificar_unificacion_streamlit(df)

    # ==============================================================
    # 4️⃣ Limpieza y preparación
    # ==============================================================

    with st.expander("🟠 Limpieza y Preparación de Datos", expanded=False):

        # Convertir fechas
        fecha_cols = ['fecha', 'fecha_alta']
        for col in fecha_cols:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
                st.write(f"◽ '{col}' convertida a datetime")

        # Quitar importe duplicado
        if 'importe' in df.columns and 'total_venta' in df.columns:
            if (df['importe'] == df['total_venta']).all():
                df.drop(columns=['importe'], inplace=True)
                st.write("◽ 'importe' eliminada (igual a total_venta)")
            else:
                st.info("◽ 'importe' se conserva (no coincide con total_venta)")

        # Renombrar fecha
        if 'fecha' in df.columns:
            df.rename(columns={'fecha': 'fecha_venta'}, inplace=True)
            st.write("◽ 'fecha' renombrada a 'fecha_venta'")

        st.write("### Tipos de datos")
        st.dataframe(df.dtypes)

        st.write("### Valores nulos")
        st.bar_chart(df.isnull().sum())

    # ==============================================================
    # 5️⃣ Estadísticas descriptivas
    # ==============================================================

    with st.expander("🟠 Estadísticas Descriptivas", expanded=False):

        numericas = ['cantidad', 'precio_unitario', 'total_venta']
        numericas = [c for c in numericas if c in df.columns]

        st.dataframe(df[numericas].describe())

    # ==============================================================
    # 6️⃣ Distribución de variables numéricas
    # ==============================================================

    with st.expander("🟠 Distribución de Variables Numéricas", expanded=False):

        cols = st.columns(3)
        for i, col in enumerate(numericas):
            fig, ax = plt.subplots(figsize=(5,4))
            sns.histplot(            
                df[col],
                kde=True,
                color=PALETA["claro"],
                ax=ax,
                edgecolor="white",   
                linewidth=1                 
            )

            for line in ax.lines:
                line.set_color(PALETA["secundario"])
                line.set_linewidth(2)

            ax.set_title(f"Distribución de {col}", fontsize=14, fontweight="bold", color=PALETA["secundario"])
            save_fig_to_disk(fig)

            cols[i % 3].pyplot(fig)
            
        # ✅ Interpretación conjunta
        tabla_interpretacion = cargar_interpretacion(
            INTERPRETACIONES_PATH,
            "distribucion_numericas"
        )

        st.markdown("### 📝 Interpretación Conjunta de Variables Numéricas")
        st.markdown(tabla_interpretacion, unsafe_allow_html=True)

    # ==============================================================
    # 7️⃣ Matriz de correlación
    # ==============================================================

    with st.expander("🟠 Matriz de Correlación", expanded=False):
        numeric_cols = df.select_dtypes(include='number').columns
        
        if len(numericas) > 1:
            fig, ax = plt.subplots(figsize=(max(4, len(numeric_cols)*0.5), max(4, len(numeric_cols)*0.5)))
            corr = df[numericas].corr()
            
            # Eliminar “index—streamlit-generated”
            corr.index.name = ""
            corr.columns.name = ""

            sns.heatmap(
                corr,
                annot=True,
                cmap=sns.diverging_palette(25, 220, s=70, l=40, as_cmap=True),
                center=0,
                square=True, 
                ax=ax
            )

            ax.set_title("Matriz de Correlación", fontsize=14, fontweight="bold", color=PALETA["secundario"])
            
            save_fig_to_disk(fig)
            mostrar_fig(fig, save=True, ancho=500)
            
            # Cargar e insertar interpretación desde documentación
            interpretacion = cargar_interpretacion(INTERPRETACIONES_PATH, "correlacion")
            st.markdown(f"#### 📝 Interpretación\n{interpretacion}")

    # ==============================================================
    # 8️⃣ Visualizaciones principales
    # ==============================================================

    with st.expander("🟠 Visualizaciones Principales", expanded=False):

        # --- Ventas por mes ---           
        # Verificar que existan las columnas
        if 'fecha_venta' in df.columns and 'total_venta' in df.columns:

            # Convertir fecha y agrupar por mes
            df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
            df['mes'] = df['fecha_venta'].dt.to_period('M')
            ventas_mes = df.groupby('mes')['total_venta'].sum().reset_index()

            plt.figure(figsize=(9,6))
            plt.plot(
                ventas_mes['mes'].astype(str),
                ventas_mes['total_venta'],
                marker='o',
                color=PALETA["principal"],
                linewidth=2
            )

            # Etiquetas de valor en cada punto
            for x, y in zip(ventas_mes['mes'].astype(str), ventas_mes['total_venta']):
                plt.text(x, y + 8000, f"{y:,.0f}", ha='center', fontsize=9, color='#333333')

            # Destacar máximo y mínimo
            max_mes = ventas_mes.loc[ventas_mes['total_venta'].idxmax()]
            min_mes = ventas_mes.loc[ventas_mes['total_venta'].idxmin()]
            
            fig, ax = plt.subplots(figsize=(9,6))
            ax.plot(
                ventas_mes['mes'].astype(str),
                ventas_mes['total_venta'],
                marker='o',
                color=PALETA["principal"],
                linewidth=2
            )

            # Etiquetas de valor en cada punto
            for x, y in zip(ventas_mes['mes'].astype(str), ventas_mes['total_venta']):
                ax.text(x, y + 8000, f"{y:,.0f}", ha='center', fontsize=9, color='#333333')

            # Destacar máximo y mínimo
            max_mes = ventas_mes.loc[ventas_mes['total_venta'].idxmax()]
            min_mes = ventas_mes.loc[ventas_mes['total_venta'].idxmin()]

            ax.scatter(str(max_mes['mes']), max_mes['total_venta'], color='green', s=80, label='Máximo')
            ax.scatter(str(min_mes['mes']), min_mes['total_venta'], color='red', s=80, label='Mínimo')

            ax.annotate(
                f"Máximo: {max_mes['total_venta']:,.0f}",
                xy=(str(max_mes['mes']), max_mes['total_venta']),
                xytext=(0, 20),
                textcoords='offset points',
                ha='center',
                color='green',
                fontsize=9
            )

            ax.annotate(
                f"Mínimo: {min_mes['total_venta']:,.0f}",
                xy=(str(min_mes['mes']), min_mes['total_venta']),
                xytext=(0, -25),
                textcoords='offset points',
                ha='center',
                color='red',
                fontsize=9
            )

            # Línea de promedio
            promedio = ventas_mes['total_venta'].mean()
            ax.axhline(promedio, color=PALETA["acento2"], linestyle='--', linewidth=1, label=f'Promedio: {promedio:,.0f}')

            ax.set_ylim(200000, 650000)
            ax.set_title("Ventas Totales por Mes", fontsize=14, fontweight="bold", color=PALETA["secundario"])
            ax.set_xlabel("Mes")
            ax.set_ylabel("Total Ventas")
            ax.grid(True, linestyle='--', alpha=0.5)
            ax.legend()
            plt.tight_layout()

            # ✅ Mostrar y guardar en Streamlit
            save_fig_to_disk(fig)
            mostrar_fig(fig, save=True, ancho=700) 
            
            # Cargar e insertar interpretación desde documentación
            interpretacion = cargar_interpretacion(INTERPRETACIONES_PATH, "ventas_total_por_mes")
            st.markdown(f"#### 📝 Interpretación\n{interpretacion}")
                

        # --- Dispersión cantidad vs total ---
        if 'cantidad' in df.columns and 'total_venta' in df.columns:

            fig, ax = plt.subplots(figsize=(8,5))
            sns.regplot(
                data=df,
                x='cantidad',
                y='total_venta',
                scatter_kws={'color': PALETA["principal"], 'alpha': 0.6},
                line_kws={'color': PALETA["acento1"]},
                ci=None,
                ax=ax
            )

            corr = df['cantidad'].corr(df['total_venta'])

            ax.set_title("Relación Cantidad - Total Venta", fontsize=14, fontweight="bold", color=PALETA["secundario"])
            ax.grid(True, linestyle='--', alpha=0.5)

            ax.text(
                x=df['cantidad'].min() + 0.05*(df['cantidad'].max()-df['cantidad'].min()),
                y=df['total_venta'].max()*0.95,
                s=f"Correlación: {corr:.2f}",
                fontsize=12,
                color=PALETA["acento1"]
            )

            save_fig_to_disk(fig)
            mostrar_fig(fig, save=True, ancho=700)
            
            # Cargar e insertar interpretación desde documentación
            interpretacion = cargar_interpretacion(INTERPRETACIONES_PATH, "relacion_cantidad")
            st.markdown(f"#### 📝 Interpretación\n{interpretacion}")
            

        # --- Top productos por categoría ---      
        with st.expander("Top Productos por Categoría", expanded=False):

            if "categoria_corregida" in df.columns:
                
                st.write("### Seleccioná una categoría")

                categorias = sorted(df["categoria_corregida"].unique())
                categoria_seleccionada = st.selectbox(
                    "Categoría:",
                    categorias
                )

                df_cat = df[df["categoria_corregida"] == categoria_seleccionada]
                top_prod = (
                    df_cat.groupby("nombre_producto")["cantidad"]
                    .sum()
                    .sort_values(ascending=False)
                    .head(5)
                )

                st.write(f"### Top 5 de {categoria_seleccionada}")
                st.dataframe(top_prod)

                fig, ax = plt.subplots(figsize=(5,3))
                ax.barh(top_prod.index, top_prod.values, color=PALETA["principal"])
                ax.invert_yaxis()
                ax.set_title(f"Top 5 Productos — {categoria_seleccionada}", fontsize=14, fontweight="bold", color=PALETA["secundario"])

                mostrar_fig(fig, save=True, ancho=700)

    # ==============================================================
    # 9️⃣ Outliers
    # ==============================================================

    with st.expander("🟠 Outliers y Distribución", expanded=False):

        cols = st.columns(3)                                                                                                                                                                          
        
        for i, col in enumerate(numericas):
            fig, ax = plt.subplots(figsize=(5,4))
            sns.boxplot(
                x=df[col],
                color=PALETA["acento1"],
                ax=ax,
                flierprops=dict(marker='o', color=PALETA["claro"], alpha=0.5)
            )
            sns.stripplot(
                x=df[col],
                color=PALETA["claro"],
                size=3,
                alpha=0.4,
                jitter=True,
                ax=ax
            )
            ax.set_title(f"Boxplot — {col}", fontsize=14, fontweight="bold", color=PALETA["secundario"])
            save_fig_to_disk(fig, name=f"outliers_{col}")
            cols[i % 3].pyplot(fig)
            
        # ----- INTERPRETACIÓN COMBINADA -----
        interpretacion = cargar_interpretacion(
            INTERPRETACIONES_PATH,
            "outliers"
        )

        st.markdown("### 📝 Interpretación de Outliers")
        st.markdown(interpretacion, unsafe_allow_html=True)

    # ==============================================================
    # 1️⃣0️⃣ Interpretación preliminar
    # ==============================================================

    with st.expander("📝 Interpretación Preliminar", expanded=False):

        st.write("""
        - Revisar productos con ventas decrecientes para detectar exceso de stock.
        - Identificar picos estacionales o caídas por mes.
        - La correlación cantidad–venta ayuda a detectar productos caros o de alta demanda.
        - Los outliers pueden revelar errores o ventas extraordinarias.
        """)

    # ==============================================================
    # Guardado final
    # ==============================================================

    os.makedirs("data", exist_ok=True)
    ruta_guardado = os.path.join("data", "df_tienda_aurelion_modificado.csv")

    df.to_csv(ruta_guardado, index=False)
    st.success(f"💾 Dataset guardado automáticamente en {ruta_guardado}")

    st.download_button(
        label="📥 Descargar dataset modificado",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='df_tienda_aurelion_modificado.csv',
        mime='text/csv'
    )
