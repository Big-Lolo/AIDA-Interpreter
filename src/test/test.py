import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


oraciones = [
    ("Investiga sobre la historia de la Revolución Industrial en el siglo XVIII.", "historia Revolución Industrial siglo XVIII"),
    ("Busca datos sobre el cambio climático y sus efectos en el medio ambiente.","cambio climático efectos medio ambiente"),
    ("Explora la vida y logros de Albert Einstein.","vida logros Albert Einstein"),
    ("Háblame sobre las aplicaciones de inteligencia artificial en la medicina.","aplicaciones inteligencia artificial medicina"),
    ("Investiga sobre la arquitectura moderna y sus principales exponentes.","arquitectura moderna principales exponentes"),
    ("Cuéntame sobre la vida de Leonardo da Vinci.","vida Leonardo da Vinci"),
    ("Habla sobre la influencia de la música en la mente humana.","influencia música mente humana"),
    ("Busca información sobre los beneficios del ejercicio físico.", "beneficios ejercicio físico"),
    ("Explora las teorías de la evolución de Charles Darwin.", "teorías evolución Charles Darwin"),
    ("Investiga sobre los diferentes tipos de energías renovables.", "tipos energías renovables"),
    ("Háblame sobre la Revolución Francesa y sus consecuencias.", "Revolución Francesa consecuencias"),
    ("Busca datos sobre la exploración espacial.", "exploración espacial"),
    ("Investiga sobre los alimentos saludables para el corazón.", "alimentos saludables corazón"),
    ("Háblame sobre la importancia de la conservación del agua.", "importancia conservación agua"),
    ("Explora las teorías de Sigmund Freud sobre el psicoanálisis.", "teorías Sigmund Freud psicoanálisis"),
    ("Investiga sobre las propiedades curativas de las plantas medicinales.", "propiedades curativas plantas medicinales"),
    ("Cuéntame sobre las obras más famosas de William Shakespeare.", "obras famosas William Shakespeare"),
    ("Háblame sobre la teoría de la relatividad de Albert Einstein.", "teoría relatividad Albert Einstein"),
    ("Busca datos sobre la cultura egipcia y sus tradiciones.", "cultura egipcia tradiciones"),
    ("Investiga sobre las principales figuras de la Revolución Rusa.", "principales figuras Revolución Rusa"),
    ("Explora los efectos del cambio climático en la biodiversidad.", "efectos cambio climático biodiversidad"),
    ("Cuéntame sobre la anatomía y funcionamiento del sistema nervioso.", "anatomía funcionamiento sistema nervioso"),
    ("Háblame sobre la historia de la medicina antigua.", "historia medicina antigua"),
    ("Investiga sobre las aplicaciones de la robótica en la industria.", "aplicaciones robótica industria"),
    ("Busca información sobre la teoría del Big Bang y el origen del universo.", "teoría Big Bang origen universo"),
    ("Explora la importancia de la educación en la sociedad.", "importancia educación sociedad"),
    ("Investiga sobre los avances en la tecnología de energía solar.", "avances tecnología energía solar"),
    ("Háblame sobre la cultura japonesa y sus tradiciones.", "cultura japonesa tradiciones"),
    ("Busca datos sobre las especies en peligro de extinción.", "especies peligro extinción"),
    ("Cuéntame sobre la teoría de la evolución de las especies.", "teoría evolución especies"),
    ("Explora las diferentes formas de energía y sus usos.", "formas energía usos"),
    ("Háblame sobre los beneficios de una dieta equilibrada.","beneficios dieta equilibrada"),
    ("Investiga sobre las principales enfermedades del sistema cardiovascular.", "enfermedades sistema cardiovascular"),
    ("Busca datos sobre la historia de la música clásica.", "historia música clásica"),
    ("Cuéntame sobre la importancia de la preservación del medio ambiente.","importancia preservación medio ambiente"),
    ("Háblame sobre las propiedades y beneficios del té verde.", "propiedades beneficios té verde"),
    ("Explora la vida y legado de Mahatma Gandhi.", "vida legado Mahatma Gandhi"),
    ("Investiga sobre las aplicaciones de la inteligencia artificial en la educación.", "aplicaciones inteligencia artificial educación"),
    ("Busca información sobre los descubrimientos de Marie Curie en la radioactividad.", "descubrimientos Marie Curie radioactividad"),
    ("Cuéntame sobre las técnicas de cultivo de alimentos orgánicos.", "técnicas cultivo alimentos orgánicos"),
    ("Háblame sobre la historia de la filosofía antigua.", "historia filosofía antigua"),
    ("Investiga sobre la importancia de la diversidad cultural.", "importancia diversidad cultural"),
    ("Busca datos sobre los avances en la medicina moderna.", "avances medicina moderna"),
    ("Explora la arquitectura de la antigua Roma y sus monumentos.", "arquitectura antigua Roma monumentos"),
]



X_train = oraciones
y_train = consultas_simplificadas


tokenizer_oraciones = Tokenizer()
tokenizer_oraciones.fit_on_texts(X_train)

# Crear y entrenar el tokenizer para consultas
tokenizer_consultas = Tokenizer()
tokenizer_consultas.fit_on_texts(y_train)


def cargar_modelo(filename):
    loaded_model = tf.keras.models.load_model(filename)
    return loaded_model

def probar_modelo(modelo, tokenizer_oraciones, tokenizer_consultas, oracion):
    # Preprocesar la oración de entrada
    sequence = tokenizer_oraciones.texts_to_sequences([oracion])
    padded_sequence = pad_sequences(sequence, maxlen=13, padding='post')

    # Generar la consulta simplificada
    input_seq = np.array(padded_sequence)
    prediction = modelo.predict([input_seq, input_seq])

    # Decodificar la salida para obtener la consulta simplificada
    decoded_output = np.argmax(prediction, axis=-1)
    simplified_query = ' '.join([tokenizer_consultas.index_word[idx] for idx in decoded_output[0] if idx > 0])

    return simplified_query


loaded_model = cargar_modelo('searcher.h5')

# Probar el modelo con una oración
oracion_ejemplo = "Investiga sobre la Revolución Francesa."
consulta_simplificada = probar_modelo(loaded_model, tokenizer_oraciones, tokenizer_consultas, oracion_ejemplo)

print("Oración de entrada:", oracion_ejemplo)
print("Consulta simplificada:", consulta_simplificada)


