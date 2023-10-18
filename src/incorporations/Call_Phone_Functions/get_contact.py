import spacy
import re

import os
import sys

directorio_actual = os.path.dirname(os.path.abspath(__file__))
carpeta_raiz = os.path.abspath(os.path.join(directorio_actual, '../..'))
sys.path.append(carpeta_raiz)


from incorporations.Alarma_Functions.others.string2num import get_number_from_sentence


def getNameContact(sentence):
    contact_list = ["juan", "manuel", "mama", "papa", "amigo palillos"]
    # Convertir la oración a minúsculas para hacer la búsqueda insensible a mayúsculas
    sentence_lower = sentence.lower()

    # Lista para almacenar los nombres encontrados

    for name in contact_list:
        name_lower = name.lower()
        
        if name_lower in sentence_lower:
            return name

    
    return None

def getPhoneNumber2Call(senten):
    sentence = get_number_from_sentence(senten)
    sentence = sentence.replace(' ', '')
    
   # Definir el patrón de expresión regular para buscar números de teléfono
    pattern = r"\d{9,}"
    # Buscar los números de teléfono en la oración utilizando el patrón
    matches = re.findall(pattern, sentence)

    # Limpiar los números encontrados eliminando separadores
    clean_matches = [re.sub(r"[ \-,]", "", match) for match in matches]

    # Filtrar solo los números que tienen 9 dígitos
    valid_numbers = [match for match in clean_matches if len(match) == 9]
    

    return valid_numbers if valid_numbers else None
