# src/data_loader.py
import os
import pandas as pd
import streamlit as st

# ==============================================================
# 🟢 CONFIGURACIÓN DE RUTAS
# ==============================================================

def get_dataset_paths():
    """
    Retorna un diccionario con los paths de los datasets disponibles.
    Las claves son los nombres amigables y los valores las rutas absolutas.
    """
    ruta_actual = os.path.dirname(__file__)
    return {
        "Clientes": os.path.join(ruta_actual, "..", "data", "clientes.xlsx"),
        "Productos": os.path.join(ruta_actual, "..", "data", "productos.xlsx"),
        "Ventas": os.path.join(ruta_actual, "..", "data", "ventas.xlsx"),
        "Detalle Ventas": os.path.join(ruta_actual, "..", "data", "detalle_ventas.xlsx"),
        "df_tienda_aurelion": os.path.join(ruta_actual, "..", "data", "df_tienda_aurelion.csv")
    }

# ==============================================================
# 🟢 CARGA GENERAL DE DATASETS
# ==============================================================

@st.cache_data
def load_dataset(nombre):
    """
    Carga un dataset desde la carpeta 'data' en formato Excel (.xlsx/.xls) o CSV (.csv).
    Si es el dataset unificado y no existe, lo genera automáticamente.
    """
    paths = get_dataset_paths()
    
    if nombre not in paths:
        st.warning(f"⚠️ Dataset '{nombre}' no encontrado.")
        return None

    ruta = paths[nombre]

    # --- Si es el dataset unificado y no existe, generarlo ---
    if nombre == "df_tienda_aurelion" and not os.path.exists(ruta):
        # El mensaje de "no encontrado" lo mostramos dentro de load_and_merge_datasets
        return load_and_merge_datasets()
    
    try:
        if ruta.endswith((".xlsx", ".xls")):
            df = pd.read_excel(ruta)
        elif ruta.endswith(".csv"):
            df = pd.read_csv(ruta, encoding="utf-8-sig")
        else:
            st.warning(f"⚠️ Formato de archivo no soportado: {ruta}")
            return None

        return df

    except Exception as e:
        st.warning(f"⚠️ Error al cargar '{nombre}': {e}")
        return None

# ==============================================================
# 🟢 UNIFICACIÓN DE LOS DATASETS
# ==============================================================

def unificar_datasets(clientes_path, ventas_path, detalle_ventas_path, productos_path):
    """
    Carga y unifica los datasets de clientes, ventas, detalle de ventas y productos.
    Retorna un DataFrame final llamado df_unificado.
    """

    # --- 1️⃣ Cargar los archivos ---
    clientes = pd.read_excel(clientes_path)
    ventas = pd.read_excel(ventas_path)
    detalle_ventas = pd.read_excel(detalle_ventas_path)
    productos = pd.read_excel(productos_path)

    # --- 2️⃣ Merge clientes + ventas ---
    df_1 = pd.merge(
        clientes,
        ventas,
        on="id_cliente",
        how="left",
        suffixes=("_cliente", "_venta")
    )

    # --- 3️⃣ Merge ventas + clientes ---
    ventas_clientes = pd.merge(ventas, clientes, on=['id_cliente','nombre_cliente','email'], how='left')

    # --- 4️⃣ Merge detalle_ventas + productos ---
    detalle_productos = pd.merge(detalle_ventas, productos, on=['id_producto','nombre_producto','precio_unitario'], how='left')

    # --- 5️⃣ Merge final: ventas_clientes + detalle_productos ---
    df_unificado = pd.merge(ventas_clientes, detalle_productos, on='id_venta', how='left')

    # --- 6️⃣ Limpieza y ajustes finales ---
    df_unificado['total_venta'] = df_unificado['cantidad'] * df_unificado['precio_unitario']
    df_unificado['fecha'] = pd.to_datetime(df_unificado['fecha'])

    return df_unificado

def load_and_merge_datasets():
    """
    Crea el dataset unificado y lo guarda como CSV.
    """
    paths = get_dataset_paths()

    df_unificado = unificar_datasets(
        clientes_path=paths["Clientes"],
        ventas_path=paths["Ventas"],
        detalle_ventas_path=paths["Detalle Ventas"],
        productos_path=paths["Productos"]
    )

    if df_unificado is not None:
        output_path = paths["df_tienda_aurelion"]
        # Asegurarse de que la carpeta existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df_unificado.to_csv(output_path, index=False, encoding="utf-8-sig")
        st.success(f"✅ Dataset unificado generado y guardado en: {output_path}")
    else:
        st.error("❌ No se pudo generar el dataset unificado.")
    
    return df_unificado

# ==============================================================
# 🟢 VERIFICACIÓN DEL DATAFRAME UNIFICADO
# ==============================================================

def verificar_unificacion_streamlit(df):
    """
    Muestra información básica del DataFrame unificado en Streamlit.
    """
    if df is None or df.empty:
        st.warning("⚠️ No hay datos disponibles para verificar.")
        return

    st.subheader("✅ Verificación de Unificación")
    st.write(f"**Dimensiones del DataFrame:** {df.shape[0]} filas x {df.shape[1]} columnas")

    st.write("### Columnas del DataFrame")
    st.write(list(df.columns))

    st.write("### Vista previa de las primeras filas")
    st.dataframe(df.head())

