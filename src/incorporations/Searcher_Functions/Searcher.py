import spacy

# Cargar el modelo de spaCy
nlp = spacy.load("es_core_news_sm")

# Oración de ejemplo
def simply_searcher(oracion):
    # Analizar la oración
    doc = nlp(oracion)

    # Extraer sustantivos y verbos clave
    sustantivos_verbos_clave = [token.text for token in doc if token.pos_ in ("NOUN", "ADJ")]

    # Construir la oración simplificada
    oracion_simplificada = " ".join(sustantivos_verbos_clave)

    return oracion_simplificada
