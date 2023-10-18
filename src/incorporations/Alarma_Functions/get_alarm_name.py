import re

def extract_alarm_name(sentence):
    # Dividir la oración en palabras
    palabras = sentence.lower().split()

    # Palabras clave que indican que lo que sigue es parte del nombre
    palabras_clave = ['nombre', 'nombrar', 'nombrada', 'tiene', 'posee']
    
    # Palabras clave que indican el fin del nombre
    palabras_fin_nombre = ['después', 'punto', 'despues', ',', 'coma']

    # Encontrar el índice de la palabra clave
    indice_clave = -1
    for palabra in palabras_clave:
        if palabra in palabras:
            indice_clave = palabras.index(palabra)
            break

    # Extraer el nombre de la alarma
    nombre_alarma = None
    if indice_clave != -1 and indice_clave < len(palabras) - 1:
        # El nombre está después de la palabra clave
        nombre_alarma = []
        i = indice_clave + 1

        while i < len(palabras):
            if palabras[i] in palabras_fin_nombre:
                # Si se encuentra una palabra que indica el fin del nombre, se detiene
                break

            nombre_alarma.append(palabras[i])
            i += 1

        if nombre_alarma:
            # Si la primera palabra es "de", la eliminamos
            if nombre_alarma[0] == 'de':
                nombre_alarma = ' '.join(nombre_alarma[1:])
            else:
                nombre_alarma = ' '.join(nombre_alarma)


            oracion_lower = nombre_alarma.lower()
            indice = len(nombre_alarma)
            for palabra in palabras_fin_nombre:
                palabra_lower = palabra.lower()
                if palabra_lower in oracion_lower:
                    indice_palabra = oracion_lower.find(palabra_lower)
                    indice = min(indice, indice_palabra)

            nombre_alarma = nombre_alarma[:indice].rstrip()
                     


        else:
            nombre_alarma = "No se encontró un nombre de alarma."

    return nombre_alarma


