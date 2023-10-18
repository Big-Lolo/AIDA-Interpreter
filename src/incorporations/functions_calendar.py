import os
import sys

directorio_actual = os.path.dirname(os.path.abspath(__file__))
carpeta_raiz = os.path.abspath(os.path.join(directorio_actual, '../..'))
sys.path.append(carpeta_raiz)


from incorporations.Alarma_Functions.get_hour import get_hour, find_hours_in_string
from incorporations.Alarma_Functions.get_date import extract_date_info
from incorporations.Alarma_Functions.iterativity import find_days_in_string
from incorporations.Alarma_Functions.get_alarm_name import extract_alarm_name
from incorporations.Calendar_Functions.find_days_in_calendar import find_dates_day_in_string
import asyncio




async def get_calendar_data_info(text):

    info = {
    "name":None,
    "Periodo_dias": None,
    "Periodo_fechas":None,
    "Periodo_hora":None 
    }

    info["name"]= extract_alarm_name(text)
    info["Periodo_dias"] = find_days_in_string(text)   ## Esto seria si se dijera, des del lunes hasta el miercoles, o solo el fin de semana...
    info["Periodo_fechas"] = find_dates_day_in_string(text)  ##Esto seria si se dijera, des del dia 23 de enero hasta el dia 25 
    info["Periodo_hora"] = find_hours_in_string(text)

    if info["Periodo_fechas"][0]:
        if not info["Periodo_fechas"][1]:
            info["Periodo_fechas"][1] = info["Periodo_fechas"][0]



    return info



async def create_appointment_calendar(sentence):
    result = await get_calendar_data_info(sentence)
    print(result)
    return result


async def delete_appointment_calendar(sentence):
    result = await get_calendar_data_info(sentence)
    print(result)
    return result


async def get_appointment_calendar(sentence):
    result = await get_calendar_data_info(sentence)
    print(result)
    return result






async def main():
    while True:
        texte = input("Introduce algo: ")
        result = await get_calendar_data_info(texte)
        print(result)
    

if __name__ == '__main__':
    asyncio.run(main())