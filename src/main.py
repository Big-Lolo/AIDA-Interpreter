import torch 
from transformers import BertTokenizer, BertModel, GPT2Tokenizer, GPT2LMHeadModel, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
import pandas as pd
import random
import nltk


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Cargar el archivo CSV en un DataFrame
data = pd.read_csv('datas.csv', sep=';')

# Obtener las instrucciones, respuestas y acciones
instrucciones = data['instruccion'].tolist()
respuestas = data['respuesta'].tolist()
acciones = data['accion'].tolist()
num_classes = len(set(acciones))  # Cantidad de clases únicas




# Cargar el tokenizador y el modelo preentrenado de BERT
bert_tokenizer = BertTokenizer.from_pretrained('mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es')
bert_model = BertForSequenceClassification.from_pretrained('mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es', num_labels=num_classes)  # Ajusta num_labels según el número de clases en tu problema
# Optimizador y tasa de aprendizaje para BERT
optimizer = AdamW(bert_model.parameters(), lr=1e-5)  # Ajusta la tasa de aprendizaje según sea necesario



def encode_instruction (instruction): 
    # Tokenizar la instrucción con el tokenizador de 
    input_ids = bert_tokenizer.encode(instruction, return_tensors='pt') 
    # Obtener el vector de características de la instrucción con el modelo de BERT 
    output = bert_model(input_ids) 
    # Devolver el último estado oculto del modelo de BERT 
    return output.last_hidden_state


def generate_response(feature_vector): 
    # Generar una secuencia de tokens a partir del vector de características con el modelo de GPT-2 
    output = gpt2_model.generate (feature_vector, max_length=50) 
    # Decodificar la secuencia de tokens con el tokenizador de GPT-2 
    response = gpt2_tokenizer.decode(output[0]) # Devolver el texto de respuesta generado 
    return response 

def classify_response(response): 
    # Tokenizar el texto de respuesta con el tokenizador de BERT 
    input_ids = bert_tokenizer.encode(response, return_tensors='pt') 
    # Obtener la salida del clasificador del modelo de BERT
    output = bert_model(input_ids) 
    # Aplicar una función softmax para obtener las probabilidades de cada clase 
    probabilities = torch.nn.functional.softmax(output.logits, dim=-1)
    # Obtener la clase con mayor probabilidad 
    action = torch.argmax(probabilities) 
    # Devolver la acción seleccionada 
    return action 


def process_instruction(instruction): 
    # Codificar la instrucción con BERT 
    feature_vector = encode_instruction (instruction) 
    # Generar el texto de respuesta con GPT-2 
    response = generate_response(feature_vector) 
    # Clasificar el texto de respuesta con BERT 
    action = classify_response(response) 
    # Devolver la respuesta y la acción al usuario 
    return response, action 


# Tokenizar las instrucciones y respuestas BERT
tokenized_inputs = bert_tokenizer(instrucciones, return_tensors='pt', padding=True, truncation=True)
tokenized_responsess = bert_tokenizer(respuestas, return_tensors='pt', padding=True, truncation=True)

# Convertir las acciones en etiquetas numéricas BERT
labels = [int(action) for action in acciones]  # Asumiendo que las acciones son etiquetas numéricas
tokenized_inputs_tensor = torch.tensor(tokenized_inputs.input_ids)
labels_tensor = torch.tensor(labels)
# Dividir los datos en conjuntos de entrenamiento y validación
train_inputs, val_inputs, train_labels, val_labels = train_test_split(tokenized_inputs_tensor, labels_tensor, test_size=0.1, random_state=42)

# Crear datasets de PyTorch BERT
train_dataset = torch.utils.data.TensorDataset(train_inputs, train_labels)
val_dataset = torch.utils.data.TensorDataset(val_inputs, val_labels)

# Crear dataloaders BERT
train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=92, shuffle=True)
val_dataloader = torch.utils.data.DataLoader(val_dataset, batch_size=92)

# Definir la función de pérdida y el optimizador BERT
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = AdamW(bert_model.parameters(), lr=1e-5)

# Entrenar BERT
num_epochs = 20  # Ajusta el número de épocas según sea necesario 
for epoch in range(num_epochs):
    bert_model.train()
    total_loss = 0
    
    for batch in train_dataloader:
        inputs, labels = batch
        outputs = bert_model(inputs, labels=labels)
        loss = outputs.loss
        total_loss += loss.item()
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    average_train_loss = total_loss / len(train_dataloader)
    print(f"Epoch {epoch+1}/{num_epochs}, Train Loss: {average_train_loss:.4f}")

# Evaluar en el conjunto de validación BERT
bert_model.eval()
val_loss = 0
correct = 0
total = 0

