from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
import pandas as pd
import torch

from ...src.main import tokenizer, model


##Funciones

def generar_respuesta(instruccion):
    # Tokenizar la instrucción
    inputs = tokenizer(instruccion, return_tensors="pt")

    # Obtener la salida del modelo
    outputs = model(**inputs)
    
    # Aquí puedes procesar la salida según tu necesidad
    # En este ejemplo, simplemente decodificamos la salida
    respuesta = tokenizer.decode(outputs.logits.argmax(), skip_special_tokens=True)
    
    return respuesta