import pandas as pd

import spacy
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data = pd.read_csv('datas.csv')  
nlp = spacy.load('es_core_news_sm')  
data['instruccion'] = data['instruccion'].apply(lambda text: ' '.join([token.lemma_ for token in nlp(text.lower())]))

X_train, X_test, y_train, y_test = train_test_split(data['instruccion'], data['accion'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

#modelo

model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

predictions = model.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, predictions)

print('Precisión del modelo:', accuracy)



for i in range(len(X_test)):
    if predictions[i] != y_test.iloc[i]:
        print("Instrucción:", X_test.iloc[i])
        print("Predicción:", predictions[i])
        print("Etiqueta verdadera:", y_test.iloc[i])
        print("-----")