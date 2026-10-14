# marco morquecho 1440
import sys
import os
import pandas as pd
import io

# Permitir importar dicc_1440.py desde la subcarpeta hermana 'datos-de-entrada-ml-1440'
ruta_entrada = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-1440'))
if ruta_entrada not in sys.path:
    sys.path.insert(0, ruta_entrada)

import dicc_1440 

encabezado_pie = "marco morquecho Machine Learning pandas, NC 1440"
print(encabezado_pie)

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame usando la variable correcta: datos_marcas
df = pd.DataFrame(dicc_1440.datos_marcas)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head) 1440", df.head(2))
registrar("2.2 Últimas Filas (tail) 1440", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas) 1440", df.shape)
registrar("2.4 Tipos de Datos por Columna 1440", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info) 1440", buffer.getvalue())

# 3. Estadísticas Generales de la Columna Numérica (Precio_promedio)
registrar("3. Estadísticas Generales de la Columna 'Precio_promedio'", df['Precio_promedio'].describe())

# 4. Ordenar Ascendente por Precio Promedio
df_asc_precio = df.sort_values(by="Precio_promedio", ascending=True)
registrar("4. Ordenar Ascendente por Precio_promedio", df_asc_precio)

# 5. Ordenar Descendente por País
df_desc_pais = df.sort_values(by="Pais", ascending=False)
registrar("5. Ordenar Descendente por País", df_desc_pais)

# 6. Guardar el archivo resultados-ml-1440.md dentro de resultados-1440
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-1440'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-1440.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print(encabezado_pie)

print("MArco morquecho 1440")