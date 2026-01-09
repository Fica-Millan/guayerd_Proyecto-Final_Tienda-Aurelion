# src/utils/rules.py

"""
rules.py
--------

Definición de reglas de clasificación de productos a categorías comerciales.

El módulo contiene dos niveles de reglas:
1) Clasificaciones exactas por nombre de producto.
2) Clasificaciones basadas en expresiones regulares aplicadas sobre el texto normalizado.

Estas reglas se utilizan para inferir la categoría de un producto a partir
de su descripción textual cuando no existe una clasificación explícita.
"""

import re

# ==============================================================
# 1️⃣ Clasificaciones exactas
# ==============================================================
EXACT = {
    "medialunas de manteca": "Panificados",
    "medialuna de manteca":  "Panificados",
    "helado chocolate 1L": "Congelados",
    "caldo concentrado verdura": "Alimentos secos",
    "yogur natural 200g": "Lácteos y refrigerados"
}

# ==============================================================
# 2️⃣ Clasificaciones por regex
# ==============================================================

RULES = {
    "Bebidas sin alcohol": [
        r"\bcoca\b", r"\bpepsi\b", r"\bsprite\b", r"\bfanta\b",
        r"\bagua\b", r"\bmineral\b", r"\bjugo\b", r"\bpolvo\b",
        r"\bbebida\b", r"\bnitro\b", r"\benerg(ética|etica|etic)\b"
    ],

    "Bebidas alcohólicas": [
        r"\bcerveza\b", r"\bfernet\b", r"\bvodka\b", r"\bwhisky\b",
        r"\bron\b", r"\bgin\b", r"\bsidra\b", r"\bvin(o)?\b", r"\blicor\b"
    ],

    "Congelados": [
        r"\bcongelad[oa]s?\b", r"\bempanad[ao]s?\b", r"\bhamburguesa\b",
        r"\bpizza\b", r"\bhelado(s)?\b", r"\bverdura(s)?\b"
    ],

    "Panificados": [
        r"\bpan\b", r"\blactal\b", r"\bmedialuna(s)?\b", r"\bfactura(s)?\b", r"\bmedialunas? de manteca\b"
    ],

    "Snacks y golosinas": [
        r"\balfajor(es)?\b", r"\bpapas?\b", r"\bfritas\b", r"\bman[ií]\b",
        r"\bbizcocho(s)?\b", r"\bturr[oó]n\b", r"\bchocolate\b",
        r"\bgalletita(s)?\b", r"\bcereal(es)?\b", r"\bbarrita(s)?\b",
        r"\bcaramelo(s)?\b", r"\bchicle(s)?\b", r"\bchupet(e)?\b", r"\bchupet[ií]n\b"
    ],

    "Lácteos y refrigerados": [
        r"\bleche\b", r"\byogur?t\b", r"\bqueso\b", r"manteca\b",
        r"\buntable\b", r"\bcremoso\b", r"\brallado\b", r"\bazul\b"
    ],
    
    "Infusiones": [
        r"\byerba\b",
        r"\bt[eé]\b",
        r"\bcaf[eé]\b",
        r"\binfusi[oó]n(es)?\b",
        r"\bstevia\b"
    ],

    "Higiene personal": [
        r"\bshampoo\b", r"\bjab[oó]n\b", r"\b(dental|cepillo)\b",
        r"\bhilo\b", r"\bcapilar\b", r"\bdesodorante\b",
        r"\bmascarilla\b", r"\btoalla\b", r"\bh[uú]meda(s)?\b"
    ],

    "Limpieza del hogar": [
        r"\bdetergente\b", r"\blavandina\b", r"\blimpiavidrios\b",
        r"\bdesengrasante\b", r"\besponja(s)?\b", r"\bsuavizante\b",
        r"\btrapo\b", r"\bservilleta(s)?\b", r"\bpapel higi[eé]nico(s)?\b"
    ],

    "Alimentos secos": [
        r"\baceite\b", r"\bvinagre\b", r"\barroz\b", r"\bharina\b",
        r"\baz[uú]car\b", r"\bsal\b", r"\bsalsa\b", r"\btomate\b",
        r"\bgarbanzo(s)?\b", r"\blenteja(s)?\b", r"\bporoto(s)?\b",
        r"\bfideos\b", r"\bspaghetti\b", r"\baceituna(s)?\b",
        r"\bmiel\b", r"\bgranola\b", r"\bfrutos?\b", r"\bavena\b",
        r"\bsopa\b", r"\bcaldo\b", r"\bmermelada\b", r"\bdurazno\b",
        r"\bfrutilla\b", r"\binstant[áa]ne[ao]\b", r"\bsec[ao]s?\b"
    ]
}
