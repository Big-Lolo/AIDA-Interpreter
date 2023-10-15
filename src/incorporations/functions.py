import spacy
import re
nlp = spacy.load("es_core_news_sm")  ##Interprete de oracion con tal de sacar argumentos de las oraciones




def extract_alarm_information(text):
    doc = nlp(text)
    menos_x_pattern = re.compile(r'(\d+) menos (\d+)')
    en_punto_pattern = re.compile(r'(\d+) en punto')
    patron_con_y = re.compile(r'las (\d+) y (\d+)')
    patron_sin_separacion = re.compile(r'a las (\d+) (\d+)')
    time_pattern = r'(\d+)\s*([yY])\s*media'  # Buscar patrón de "n y media"
    match_en_punto = en_punto_pattern.search(text)
    match_con_y = patron_con_y.search(text)
    match_sin_separacion = patron_sin_separacion.search(text)
    match_time_pattern = re.search(time_pattern, text)


    alarm_info = {
        "hora": [0, 0], #horas, minutos
        "fecha": None,
        "iteratividad": None,
        "vibracion": None,
        "volumen": None
    }
    word_to_minute = {
        'media': 30,
        'cuarto': 15
    }
    if match_en_punto:
        print("b")
        alarm_info["hora"][1] = 0
        alarm_info["hora"][0] = match_en_punto.group(1)
    
    if match_con_y:
        print("a")
        alarm_info["hora"][0] = int(match_con_y.group(1))
        alarm_info["hora"][1] = int(match_con_y.group(2))
    elif match_sin_separacion:
        print("c")
        alarm_info["hora"][0] = int(match_sin_separacion.group(1))
        alarm_info["hora"][1] = int(match_sin_separacion.group(2))

    for token in doc:
        if token.text.lower() in ["mañana", "tarde", "noche"]:
            alarm_info["hora"][0] = int(token.text)
        
        if token.text.lower() in word_to_minute:
            alarm_info["hora"][1] += int(word_to_minute[token.text.lower()])
        if token.text.lower() == 'menos':
            match = menos_x_pattern.search(text)
            if match:
                if alarm_info["hora"][1] == 0:
                    alarm_info["hora"][1] =60 - int(match.group(1))
                    
                else:
                    alarm_info["hora"][1] -= int(match.group(2))
                    
                alarm_info["hora"][0] = (int(match.group(1)) - 1)


    return alarm_info


async def set_alarm(knowledge_base):
    #Creando alarma...
    user_input: str = input(f'{knowledge_base["systemInfo"]["user_name"]} Config Alarma: ')

    infoAlarm =  extract_alarm_information(user_input)
    print(infoAlarm)
    return infoAlarm
    