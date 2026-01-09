#src/utils/docs_loader.py

import re

def extraer_seccion(contenido, titulo):
    """
    Extrae el contenido de una sección Markdown identificada por un título.

    Busca dentro del texto completo la sección que comienza con un encabezado
    de nivel 3 (### <titulo>) y devuelve su contenido hasta el siguiente
    encabezado del mismo nivel o el final del documento.

    Parámetros:
    - contenido (str): Texto completo en formato Markdown.
    - titulo (str): Título exacto de la sección a extraer.

    Retorna:
    - str | None: Contenido de la sección encontrada, o None si no existe.
    """
    
    patron = (
        r"###\s+"
        + re.escape(titulo) +
        r"\n(.*?)"
        r"(?=\n###\s+|\Z)"
    )

    match = re.search(patron, contenido, re.DOTALL)
    return match.group(1) if match else None


def cargar_interpretacion(path, grafica):
    """
    Obtiene la interpretación textual asociada a una gráfica desde un archivo Markdown.

    Busca dentro del archivo la sección correspondiente a una gráfica específica,
    identificada por el encabezado:
    #### 🔸 Gráfica: <grafica>

    Parámetros:
    - path (str): Ruta al archivo Markdown de documentación.
    - grafica (str): Nombre exacto de la gráfica a buscar.

    Retorna:
    - str: Texto de interpretación encontrado o un mensaje de advertencia si no existe.
    """
    with open(path, "r", encoding="utf-8") as f:
        contenido = f.read()

    patron = (
        r"####\s+🔸\s+Gráfica:\s*"
        + re.escape(grafica) +
        r"\n(.*?)"
        r"(?=\n---|\n####\s+🔸\s+Gráfica:|\Z)"
    )

    match = re.search(patron, contenido, re.DOTALL)

    if match:
        return match.group(1).strip()

    return "⚠️ Interpretación no encontrada en documentación."