with torch.no_grad():
    for batch in val_dataloader:
        inputs, labels = batch
        outputs = bert_model(inputs, labels=labels)
        loss = outputs.loss
        val_loss += loss.item()
        
        _, predicted = torch.max(outputs.logits, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Validation Loss: {val_loss / len(val_dataloader):.4f}")
print(f"Validation Accuracy: {100 * correct / total:.2f}%")


# - - - - -  - --  - -- - - - - - -GPT2- - - - - - - - - - - - - -#
# Cargar el tokenizador y el modelo preentrenado de GPT-2
gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
gpt2_model = GPT2LMHeadModel.from_pretrained('gpt2')
gpt2_model.to(device)
# Optimizador y tasa de aprendizaje para GPT-2
optimizer_gpt2 = AdamW(gpt2_model.parameters(), lr=1e-5)  # Ajusta la tasa de aprendizaje según sea necesario
# Tokenizar instrucciones y respuestas GPT2
max_length = 50
gpt2_tokenizer.pad_token = gpt2_tokenizer.eos_token
tokenized_instructions = gpt2_tokenizer(instrucciones, return_tensors='pt', padding='max_length', truncation=True,  max_length=max_length)
tokenized_responses = gpt2_tokenizer(respuestas, return_tensors='pt', padding='max_length', truncation=True,  max_length=max_length)

# Crear datasets de PyTorch GPT2
gpt2_train_dataset = torch.utils.data.TensorDataset(tokenized_instructions.input_ids, tokenized_responses.input_ids)

# Crear dataloaders GPT2
gpt2_train_dataloader = torch.utils.data.DataLoader(gpt2_train_dataset, batch_size=92, shuffle=True)


print("Tamaño del lote de instrucciones:", tokenized_instructions.input_ids.size(0))
print("Tamaño del lote de respuestas:", tokenized_responses.input_ids.size(0))
for batch in gpt2_train_dataloader:
    inputs, labels = batch
    print("Tamaño del lote (inputs):", inputs.size(0))  # Tamaño del lote de las entradas
    print("Tamaño del lote (labels):", labels.size(0))  # Tamaño del lote de las etiquetas

# Definir la función de pérdida y el optimizador GPT2
loss_fn_gpt2 = torch.nn.CrossEntropyLoss()
optimizer_gpt2 = AdamW(gpt2_model.parameters(), lr=1e-5)

# Entrenar GPT-2
num_epochs_gpt2 = 20  # Ajusta el número de épocas según sea necesario GPT2
print("Número de muestras en el conjunto de datos:", len(gpt2_train_dataset))

for epoch in range(num_epochs_gpt2):
    gpt2_model.train()
    total_loss_gpt2 = 0
    
    for batch in gpt2_train_dataloader:
        instructions, responses = batch
        print("Tamaño del lote (inputs):", instructions.size(0))  # Imprime el tamaño de las instrucciones
        print("Tamaño del lote (labels):", responses.size(0))  # Imprime el tamaño de las respuestas  
        print("Forma de las instrucciones:", instructions.shape)
        print("Forma de las respuestas:", responses.shape)      
        outputs = gpt2_model(input_ids=instructions, labels=responses)
        loss_gpt2 = outputs.loss
        total_loss_gpt2 += loss_gpt2.item()
        
        optimizer_gpt2.zero_grad()
        loss_gpt2.backward()
        optimizer_gpt2.step()
    
    average_train_loss_gpt2 = total_loss_gpt2 / len(gpt2_train_dataloader)
    print(f"Epoch {epoch+1}/{num_epochs_gpt2}, Train Loss: {average_train_loss_gpt2:.4f}")



# Evaluar en el conjunto de validación y generar respuestas
gpt2_model.eval()
val_loss_gpt2 = 0



with torch.no_grad():
    for batch in gpt2_train_dataloader:  # Utilizamos el mismo dataloader para la evaluación
        instructions, responses = batch
        outputs = gpt2_model(input_ids=instructions, labels=responses)
        loss_gpt2 = outputs.loss
        val_loss_gpt2 += loss_gpt2.item()

    average_val_loss_gpt2 = val_loss_gpt2 / len(gpt2_train_dataloader)
    print(f"Validation Loss: {average_val_loss_gpt2:.4f}")

# Generar respuestas basadas en instrucciones
def generate_gpt2_response(instruction, attention_mask, max_length=50):
    input_ids = gpt2_tokenizer.encode(instruction, return_tensors='pt')
    max_response_length = min(max_length, gpt2_model.config.max_position_embeddings)
    output = gpt2_model.generate(input_ids, attention_mask=attention_mask, max_length=max_response_length)
    response = gpt2_tokenizer.decode(output[0])
    return response

# Ejemplo de generación de respuesta para una instrucción específica
example_instruction = "Dime cómo llegar a la estación de tren."
input_ids = gpt2_tokenizer.encode(example_instruction, return_tensors='pt')
attention_mask = (input_ids != 0).float()
generated_response = generate_gpt2_response(example_instruction, attention_mask)
print("Ejemplo de respuesta generada:")
print(generated_response)

# Medir calidad de las respuestas generadas
def evaluate_response_quality(instructions, num_samples=10):
    total_bleu_score = 0
    for instruction in instructions:
        reference = respuestas[instrucciones.index(instruction)]
        input_ids = gpt2_tokenizer.encode(instruction, return_tensors='pt')
        attention_mask = (input_ids != 0).float()
        generated_responses = [generate_gpt2_response(instruction, attention_mask ) for _ in range(num_samples)]
        bleu_score = nltk.translate.bleu_score.sentence_bleu([reference.split()], generated_responses)
        total_bleu_score += bleu_score

    average_bleu_score = total_bleu_score / len(instructions)
    return average_bleu_score

# Ejemplo de evaluación de calidad de respuestas generadas
sample_instructions = ["¿Qué hiciste hoy?", "Despiértame a las 6:30 AM para hacer ejercicio"]  # Lista de instrucciones
avg_bleu_score = evaluate_response_quality(sample_instructions)
print("Promedio de puntuación BLEU para respuestas generadas:", avg_bleu_score)

while True:
    new_instruction = input("Ingresa una nueva instrucción: ")
    input_ids = gpt2_tokenizer.encode(new_instruction, return_tensors='pt')
    attention_mask = (input_ids != 0).float()
    new_generated_response = generate_gpt2_response(new_instruction, attention_mask)
    predicted_action = classify_response(new_generated_response)
    print("Respuesta generada:", new_generated_response)
    print("Acción predicha:", predicted_action)