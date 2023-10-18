import os
import sys
import asyncio

directorio_actual = os.path.dirname(os.path.abspath(__file__))
carpeta_raiz = os.path.abspath(os.path.join(directorio_actual, '../..'))
sys.path.append(carpeta_raiz)


from incorporations.Call_Phone_Functions.get_contact import getNameContact, getPhoneNumber2Call
from incorporations.Call_Phone_Functions.call_complements import getComplementStatus



async def realize_call(sentence):
    
    val = await getCallInfo(sentence)

    print(val)

    return val


async def getCallInfo(oracion):

    information = {
        "Nombre":None,
        "Phone_Number":None,
        "Bluethood":None,
        "Altavoz":None 
    }
    information["Nombre"] = getNameContact(oracion)
    information["Phone_Number"] = getPhoneNumber2Call(oracion)
    a = getComplementStatus(oracion)
    information["Altavoz"] = a["altavoz"]
    information["Bluethood"] = a["bluethooth"]


    return information