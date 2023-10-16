import re
from datetime import datetime
import calendar

##La funcion serviria para detectar si en una oración se menciona algun dia en concreto. Esto serviria para que 
# si se quiere configurar una alarma X dias pues que se configure para X dias








def find_days_in_string(input_string):
    # Lista de nombres de días de la semana en español
    days_of_week = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    
    # Expresión regular para buscar nombres de días de la semana
    pattern = r'\b(?:' + '|'.join(days_of_week) + r')\b'
    
    # Buscar coincidencias con la expresión regular en el string
    matches = re.findall(pattern, input_string, re.IGNORECASE)
    
    # Convertir los nombres de días encontrados a mayúsculas
    # para tener coherencia en el formato
    matches = [day.capitalize() for day in matches]
    
    # Identificar y eliminar casos con "próximo" antes del día de la semana
    modified_matches = []
    prev_word = None
    for day in matches:
        if prev_word and prev_word.lower() == 'próximo' and day.lower() == 'lunes':
            # Si la palabra anterior indica "próximo" y es seguida por "lunes", no incluimos "lunes"
            pass
        else:
            # No es "próximo lunes", lo incluimos
            modified_matches.append(day)
        prev_word = day
    
    return modified_matches


def exect():
    while True:
        vare = input("Introduce periodicidad: ")
        a = find_days_in_string(vare)
        print(a)

if __name__ == '__main__':
    exect()