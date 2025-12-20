#src/pages/estadisticas.py
import io
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_loader import get_dataset_paths, load_dataset
from src.utils.palette import PALETA, COLORES_BARRAS, COLORES_PIE

def show_statistics():
    """
    Muestra estadísticas descriptivas y visualizaciones interactivas
    de un dataset seleccionado por el usuario en Streamlit.

    Flujo principal:
    1. Filtra los datasets disponibles para excluir el unificado.
    2. Permite al usuario seleccionar un dataset.
    3. Si el dataset se carga correctamente:
        - Muestra información general, valores nulos y únicos.
        - Muestra resumen estadístico.
        - Si es "Detalle Ventas", genera un mapa de correlación.
        - Genera visualizaciones específicas según el tipo de dataset.
    4. Si el dataset no se puede cargar, muestra advertencia en pantalla.

    Notas:
    - Todas las visualizaciones se muestran directamente en la app
      de Streamlit.
    - La función no recibe parámetros y no devuelve ningún valor.
    """
    
    st.subheader("📊 Estadísticas descriptivas de cada dataset")
       
    # --- Elegir dataset ---
    # Obtiene la lista de datasets disponibles y elimina el dataset unificado
    dataset_paths = get_dataset_paths()

    # Filtrar el archivo unificado (por nombre clave o coincidencia parcial)
    dataset_paths = {k: v for k, v in dataset_paths.items() if "tienda_aurelion" not in k.lower()}

    # Menú de selección
    dataset_nombre = st.selectbox("Selecciona el dataset:", list(dataset_paths.keys()))
    
    df = load_dataset(dataset_nombre)
    
    if df is not None:
        # --- Información general ---
        # Muestra número de registros y columnas, y los tipos de cada columna
        st.markdown(f"**Información general de {dataset_nombre}:**")
        st.write(f"- Número de registros: {df.shape[0]}")
        st.write(f"- Número de columnas: {df.shape[1]}")
        st.write("**Tipos de columnas:**")
        st.table(pd.DataFrame(df.dtypes, columns=["Tipo"]).reset_index().rename(columns={"index":"Columna"}))


        # --- Valores nulos ---
        # Muestra la cantidad de valores faltantes por columna
        st.markdown("**Valores faltantes por columna:**")
        st.table(df.isnull().sum().reset_index().rename(columns={"index":"Columna", 0:"Nulos"}))


        # --- Valores únicos ---
        # Muestra la cantidad de valores únicos por columna
        st.markdown("**Cantidad de valores únicos por columna:**")
        st.table(df.nunique().reset_index().rename(columns={"index":"Columna", 0:"Valores únicos"}))


        # --- Estadísticas descriptivas ---
        # Tabla resumen con estadísticas de todas las columnas
        st.markdown("**Resumen estadístico:**")
        st.dataframe(df.describe(include="all"), height=400, use_container_width=True)

                   
        # --- Mapa de correlación ---
        # Solo se muestra para el dataset "Detalle Ventas"
        if dataset_nombre == "Detalle Ventas":
            numeric_cols = df.select_dtypes(include='number').columns
            if len(numeric_cols) > 1:
                st.markdown("**Mapa de correlación (numéricas):**")
                corr = df[numeric_cols].corr()
                fig, ax = plt.subplots(figsize=(max(5, len(numeric_cols)*0.5), max(5, len(numeric_cols)*0.5)))
                sns.heatmap(corr, cmap=sns.diverging_palette(25, 220, s=70, l=40, as_cmap=True), center=0)
                plt.tight_layout()
                buf = io.BytesIO()
                fig.savefig(buf, format="png", dpi=100)
                buf.seek(0)
                st.image(buf)            
            

        # --- Función auxiliar para mostrar figuras ---
        # Convierte la figura de Matplotlib a imagen para Streamlit
        def mostrar_fig(fig, ancho=500):
            buf = io.BytesIO()
            fig.savefig(buf, format="png", dpi=120, bbox_inches='tight')
            buf.seek(0)
            st.image(buf, width=ancho)
            plt.close(fig)


        # --- Visualizaciones específicas por dataset ---
        if dataset_nombre == "Clientes":
            st.markdown("### Clientes")
            # Clientes por ciudad (barras)
            fig, ax = plt.subplots()
            df['ciudad'].value_counts().plot(kind='bar', ax=ax, color=COLORES_BARRAS)
            ax.set_ylabel('Cantidad de Clientes')
            ax.set_title('Clientes por Ciudad')
            mostrar_fig(fig, ancho=500)

            # Clientes registrados por mes (barras)
            fig, ax = plt.subplots()
            df['fecha_alta'] = pd.to_datetime(df['fecha_alta'])
            df['fecha_alta'].dt.to_period('M').value_counts().sort_index().plot(kind='bar', ax=ax, color=COLORES_BARRAS)
            ax.set_title('Clientes registrados por mes')
            ax.set_ylabel('Cantidad')
            mostrar_fig(fig, ancho=500)

        elif dataset_nombre == "Productos":
            st.markdown("### Productos")
            # Distribución de precios unitarios (histograma) con media y mediana
            fig, ax = plt.subplots()
            sns.histplot(df['precio_unitario'], bins=20, kde=True, color=PALETA["suave"], ax=ax)
            media = df['precio_unitario'].mean()
            mediana = df['precio_unitario'].median()
            ax.axvline(media, color=PALETA["acento1"], linestyle='--', linewidth=2, label=f'Media: {media:.2f}')
            ax.axvline(mediana, color=PALETA["claro"], linestyle='-', linewidth=2, label=f'Mediana: {mediana:.2f}')
            ax.set_title('Distribución de precios unitarios')
            ax.set_xlabel('Precio unitario ($)')
            ax.legend()
            mostrar_fig(fig, ancho=500)

            # Cantidad de productos por categoría (barras)
            fig, ax = plt.subplots()
            df['categoria'].value_counts().plot(
                kind='bar',
                ax=ax,
                color=[COLORES_BARRAS[i % len(COLORES_BARRAS)] for i in range(len(df['categoria'].value_counts()))]
            )
            ax.set_ylabel('Cantidad de productos')
            ax.set_title('Cantidad de productos por categoría')
            mostrar_fig(fig, ancho=500)

        elif dataset_nombre == "Ventas":
            st.markdown("### Ventas")
            
            # Ventas por mes (barras)
            fig, ax = plt.subplots()
            df['fecha'] = pd.to_datetime(df['fecha'])
            df['fecha'].dt.to_period('M').value_counts().sort_index().plot(kind='bar', ax=ax, color=COLORES_BARRAS)
            ax.set_title('Ventas por mes')
            ax.set_ylabel('Cantidad de ventas')
            mostrar_fig(fig, ancho=500)

            # Distribución de medios de pago (pie)
            fig, ax = plt.subplots()
            df['medio_pago'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax,
                                                 colors=COLORES_PIE)
            ax.set_ylabel('')
            ax.set_title('Distribución de medios de pago')
            mostrar_fig(fig, ancho=500)

        elif dataset_nombre == "Detalle Ventas":
            st.markdown("### Detalle de Ventas")
            
            # Cantidad vendida por producto (histograma) con media y mediana
            fig, ax = plt.subplots()
            sns.histplot(df['cantidad'], bins=5, kde=False, color=PALETA["principal"], ax=ax)
            media = df['cantidad'].mean()
            mediana = df['cantidad'].median()
            ax.axvline(media, color=PALETA["acento2"], linestyle='--', linewidth=2, label=f'Media: {media:.2f}')
            ax.axvline(mediana, color=PALETA["secundario"], linestyle='-', linewidth=2, label=f'Mediana: {mediana:.2f}')
            ax.set_title('Distribución de cantidad vendida por producto')
            ax.set_xlabel('Cantidad')
            ax.legend()
            mostrar_fig(fig, ancho=500)

            # Importe por ítem (histograma) con media y mediana
            fig, ax = plt.subplots()
            sns.histplot(df['importe'], bins=10, kde=False, color=PALETA["principal"], ax=ax)
            media = df['importe'].mean()
            mediana = df['importe'].median()
            ax.axvline(media, color=PALETA["acento2"], linestyle='--', linewidth=2, label=f'Media: {media:.2f}')
            ax.axvline(mediana, color=PALETA["secundario"], linestyle='-', linewidth=2, label=f'Mediana: {mediana:.2f}')
            ax.set_title('Distribución del importe por ítem')
            ax.set_xlabel('Importe')
            ax.legend()
            mostrar_fig(fig, ancho=500)

    else:
        # Mensaje de error si no se pudo cargar el dataset
        st.warning("No se pudo cargar el dataset seleccionado.")