
import re
import spacy
nlp = spacy.load("es_core_news_sm")




def getComplementStatus(oracion):
  # Convertir la oración a minúsculas para hacer la búsqueda insensible a mayúsculas
    oracion = oracion.lower()

    # Palabras clave para activar y desactivar el altavoz y el bluetooth
    activar_altavoz_palabras = {'pon el altavoz', 'activa el altavoz', 'encidente el altavoz', 'ponlo en altavoz', 'ponme en altavoz', 'activame el altavoz', 'enciendeme el altavoz', 'habilitame el altavoz', 'habilita el altavoz'}
    desactivar_altavoz_palabras = {'apaga el altavoz', 'desactiva el altavoz', 'apagame el altavoz', 'desconectame el altavoz', 'deshabilita el altavoz', 'deshabilitame el altavoz', 'quita el altavoz', 'quitame el altavoz', 'deshabilitame el altavoz', 'deshabilita el altavoz'}
    activar_bluetooth_palabras = {'conéctate al bluethooth','conectate al bluethooth', 'activa el bluethooth', 'enciende el bluethooth', 'conéctate al bluethood', 'conectate al bluethood', 'activa el bluethood', 'enciende el bluethood', 'activame el bluethooth', 'activame el bluethood', 'habilita el bluethooth', 'habilita el bluethood', 'habilitame el bluethooth', 'habilitame el bluethood', 'enciendeme el bluethood', 'enciende el bluethooth', 'activa el manos libres', 'enciende el manos libres', 'activame el manos libres', 'enciendeme el manos libres', 'conecta el manos libres', 'conectame el manos libres' }
    desactivar_bluetooth_palabras = {'desconéctate del bluetooth', 'desactiva el bluetooth', 'desconéctate del bluethood', 'desactiva el bluethood', 'desconectate del bluethooth', 'desconectate del bluethood', 'desactivame el bluethood', 'desactivame el bluethooth', 'deshabilitame el bluethooth', 'deshabilitame el bluethood', 'deshabilita el bluethooth', 'deshabilita el bluethood', 'apaga el bluethooth', 'apaga el bluethood', 'apagame el bluethooth', 'apagame el bluethood'}

    # Determinar si se debe activar o desactivar el altavoz o el bluetooth
    activar_altavoz = any(palabra in oracion for palabra in activar_altavoz_palabras)
    desactivar_altavoz = any(palabra in oracion for palabra in desactivar_altavoz_palabras)
    activar_bluetooth = any(palabra in oracion for palabra in activar_bluetooth_palabras)
    desactivar_bluetooth = any(palabra in oracion for palabra in desactivar_bluetooth_palabras)

    # Retornar True si se debe activar, False si se debe desactivar, None si no hay indicación
    altavoz = None
    bluethooth = None

    if activar_altavoz:
        altavoz = True
    elif desactivar_altavoz:
        altavoz = False
    elif activar_bluetooth:
        bluethooth = True
    elif desactivar_bluetooth:
        bluethooth = False
    data = {"altavoz" : altavoz, "bluethooth":bluethooth}
    
    return data

    












