


async def register_Message():
    send = False
    message = None

    print("Dictame el mensaje.")
    message = input("Mensaje: ")

    if message == "cancelar mensaje" or message == "eliminar mensaje":
        message = None
        send = False
    else:
        send = True


    return message, send