#esercizio 3.7

dinner_list: list = ["giulia", "Leo", "Valerio", "Leo", "Chiara"]

print(f"sorry {dinner_list[4]}, cena annullata")
dinner_list.pop()

print(dinner_list)
print(f"sorry {dinner_list[3]}, cena annullata")

dinner_list.pop()

print(dinner_list)
print(f"sorry {dinner_list[2]}, cena annullata")
dinner_list.pop()

print(dinner_list)
print(f"sorry {dinner_list[1]}, cena annullata")
dinner_list.pop()
print(dinner_list)

for amici in dinner_list:
    print(f"{amici} cena confermata")

del dinner_list
print(dinner_list)