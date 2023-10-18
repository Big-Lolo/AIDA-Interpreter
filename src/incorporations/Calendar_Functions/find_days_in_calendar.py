import os
import sys
import datetime

directorio_actual = os.path.dirname(os.path.abspath(__file__))
carpeta_raiz = os.path.abspath(os.path.join(directorio_actual, '../..'))
sys.path.append(carpeta_raiz)
from incorporations.Alarma_Functions.others.string2num import get_number_from_sentence
from incorporations.Alarma_Functions.get_date import extract_date_info




def find_dates_day_in_string(text):
    # Buscar la palabra "hasta" o "a" y dividir la oración en dos partes
    partes = None
    texto = text.lower()  # Convertir a minúsculas para hacer coincidencias sin importar mayúsculas o minúsculas

    if ' hasta ' in texto:
        partes = texto.split(' hasta ')
    elif ' a ' in texto:
        partes = texto.split(' a ')
   
    if partes:
        if len(partes) != 2:
            return (None, None)
        else:
            rango_minimo_dias = extract_date_info(partes[0])
            rango_maximo_dias = extract_date_info(partes[1])
    else:
        # Comprobar si menciona "toda la semana" o "la semana entera"
        if 'toda la semana' in texto or 'la semana entera' in texto:
            # Obtener el primer y último día de la semana actual
            hoy = datetime.date.today()
            primer_dia_semana = hoy - datetime.timedelta(days=hoy.weekday())
            ultimo_dia_semana = primer_dia_semana + datetime.timedelta(days=6)
            
            rango_minimo_dias = primer_dia_semana
            rango_maximo_dias = ultimo_dia_semana
        else:
            rango_minimo_dias = extract_date_info(texto)
            rango_maximo_dias = rango_minimo_dias

    if rango_minimo_dias is None or rango_maximo_dias is None:
        return None, None

    return rango_minimo_dias, rango_maximo_dias