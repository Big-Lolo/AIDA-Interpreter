import spacy
import re
from dateutil import parser

nlp = spacy.load("es_core_news_sm")  ##Interprete de oracion con tal de sacar argumentos de las oraciones



def get_hour(text):
    doc = nlp(text)
    hour = None
    minutes = None

    word_to_minute = {
        'media': 30,
        'cuarto': 15,
        'menos': -1,  # Placeholder para detectar "menos"
        'en': -2  # Placeholder para detectar "en punto"
    }

    # Variables para controlar si es "de la tarde" o "de la noche"
    is_tarde = False
    is_noche = False

    for i, token in enumerate(doc):
        if token.text.lower() in ["mañana", "tarde", "noche"]:
            # Verificar si "mañana", "tarde" o "noche" están precedidas por "de la"
            if i > 0 and i < len(doc) - 1 and doc[i - 1].text.lower() == "de" and doc[i + 1].text.lower() == "la":
                # La palabra está precedida por "de la", se interpreta como estado del día
                if token.text.lower() == "mañana":
                    hour = 6  # Hora de la mañana (ejemplo)
                elif token.text.lower() == "tarde":
                    print("is true weon")
                    is_tarde = True
                elif token.text.lower() == "noche":
                    is_noche = True

        if token.text.isdigit():
            # Si encontramos un dígito, considerémoslo como parte de la hora
            if hour is None:
                hour = int(token.text)
            else:
                minutes = int(token.text)
        elif token.text.lower() in word_to_minute:
            value = word_to_minute[token.text.lower()]
            if value == -1 and minutes is not None:  # Restar minutos
                minutes -= value
                if minutes < 0:
                    hour -= 1
                    minutes = 60 + minutes
            elif value == -2:  # Si es "en punto", los minutos son 0
                minutes = 0
            elif minutes is not None:
                minutes += value

    # Si es "de la tarde" o "de la noche", sumar 12 horas
    if is_tarde and hour is not None:
        hour += 12
    elif is_noche and hour is not None:
        hour += 12

    # Establecer minutos en 0 si no se han proporcionado minutos
    if minutes is None:
        minutes = 0

    return hour, minutes