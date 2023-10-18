import re

def extract_volume_information(sentence):
    def extract_volume_value(text):
        # Expresiones regulares para buscar porcentaje en el texto
        percent_pattern = r'(\d+(\.\d+)?)%'
        
        # Buscar porcentaje en el texto
        percent_matches = re.findall(percent_pattern, text)
        if percent_matches:
            # Si se encuentra un porcentaje, convertirlo a decimal
            percent_value = float(percent_matches[0][0]) / 100.0
            return percent_value
        
        return None  # Si no se encontró porcentaje

    # Palabras clave que indican la referencia al volumen
    keywords_activar = ['volumen', 'pon', 'establece']
    keywords_desactivar = ['no', 'quita']

    # Convertir la oración a minúsculas para hacer la comparación sin distinción de mayúsculas
    sentence_lower = sentence.lower()

    # Separar la oración en palabras
    words = sentence_lower.split()

    # Definir la ventana de palabras alrededor de las palabras clave
    window_size = 5  # Tamaño de la ventana

    for i, word in enumerate(words):
        if word in keywords_activar:
            # Verificar las palabras en la ventana alrededor de la palabra clave
            for j in range(max(0, i - window_size), min(len(words), i + window_size + 1)):
                # Verificar si se menciona un valor numérico de volumen
                if any(char.isdigit() for char in words[j]):
                    volume_value = extract_volume_value(' '.join(words[j - window_size:i + window_size + 1]))
                    if volume_value is not None:
                        return volume_value
                # Verificar si se menciona "mitad", "un cuarto" o "medio"
                if words[j] in ['mitad', 'cuarto', 'medio']:
                    if words[j] == 'cuarto' and j + 1 < len(words) and words[j + 1] == 'de':
                        return 0.25  # Un cuarto
                    elif words[j] == 'tres' and j + 1 < len(words) and words[j + 1] == 'cuartos':
                        return 0.75  # Tres cuartos
                    else:
                        return 0.5  # Mitad

    # Verificar si alguna palabra clave de desactivación está presente
    for keyword in keywords_desactivar:
        if keyword in sentence_lower:
            return 0.0

    # Si no se encontraron palabras clave, por defecto retornar None
    return None

