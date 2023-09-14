texto_pdf="""
"""
def dividir_texto(texto, longitud):
    partes = []
    while len(texto) > longitud:
        parte = texto[:longitud]
        partes.append(parte)
        texto = texto[longitud:]
    partes.append(texto)
    return partes

# Ejemplo de uso
longitud_parte = 4096

partes_pdf = dividir_texto(texto_pdf, longitud_parte)

# Imprimir las partes divididas
for i, parte in enumerate(partes_pdf):
    nombre_archivo_salida = f"parte_{i+1}"
    with open(nombre_archivo_salida, "w", encoding='utf-8') as archivo_salida:
        archivo_salida.write(parte)
        print(f"Parte {i+1} guardada en {nombre_archivo_salida}")

