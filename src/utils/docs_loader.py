#src/utils/docs_loader.py

import re

def extraer_seccion(contenido, titulo):
    patron = (
        r"###\s+"
        + re.escape(titulo) +
        r"\n(.*?)"
        r"(?=\n###\s+|\Z)"
    )

    match = re.search(patron, contenido, re.DOTALL)
    return match.group(1) if match else None


def cargar_interpretacion(path, grafica):
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


