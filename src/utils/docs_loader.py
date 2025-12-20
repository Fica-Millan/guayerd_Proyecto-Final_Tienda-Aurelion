#src/utils/docs_loader.py

import re

def cargar_interpretacion(path, seccion):
    with open(path, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Buscar sección tipo ## nombre_seccion
    patron = rf"#### {seccion}\n(.*?)(?=\n#### |\Z)"
    match = re.search(patron, contenido, re.DOTALL)

    if match:
        return match.group(1).strip()
    return "⚠️ Interpretación no encontrada en documentación."
