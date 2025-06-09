import string

def count_unique_words(text):
    # Suddividi il testo sugli spazi bianchi
    tokens = text.split()
    
    # Dizionario per il conteggio delle parole
    word_count = {}
    
    for token in tokens:
        # Converti in minuscolo
        token = token.lower()
        # Rimuovi punteggiatura iniziale e finale
        token = token.strip(string.punctuation)
        # Ignora i token vuoti
        if token:
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1
    
    return word_count

# Esempio di utilizzo
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
print(output)
