import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from incorporations.functions_alarm import set_alarm, delete_alarm, disable_alarm
from incorporations.functions_calendar import create_appointment_calendar
from incorporations.functions_calls import realize_call

import asyncio


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model_v4.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag =[0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.68

    # Si la probabilidad máxima está por debajo del umbral, muestra un mensaje sugerido
    if max(res) < ERROR_THRESHOLD:
        return [{'intent': 'Desconocido', 'probability': str(max(res))}]

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []

    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})

    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    if tag == 'Desconocido':
        return "Lo siento, no entiendo lo que quieres decir. ¿Podrías reformular tu pregunta?", None

    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            functions = i.get('function')
            break

    return result, functions


async def wake_Up():
    print("El bot esta funcionando!: ")
    while True:
        message = input('usuario: ')
        ints = predict_class(message)
        res, functions = get_response(ints, intents)
        print(res) #Indicar la respuesta
        if functions:
            print(functions)
            await globals()[functions](message)


if __name__ == '__main__':
    asyncio.run(wake_Up())
