import spacy
from incorporations.Alarma_Functions.others.string2num import get_number_from_sentence



nlp = spacy.load("es_core_news_sm")  ##Interprete de oracion con tal de sacar argumentos de las oraciones



def get_hour(input_text):
    text = get_number_from_sentence(input_text)
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(text)

    hour = None
    minutes = None

    word_to_minute = {
        'media': 30,
        'cuarto': 15,
        'menos': -1,
        'en': -2
    }

    is_tarde = False
    is_noche = False

    for i, token in enumerate(doc):
        if token.text.lower() in ["mañana", "tarde", "noche"]:
            if i > 0 and doc[i - 2].text.lower() == "de" and doc[i - 1].text.lower() == "la":
                if token.text.lower() == "tarde":
                    is_tarde = True
                elif token.text.lower() == "noche":
                    is_noche = True

        if token.text.isdigit():
            if hour is None:
                hour = int(token.text)
            else:
                if doc[i - 1].text.lower() == "menos":
                   hour = hour - 1
                   minutes = 60 - int(token.text)
                else:
                    minutes = int(token.text)
        elif token.text.lower() in word_to_minute:
            value = word_to_minute[token.text.lower()]

            if token.text.lower() == "cuarto" and doc[i - 1].text.lower() == "menos":
                hour = hour - 1
                minutes = 60 - 15

            if value == -1 and minutes is not None:
                minutes -= value
                if minutes < 0:
                    hour -= 1
                    minutes = 60 + minutes
            elif value == -2:
                minutes = 0
            elif minutes == None:
                minutes = value

    if is_tarde and hour is not None and hour < 12:
        hour += 12
    elif is_noche and hour is not None:
        hour += 12

    
    if minutes is None:
        minutes = 0

    return (hour, minutes)







