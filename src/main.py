import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from incorporations.clases import MyDataset
##Sufrom incorporations.functions import generar_respuesta



    



# Cargar el conjunto de datos
data = pd.read_csv('datas.csv')

# Cargar un tokenizador y un modelo pre-entrenado de BERT para español
tokenizer = BertTokenizer.from_pretrained('dccuchile/bert-base-spanish-wwm-uncased')
model = BertForSequenceClassification.from_pretrained('dccuchile/bert-base-spanish-wwm-uncased', num_labels=len(data['accion'].unique()))

# Preparar los datos para el modelo
train_encodings = tokenizer(list(data['instruccion']), truncation=True, padding=True)
train_labels = torch.tensor([list(data['accion']).index(label) for label in data['accion']])

# Definir los argumentos para el entrenamiento
training_args = TrainingArguments(
    output_dir='./output',
    per_device_train_batch_size=30,
    num_train_epochs=3,
    logging_dir='./logs',
)

# Entrenar el modelo
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=MyDataset(train_encodings, train_labels),
)

trainer.train()

# Ahora puedes utilizar el modelo entrenado para hacer predicciones
# ...


def generar_respuesta(instruccion):
    # Tokenizar la instrucción
    inputs = tokenizer(instruccion, return_tensors="pt")

    # Obtener la salida del modelo
    outputs = model(**inputs)
    
    # Aquí obtenemos el índice de la acción predicha
    predicted_action_idx = outputs.logits.argmax().item()
    
    # Obtener la acción correspondiente al índice
    predicted_action = data['accion'].iloc[predicted_action_idx]
    
    return predicted_action


instruccion_usuario = input("Ingresa una instrucción: ")

# Generar la respuesta
respuesta_generada = generar_respuesta(instruccion_usuario)
print("Instrucción:", instruccion_usuario)
print("Respuesta generada:", respuesta_generada)