<h1>Documentación de Uso de Inteligencia Artificial</h1>

<h2>Índice</h2>

- [Introducción](#introducción)
- [Sprint 01 -- Registro de uso de IA](#sprint-01----registro-de-uso-de-ia)
- [Sprint 02 -- Registro de uso de IA](#sprint-02----registro-de-uso-de-ia)
- [Sprint 03 -- Registro de uso de IA](#sprint-03----registro-de-uso-de-ia)
- [Creación del Logo](#creación-del-logo)
- [Conclusión](#conclusión)

------------------------------------------------------------------------

# Introducción

El proyecto **Tienda Aurelion** forma parte del programa *Fundamentos de
Inteligencia Artificial* (Guayerd + IBM). A lo largo del desarrollo de
los distintos Sprints, se utilizaron herramientas de asistencia como
**ChatGPT** y **GitHub Copilot** para resolver dudas técnicas, optimizar
el código e implementar funcionalidades.

Esta documentación registra de forma clara y transparente **qué partes
del desarrollo fueron asistidas por IA**, qué problemas se resolvieron y
qué soluciones se adoptaron.

<hr style="border: 2px solid #f28b20;">

# Sprint 01 -- Registro de uso de IA
<hr style="border: 2px solid #f28b20;">

<h2 style='color:#f28b20;'>Creación de aplicación</h2>

**Problema:** se pidió una propuesta integral para construir la app
completa.

**Intervención de IA:** ChatGPT generó una propuesta completa de
arquitectura y desarrollo.

**Decisión:** se rechazó para avanzar paso a paso según los
requerimientos académicos.

<h2 style='color:#f28b20;'>Creación de aplicación con Streamlit</h2>

La IA asistió con:
 - instalación de dependencias 
 - estructura base del archivo principal
 - carga de datos, menú lateral y secciones
 - lectura de archivos .md dentro de la app

Se generó un script base funcional para iniciar el proyecto.

<h2 style='color:#f28b20;'>Duplicación de columnas en la vista previa de datos</h2>

**Problema:** se mostraba dos veces la columna ID.

**Solución asistida por IA:**

``` python
df.reset_index(drop=True)
```

Eliminó el índice duplicado y mejoró la visualización.

<h2 style='color:#f28b20;'>Error con `st.write()` y parámetro no reconocido</h2>

**Error detectado:**\
`TypeError: WriteMixin.write() got an unexpected keyword argument 'use_container_width'`

**Corrección propuesta por IA:**

``` python
st.dataframe(df.describe(include="all"), use_container_width=True)
```

<h2 style='color:#f28b20;'>Scroll vertical en tablas</h2>

Se ajustó el `height` para mejorar la lectura:

``` python
st.dataframe(..., height=450)
```

<h2 style='color:#f28b20;'>Altura dinámica en tablas</h2>

La IA confirmó que Streamlit no admite altura "auto". Solo valores
fijos.

<h2 style='color:#f28b20;'>Tamaño y centrado del flujograma</h2>

**Problemas:** imagen muy grande y alineada a la izquierda.

**Soluciones proporcionadas:** - `width=600` para controlar tamaño -
columnas para alinear al centro

<h2 style='color:#f28b20;'>Resumen Sprint 01</h2>

El primer Sprint se centró en la creación de la aplicación base y su
correcta visualización. La IA fue usada para resolver errores de
ejecución, optimizar la interfaz y asistir en decisiones técnicas sobre
Streamlit.

------------------------------------------------------------------------

<hr style="border: 2px solid #1E90FF;">

# Sprint 02 -- Registro de uso de IA
<hr style="border: 2px solid #1E90FF;">

<h2 style='color:#1E90FF;'>Refinamiento de la arquitectura de la aplicación</h2>

Reorganización del layout para lograr una estructura más clara y
consistente. 

La IA propuso: 
- reordenamiento del flujo de EDA 
- limpieza de secciones repetidas 
- mejor separación de componentes

<h2 style='color:#1E90FF;'>Sección de Outliers y Distribuciones</h2>

Se implementaron: 
- `st.expander` 
- `st.columns(3)` 
- iteración automatizada sobre variables numéricas

La IA proporcionó fragmentos para violin plots, swarmplots y boxplots.

Se rechaza los graficos de violin plots.

<h2 style='color:#1E90FF;'>Corrección en gráficos de boxplot y stripplot</h2>

Ajustes recomendados por IA: 
- separación de capas entre seaborn y matplotlib 
- uso de `flierprops` 
- evitar parámetros incompatibles

<h2 style='color:#1E90FF;'>Unificación de estilos y paleta de colores</h2>

Se estandarizó: 
- paleta `PALETA[...]` 
- tamaños de gráficos 
- estructura común entre visualizaciones

<h2 style='color:#1E90FF;'>Ajustes en visualizaciones de Streamlit</h2>

La IA recomendó tamaños fijos (`figsize=(5,4)`) para mantener
consistencia visual.

<h2 style='color:#1E90FF;'>Depuración de duplicación de columnas en EDA</h2>

IA recomendó: 
- verificar `df.reset_index(drop=True)` 
- revisar lectura del CSV 
- evitar crear columnas redundantes

<h2 style='color:#1E90FF;'>Revisión de código para evitar errores de rendering</h2>

Se corrigieron parámetros inválidos y errores típicos de autocomplete.

<h2 style='color:#1E90FF;'>Resumen Sprint 02</h2>

Este sprint consolidó la calidad visual del EDA y la interacción dentro
de Streamlit. La IA funcionó como soporte para ajustes finos y
depuración.

------------------------------------------------------------------------

<hr style="border: 2px solid #34C759;">

# Sprint 03 -- Registro de uso de IA
<hr style="border: 2px solid #34C759;">

<h2 style='color:#34C759;'>Implementación del Modelo Random Forest Manual</h2>

**Problema**: se requería construir un modelo de Random Forest configurable manualmente, con hiperparámetros editables y métricas completas.

**Intervención de IA**:

La IA ayudó a:
- definir los parámetros principales (n_estimators, max_depth, criterion, random_state)
- generar la estructura base del entrenamiento manual
- validar el flujo del proceso (split → entrenamiento → métricas → gráficos)
- corregir errores en la lectura de hiperparámetros desde Streamlit

**Decisión**: se utilizaron las recomendaciones para estructurar el código final, manteniendo orden y claridad.

<h2 style='color:#34C759;'>Corrección de errores en Streamlit durante el entrenamiento</h2>

Durante el desarrollo surgieron errores frecuentes:

🔹 Error: UnboundLocalError: local variable 'sns' referenced before assignment

Solución asistida por IA:
- Confirmar la importación de seaborn al inicio del archivo
- Eliminar imports duplicados
- Reorganizar el orden de funciones que generaban override del alias sns

<h2 style='color:#34C759;'>Estilización de la Interfaz</h2>

La IA asistió en mejoras visuales, incluyendo:

🔹 Ajustes en títulos y tamaños de letra

Se ofrecieron alternativas como:

```Python
st.markdown("<h3 style='font-size:18px;'>Título</h3>", unsafe_allow_html=True)
```

🔹 Cambios en la visibilidad de subtítulos

Ejemplo solicitado:

- Hacer un título más pequeño
- Reducir tamaño en "Curva ROC Multiclase"

<h2 style='color:#34C759;'>Gráficos del Modelo (ROC, Matriz de Confusión, Reportes)</h2>

Intervenciones de IA:
- corrección de errores al generar la curva ROC
- estandarización del uso de fig, ax = plt.subplots()
- manejo correcto para casos binarios vs multiclase
- recomendaciones para escalas más legibles en matriz de confusión

<h2 style='color:#34C759;'>Optimización de métricas y estructura del código</h2>

La IA propuso mejoras para:
- mostrar métricas agrupadas en contenedores o columnas
- evitar repeticiones entre la versión manual y automática
- corregir errores en f1-score con clases desbalanceadas
- agregar mensajes claros sobre cantidad de registros en train / test
- validar condiciones como if y.nunique() == 2 para gráficos binarios

<h2 style='color:#34C759;'>Soluciones a errores de visualización</h2>

La IA ayudó a solucionar:

🔹 Advertencia por use_column_width

Se actualizó a:

```Python
st.image(..., use_container_width=True)
```

🔹 Imágenes demasiado pequeñas

Se propuso aumentar el tamaño en:

```Python
st.image(..., width=700)
```

<h2 style='color:#34C759;'>Ajustes en la organización del proyecto</h2>

Propuestas de la IA:
- mover funciones reutilizables a archivos auxiliares
- usar una estructura más modular para páginas, modelos y utilidades
- evitar carga innecesaria del dataset en cada sección

<h2 style='color:#34C759;'>Resumen Sprint 03</h2>

En este sprint, la IA desempeñó un rol clave en:
- resolver errores de ejecución
- mejorar la experiencia visual
- optimizar el flujo del modelo Random Forest
- corregir código redundante y errores típicos de librerías
- estandarizar métricas y gráficos

------------------------------------------------------------------------

# Creación del Logo

Prompt utilizado en Copilot Desktop:

    quiero que hagas el logo para un supermercado minorista llamado Aurelion, quiero que tenga colores vibrantes, que sea de tamaño rectangular, donde se vean diferentes productos comestibles y en el medio que se destaque el nombre del comercio.

------------------------------------------------------------------------

# Conclusión

La integración de herramientas de inteligencia artificial permitió acelerar el desarrollo del proyecto, resolver problemas técnicos y mejorar la calidad del código. Gracias a su asistencia, se logró mantener coherencia visual y funcional en la aplicación, optimizar la implementación de los modelos de aprendizaje automático y asegurar un funcionamiento estable y claro.