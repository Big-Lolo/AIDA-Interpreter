


def detect_vibration(sentence):
    # Palabras clave que indican la presencia de vibración
    keywords_vibracion = ['vibracion', 'vibrar', 'vibre']

    # Convertir la oración a minúsculas para hacer la comparación sin distinción de mayúsculas
    sentence_lower = sentence.lower()

    # Separar la oración en palabras
    words = sentence_lower.split()

    # Definir la ventana de palabras alrededor de las palabras clave
    window_size = 3  # Tamaño de la ventana

    for i, word in enumerate(words):
        if word in keywords_vibracion:
            # Verificar las palabras en la ventana alrededor de la palabra clave
            for j in range(max(0, i - window_size), min(len(words), i + window_size + 1)):
                if words[j] == 'activa' or words[j] == 'activar' or words[j] == 'activando' or words[j] == 'enciende' or words[j] == 'habilita':
                    return True
                if words[j] == 'desactiva' or words[j] == 'desactivando' or words[j] == 'desactivar' or words[j] == 'quita' or words[j] == 'inutiliza' or words[j] == 'deshazte':
                    return False

    return False

