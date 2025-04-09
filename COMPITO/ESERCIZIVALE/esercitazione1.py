# def find_element(list:list[int],element:int) -> bool:
#     for item in list:
#         if item == element:
#             return True
#     return False
        
# print(find_element([1,2,3],4))

# def number_magic(n:int):
#     b = str(n)
#     b = [int(n) for n in b]
#     print(b)
#     for element in b:
#         if element == 7:
#             return True
        
#     return False
    
# print(number_magic(1237))
        

# Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
# La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione 
# e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire '
# 'il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

# print(rotate_left([1, 2, 3, 4, 5], 2))
# [3, 4, 5, 1, 2]

# def rotate_left(elements: list, k: int) -> list:
#     lunghezza = len(elements)
#     if lunghezza == 0:
#          return []
#     #k = k % lunghezza
#     nuova_lista=elements[k:]+elements[0:k]
#     return nuova_lista

# print(rotate_left([1, 2, 3, 4, 5], 2))

	



# def frequency_dict(elements: list) -> dict:
#     myDict:dict[str]={}
#     for item in elements:
#         if item in myDict:
#             myDict[item]+=1
#         else:
#             myDict[item]=1
#     return myDict
# print(frequency_dict(["mela","mela","arancia"]))

# Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
# ritorni un nuovo insieme senza i numeri specificati nella lista.
# print(remove_elements({5, 6, 7}, [7, 8, 9]))
# {5, 6}

# def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
#     if original_set == ():
#         return original_set
#     if elements_to_remove == []:
#         return original_set
#     copia_set= original_set
#     for element in elements_to_remove:
#         if element in copia_set:
#             copia_set.remove(element)
#     return copia_set
    
        
# print(remove_elements({1,2,3,4},[1,4,5]))

# def check_parentheses(expression: str) -> bool:

#     count1 = 0
#     for par in expression:
#         if par == "(":
#             count1+=1
#         if par == ")":
#             count1-=1
#     if count1 == 0:
#         return True
#     if count1 < 0:
#         return False
    
# print(check_parentheses("()(()))"))

# Scrivi una funzione che unisce due dizionari. 
# Se una chiave è presente in entrambi, somma i loro valori.

# def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
#     dict3 = dict1.copy()
#     for k2,v2 in dict2.items():
#         if k2 in dict3:
#             dict3[k2]+=v2
#         else:
#             dict3[k2]= v2
#     return dict3

# print(merge_dictionaries({'x': 5}, {'x': -5}))

# Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
# Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(myList:list[int]) -> int:
    
    count= 0

    for element in range(len(myList)):
        # if element == 0 and element != myList[element-1]:
        #     count += 1
        # if element == myList[element-1] and element != myList[element-2]:
        #     count+=1
        
        if (element == 0 or myList[element] != myList[element-1]) and (element == len(myList) -1 or myList[element] != myList[element+1]):
            count += 1  

    return count
print(count_isolated([1, 2, 3, 4, 5]))

        

#if element == 0 and element == len[myList+1]:
        #     count = 0
        # if element ==  and element == len[myList-1]:
        #     count=0
        # else:
        #     if element != len[myList-1] and element != len[myList+1]:
        #         count += 1



        






        

            

    

        
        
