import re
from datetime import datetime
import calendar

##La funcion serviria para detectar si en una oración se menciona algun dia en concreto. Esto serviria para que 
# si se quiere configurar una alarma X dias pues que se configure para X dias








def find_days_in_string(input_string):
    # Lista de nombres de días de la semana en español
    days_of_week = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    
    # Expresión regular para buscar nombres de días de la semana
    day_pattern = r'\b(?:' + '|'.join(days_of_week) + r')\b'
    
    # Buscar coincidencias con la expresión regular en el string
    day_matches = re.findall(day_pattern, input_string, re.IGNORECASE)
    
    # Convertir los nombres de días encontrados a mayúsculas
    # para tener coherencia en el formato
    day_matches = [day.capitalize() for day in day_matches]
    
    # Expresión regular para buscar rangos de días de la semana y "fin de semana"
    range_pattern = r'\b(de|desde|toda\s*la\s*semana|fin\s*de\s*semana)\s+(?:el\s+)?(\w+)\s*(?:hasta|a)?\s*(?:el\s+)?(\w+)\b'
    
    # Buscar coincidencias con la expresión regular en el string
    range_matches = re.findall(range_pattern, input_string, re.IGNORECASE)
    
    # Manejar los rangos de días y "fin de semana"
    modified_matches = []
    for match in range_matches:
        if match[0] and match[0].lower() in ['de', 'desde', 'toda la semana']:
            # Si se especifica un rango o toda la semana
            start_day = match[1].capitalize()
            end_day = match[2].capitalize() if match[2] else match[1].capitalize()
            
            try:
                start_idx = days_of_week.index(start_day.lower())
                end_idx = days_of_week.index(end_day.lower())
                # Agregar los días del rango al resultado
                modified_matches.extend(days_of_week[start_idx:end_idx + 1])
            except ValueError:
                # Si la palabra no es un día de la semana válido, ignorarla
                pass
        elif match[0] and match[0].lower() == 'fin de semana':
            # Si se especifica "fin de semana"
            modified_matches.extend(['Sábado', 'Domingo'])
    
    # Agregar los días individuales encontrados
    modified_matches.extend(day_matches)
    
    return modified_matches


