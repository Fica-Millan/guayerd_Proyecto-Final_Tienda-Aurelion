"""
Script ETL para preparar dataset de productos corregido para Power BI
Sprint 4 - Curso Análisis de Datos
"""

import pandas as pd
import re
import sys
from pathlib import Path
from src.utils.classification import clasificar_producto
from src.utils.validation import verificar_fallbacks

# Agregar src al path para importar rules
sys.path.append(str(Path(__file__).parent.parent))
from src.utils.rules import EXACT, RULES


def main():
    """
    Función principal del script ETL
    """
    print("=" * 60)
    print("PREPARACIÓN DE DATOS PARA POWER BI - SPRINT 4")
    print("=" * 60)
    print()
    
    # Rutas
    input_path = Path("data/productos.xlsx")
    output_path = Path("data/productos_corregidos.xlsx")
    
    # Verificar que existe el archivo original
    if not input_path.exists():
        print(f"❌ ERROR: No se encuentra {input_path}")
        print("   Verifica que el archivo esté en la carpeta 'data/'")
        return
    
    # Cargar dataset original
    print(f"📂 Cargando {input_path}...")
    df_productos = pd.read_excel(input_path)
    print(f"✅ Dataset cargado: {len(df_productos)} productos")
    print()
    
    # Mostrar columnas disponibles
    print("📋 Columnas encontradas:")
    for col in df_productos.columns:
        print(f"   - {col}")
    print()
    
    # Verificar columna nombre_producto
    if "nombre_producto" not in df_productos.columns:
        print("❌ ERROR: No se encuentra la columna 'nombre_producto'")
        return
    
    # Aplicar recategorización
    print("🔄 Aplicando recategorización...")
    df_productos["categoria_corregida"] = df_productos["nombre_producto"].apply(clasificar_producto)
    print("✅ Recategorización completada")
    print()
    
    # Mostrar resumen de categorías
    print("📊 RESUMEN DE CATEGORÍAS:")
    print("-" * 60)
    categoria_counts = df_productos["categoria_corregida"].value_counts()
    for categoria, count in categoria_counts.items():
        print(f"   {categoria:.<45} {count:>4} productos")
    print("-" * 60)
    print(f"   {'TOTAL':.<45} {len(df_productos):>4} productos")
    print()
    
    # Verificar fallbacks
    print("🔍 Verificando productos en fallback...")
    alimentos_reales, fallas = verificar_fallbacks(df_productos)
    
    print(f"   🔹 Alimentos secos legítimos: {len(alimentos_reales)}")
    print(f"   🔸 Productos en fallback sin keywords: {len(fallas)}")
    print()
    
    # Guardar dataset corregido
    print(f"💾 Guardando dataset corregido en {output_path}...")
    df_productos.to_excel(output_path, index=False)
    print("✅ Archivo guardado exitosamente")
    print()
    
if __name__ == "__main__":
    main()