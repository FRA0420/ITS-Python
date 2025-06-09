#importiamo la lista che contiene le lettere minuscole dell'alfabeto
from string import ascii_lowercase

def caesar_cypher_encrypt(s:str,key:int)->str:

    lista=list(ascii_lowercase)
    print(len(lista))
    frase=""
    for carattere in s:
        i = lista.index(carattere)
        i += key 
        i %= len(lista)
        frase+=lista[i]

    return frase

def caesar_cypher_decrypt(s:str,key:int)->str:
    lista=list(ascii_lowercase)
    print(len(lista))
    frase=""
    for carattere in s:
        i = lista.index(carattere)
        i -= key
        i %= len(lista)
        frase+=lista[i]
    return frase

a=caesar_cypher_encrypt("ciao",2)
print(a)
b=caesar_cypher_encrypt("ciao",200)
print(b)

c=caesar_cypher_decrypt("uasg",200)
print(c)










