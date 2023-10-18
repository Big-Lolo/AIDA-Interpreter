import spacy
import re
import os
import sys

directorio_actual = os.path.dirname(os.path.abspath(__file__))
carpeta_raiz = os.path.abspath(os.path.join(directorio_actual, '../..'))
sys.path.append(carpeta_raiz)


from incorporations.Alarma_Functions.get_hour import get_hour, find_hours_in_string
from incorporations.Alarma_Functions.get_date import extract_date_info
from incorporations.Alarma_Functions.iterativity import find_days_in_string
from incorporations.Alarma_Functions.get_vibration import detect_vibration
from incorporations.Alarma_Functions.get_volumen import extract_volume_information
from incorporations.Alarma_Functions.get_alarm_name import extract_alarm_name



def extract_alarm_information(text):
    
    alarm_info = {
        "hora": [0, 0],  # horas, minutos
        "fecha": None,
        "iteratividad": None,
        "vibracion": False,
        "volumen": None,
        "name":None
    }
    ##Llamada a funciones de definición (Proximamente ordenar mejor y crear una classe que se llame GetAlarmInfo y que tenga todo tipo de funciones)
    alarm_info["hora"][0], alarm_info["hora"][1]= get_hour(text)
    alarm_info["fecha"] = extract_date_info(text)
    alarm_info["iteratividad"] = find_days_in_string(text)
    alarm_info["vibracion"]= detect_vibration(text)
    alarm_info["volumen"] = extract_volume_information(text)
    alarm_info["name"]= extract_alarm_name(text)

    return alarm_info


async def set_alarm(knowledge_base):  
    #Creando alarma...

    infoAlarm =  extract_alarm_information(knowledge_base)
    print(infoAlarm)
    return infoAlarm


def delete_alarm(sentence):

    objective = extract_delete_alarm_information(sentence)

    return objective

def disable_alarm(sentence):

    objective = extract_delete_alarm_information(sentence)

    return objective


def extract_delete_alarm_information(sent):
    info = {
        "name":None,
        "Fecha":None,
        "Hora":None,
        "Periodo_fecha":None,
        "Periodo_hora":None 
        }

    info["name"]= extract_alarm_name(sent)
    info["Fecha"] = extract_date_info(sent)
    info["Hora"] = get_hour(sent)
    info["Periodo_fecha"] = find_days_in_string(sent)
    info["Periodo_hora"] = find_hours_in_string(sent)

    if info["Periodo_hora"]:
        info["Hora"]:None

    if info["Periodo_fecha"]:
        info["Fecha"]:None

    return info

    

