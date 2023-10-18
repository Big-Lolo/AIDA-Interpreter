from datetime import datetime, timedelta
import re


def extract_date_info(text):
    # Patrones para reconocer fechas
    tomorrow_pattern = re.compile(r'\bmañana\b', re.IGNORECASE)
    day_after_tomorrow_pattern = re.compile(r'\bpasado mañana\b', re.IGNORECASE)
    day_of_month_pattern = re.compile(r'(\d{1,2}) (?:del?|de) (\d{1,2})', re.IGNORECASE)
    week_pattern = re.compile(r'\bdentro de (\d+) (semana|semanas)\b', re.IGNORECASE)
    specific_date_pattern = re.compile(r'\b(\d{1,2}) (?:de) (\w+)\b', re.IGNORECASE)  # Nuevo patrón
    today_pattern = re.compile(r'\bhoy\b', re.IGNORECASE)

    # Lógica para extraer información de la fecha
    if tomorrow_pattern.search(text):
        return datetime.now() + timedelta(days=1)
    elif day_after_tomorrow_pattern.search(text):
        return datetime.now() + timedelta(days=2)
    elif today_pattern.search(text):
        return datetime.now()
    else:
        week_match = week_pattern.search(text)
        if week_match:
            num_weeks = int(week_match.group(1))
            return datetime.now() + timedelta(weeks=num_weeks)
        
        day_of_month_match = day_of_month_pattern.search(text)
        if day_of_month_match:
            day = int(day_of_month_match.group(1))
            month = int(day_of_month_match.group(2))
            now = datetime.now()
            year = now.year
            return datetime(year, month, day)

        specific_date_match = specific_date_pattern.search(text)
        if specific_date_match:
            day = int(specific_date_match.group(1))
            month_name = specific_date_match.group(2).lower()
            month_number = {
                'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
                'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
                'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
            }.get(month_name)
            if month_number:
                now = datetime.now()
                year = now.year
                return datetime(year, month_number, day)
    

