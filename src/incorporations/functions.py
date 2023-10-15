import spacy
import re
from incorporations.Alarma_Functions.get_hour import get_hour
from incorporations.Alarma_Functions.get_date import extract_date_info






def extract_alarm_information(text):
    
    alarm_info = {
        "hora": [0, 0],  # horas, minutos
        "fecha": None,
        "iteratividad": None,
        "vibracion": None,
        "volumen": None
    }
    ##Llamada a funciones de definición (Proximamente ordenar mejor y crear una classe que se llame GetAlarmInfo y que tenga todo tipo de funciones)
    alarm_info["hora"][0], alarm_info["hora"][1]= get_hour(text)
    alarm_info["fecha"]= extract_date_info(text)

    return alarm_info


async def set_alarm(knowledge_base):
    #Creando alarma...
    user_input: str = input(f'{knowledge_base["systemInfo"]["user_name"]} Config Alarma: ')

    infoAlarm =  extract_alarm_information(user_input)
    print(infoAlarm)
    return infoAlarm
    