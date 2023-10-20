from incorporations.Whatsapp_Functions.message_functions import register_Message
from incorporations.Call_Phone_Functions.get_contact import getNameContact


async def create_whatsapp_message(sentence):

#Primer obtener contacto de la oracion, despues localizar al usuario y cuando le encuentre decir "Dime que quieres que le escriba". Si no le encuentra, devolver feedback

    contact = getNameContact(sentence)
    if contact:
        existence = await existence_chat_contact(contact) #callback de android con un filter list
    else:
        print("No he podido encontrar al contacto, intentalo nuevamente")
        return

    if existence:
        message, send = await register_Message()
        if send:
            "funcion para enviar en mensaje(message)"
    else:
        print("No he podido encontrar al contacto, intentalo nuevamente")

    return


def crear_audio_whatsapp(sentence):

#Primero localizar el contacto y despues preguntar tiempo de grabacion de audio. Si no le encuentra devolver feedback.


    return