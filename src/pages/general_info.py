#src/pages/info_general.py
import os
import pandas as pd
import streamlit as st
from src.data_loader import get_dataset_paths, load_dataset

def show_general_info():
    """
    Muestra información general de un dataset seleccionado por el usuario.

    Flujo principal:
    1. Permite seleccionar un dataset de los disponibles.
    2. Si el dataset se carga correctamente:
        - Muestra la fecha de última modificación y tamaño del archivo.
        - Muestra las primeras filas del dataset.
        - Muestra la estructura de columnas y sus tipos.
        - Muestra la cantidad total de registros.
    3. Si no se puede cargar el dataset, muestra una advertencia en pantalla.

    Notas:
    - Todas las visualizaciones y mensajes se muestran directamente
      en la app de Streamlit.
    - La función no recibe parámetros y no devuelve ningún valor.
    """
    
    st.subheader("📄 Información general de cada dataset")
    dataset_paths = get_dataset_paths()
    
    datasets_visibles = {k: v for k, v in dataset_paths.items() if k != "df_tienda_aurelion"}

    dataset = st.selectbox("Seleccione el dataset:", list(datasets_visibles.keys()))
    df = load_dataset(dataset)

    if df is not None:
        ruta = dataset_paths[dataset]
        if os.path.exists(ruta):
            info = os.stat(ruta)
            fecha_mod = pd.to_datetime(info.st_mtime, unit='s').strftime('%d/%m/%Y %H:%M')
            tamano_kb = round(info.st_size / 1024, 2)
            st.caption(f"📅 **Última modificación:** {fecha_mod}")
            st.caption(f"💾 **Tamaño del archivo:** {tamano_kb} KB")

        st.write("**Vista previa de los datos:**")
        st.dataframe(df.head(), use_container_width=True)

        st.write("**Estructura de columnas y tipos:**")
        tipos_df = pd.DataFrame({
            "Columna": df.columns,
            "Tipo de dato": df.dtypes.astype(str)
        })
        st.table(tipos_df)
        st.write("**Cantidad de registros:**", df.shape[0])
    else:
        st.warning("No se pudo cargar el dataset seleccionado.")
