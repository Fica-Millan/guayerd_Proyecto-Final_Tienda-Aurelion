#src/pages/automated_ml.py

import streamlit as st
import pandas as pd
from pycaret.classification import *
import os
import pickle 

def show_automated_ml():
    """
    Interfaz de Streamlit para comparar modelos de clasificación utilizando PyCaret.

    Flujo de la función:
    1. Carga el dataset preprocesado desde 'data/dataset_ml_productos.csv'.
    2. Permite configurar el experimento de PyCaret (normalización, 
       eliminación de multicolinealidad y selección de características).
    3. Compara automáticamente todos los modelos disponibles y muestra 
       la tabla de métricas y el mejor modelo encontrado.

    Requisitos:
    - El archivo 'dataset_ml_productos.csv' debe existir en la carpeta 'data'.
    - PyCaret debe estar instalado y compatible con la versión de Python usada.

    Estados de sesión:
    - 'best_model': almacena el mejor modelo encontrado por la comparación automática
      para poder usarlo posteriormente en otra página.

    Uso:
    Esta función se integra dentro de una aplicación Streamlit como una página 
    que permite ejecutar de forma rápida un benchmarking automático de modelos 
    de clasificación para facilitar la selección del modelo a desarrollar manualmente.
    """

    st.subheader("AutoML: Benchmarking de Modelos")
    st.markdown(
        '<p style="font-size: 22px;">En esta sección se comparan modelos de clasificación utilizando '
        '<span style="color: orange; font-weight:600;">PyCaret.</span></p>',
        unsafe_allow_html=True
    )


    # ==============================================================
    # 1️⃣ Cargar dataset procesado
    # ==============================================================

    st.markdown("### 1. Carga del dataset preparado")

    try:
        df = pd.read_csv("data/dataset_ml_productos.csv")
        st.success("Dataset cargado correctamente.")
        st.dataframe(df.head())
    except Exception as e:
        st.error("⚠️ No se encontró `data/dataset_ml_productos.csv`. Ejecutá la página de preprocesamiento primero.")
        st.write(e)
        st.stop()

    # objetivo
    target = "nivel_demanda"
    if target not in df.columns:
        st.error(f"La columna objetivo '{target}' no está en el dataset.")
        st.stop()

    # ==============================================================
    # 2️⃣ Configurar experimento
    # ==============================================================

    st.markdown("### 2. Configuración del experimento")

    normalize = st.checkbox(
        "Normalizar variables",
        value=True,
        help="Escala todas las variables numéricas para mejorar el rendimiento de varios modelos."
    )

    remove_multicollinearity = st.checkbox(
        "Remover multicolinealidad",
        value=True,
        help="Elimina variables muy correlacionadas entre sí para evitar sobreajuste."
    )
    
    # Inicializar estados de sesión
    if 'modelo_comparado' not in st.session_state:
        st.session_state.modelo_comparado = False
    if 'modelo_descargado' not in st.session_state:
        st.session_state.modelo_descargado = False

    if st.button("Inicializar PyCaret"):
        with st.spinner("Inicializando experimento..."):
            exp = setup(
                data=df,
                target=target,
                session_id=789,
                normalize=normalize,
                remove_multicollinearity=remove_multicollinearity,
                verbose=False
            )
        st.success("Experimento inicializado.")
        st.write("Configuración establecida exitosamente:")
        st.code(exp)
        
        # Mostrar detalles internos de la configuración
        st.markdown("#### 🟠 Información del experimento")

        # Obtener datos del split
        train_df = get_config("train")
        test_df = get_config("test")

        train_count = train_df.shape[0]
        test_count = test_df.shape[0]
        total = train_count + test_count

        train_ratio = train_count / total
        test_ratio = test_count / total

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Train/Test Split:** {train_ratio:.2f} / {test_ratio:.2f}")

            # Obtener folds desde fold_generator
            fold_value = get_config("fold_generator").n_splits
            st.write("**Cross-validation folds:**", fold_value)

        with col2:
            st.write(f"**Registros en entrenamiento:** {train_count}")
            st.write(f"**Registros en test:** {test_count}")

    # ==============================================================
    # 3️⃣ Comparar modelos
    # ==============================================================

    st.markdown("### 3. Comparación automática de modelos")

    if st.button("Comparar todos los modelos"):
        with st.spinner("Entrenando y comparando modelos..."):
            best_model = compare_models(sort="AUC")

        st.success("Comparación completada.")
        
        # Mostrar tabla de métricas
        results = pull()
        st.write("### 📊 Métricas de los modelos comparados")
        st.dataframe(results)

        st.write("### 🏆 Mejor modelo encontrado:")
        st.write(best_model)
               
        # Guardar en session_state para uso posterior
        st.session_state["best_model"] = best_model
        st.session_state.modelo_comparado = True    # ✅ ACTIVAR ESTADO
        st.session_state.modelo_descargado = False  # ✅ RESETEAR DESCARGAS


    # ===============================================================
    # 4️⃣ DESCARGAR MODELO - SOLO SI SE COMPARÓ MODELOS
    # ===============================================================
    
    # Mostrar sección 4 solo si se completó la comparación
    if st.session_state.modelo_comparado:
        st.markdown("### 4. Descargar Modelo Entrenado")
        
        best_model = st.session_state["best_model"]
        
        # Convertir modelo a bytes para descarga
        model_bytes = pickle.dumps(best_model)
            
        # Botón de descarga - cuando se hace click, activa el estado
        if st.download_button(
            "📥 Descargar Modelo AutoML (.pkl)",
            model_bytes,
            "auto_ml_model.pkl",
            mime="application/octet-stream"
        ):
            # Este código se ejecuta SOLO después de hacer click en descargar
            st.session_state.modelo_descargado = True
            
            # Guardado automático en /models
            os.makedirs("models", exist_ok=True)
            ruta_modelo = "models/auto_ml_model.pkl"

            # Guardar el modelo entrenado
            with open(ruta_modelo, "wb") as f:
                pickle.dump(best_model, f)

        # ✅ MOSTRAR VALIDACIONES SOLO DESPUÉS DE DESCARGAR
        if st.session_state.modelo_descargado:
            st.success("✅ Modelo guardado automáticamente en: `models/auto_ml_model.pkl`")
            st.info(f"**Modelo guardado:** {type(best_model).__name__}")
            
            # Opcional: Mostrar características del modelo guardado
            with st.expander("🔍 Detalles del modelo guardado"):
                st.write(f"**Parámetros del modelo:**")
                st.json(best_model.get_params())
                st.write(f"**Clases:** {best_model.classes_}")
                st.write(f"**Número de características:** {best_model.n_features_in_}")
        