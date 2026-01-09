# src/utils/classification.py

import re
from src.utils.rules import RULES, EXACT

def clasificar_producto(nombre): 
    """
    Clasifica un producto en una categoría de negocio a partir de su nombre,
    aplicando reglas jerárquicas basadas en coincidencias exactas y patrones
    regex predefinidos.

    La clasificación se realiza en el siguiente orden:
    1. Coincidencia exacta contra el diccionario EXACT.
    2. Coincidencia por expresiones regulares definidas en RULES.
    3. Asignación por fallback a la categoría 'Alimentos secos' si no se
       encuentra ninguna coincidencia.

    Parámetros
    ----------
    nombre : str
        Nombre del producto a clasificar.

    Retorna
    -------
    str
        Categoría asignada según las reglas de clasificación.
    """             
                                             
    texto = nombre.lower()

    # 1) Coincidencia exacta
    if texto in EXACT:
        return EXACT[texto]

    # 2) Coincidencia por regex
    # Recorrer categorías y keywords
    for categoria, patrones in RULES.items():
        for patron in patrones:
            if re.search(patron, texto):
                return categoria

    # Fallback final
    return "Alimentos secos"
                                                                                                                                  