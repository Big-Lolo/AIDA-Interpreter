from datetime import datetime, timedelta
import re


def extract_date_info(text):
    # Patrones para reconocer fechas
    tomorrow_pattern = re.compile(r'\bmañana\b', re.IGNORECASE)
    day_after_tomorrow_pattern = re.compile(r'\bpasado mañana\b', re.IGNORECASE)
    day_of_month_pattern = re.compile(r'(\d{1,2}) (?:del?|de) (\d{1,2})', re.IGNORECASE)
    week_pattern = re.compile(r'\bdentro de (\d+) (semana|semanas)\b', re.IGNORECASE)
    # ... otros patrones

    # Lógica para extraer información de la fecha
    if tomorrow_pattern.search(text):
        return datetime.now() + timedelta(days=1)
    elif day_after_tomorrow_pattern.search(text):
        return datetime.now() + timedelta(days=2)
    else:
        # Intentar reconocer el número de semanas
        week_match = week_pattern.search(text)
        if week_match:
            num_weeks = int(week_match.group(1))
            return datetime.now() + timedelta(weeks=num_weeks)
        
        day_of_month_match = day_of_month_pattern.search(text)
        if day_of_month_match:
            day = int(day_of_month_match.group(1))
            month = int(day_of_month_match.group(2))
            # Asumiendo año actual, podrías agregar lógica para reconocer el año si es proporcionado en el texto
            now = datetime.now()
            year = now.year
            return datetime(year, month, day)
    
    # ... otras condiciones

    return None

