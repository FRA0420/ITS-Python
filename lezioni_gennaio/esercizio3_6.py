#esercizio 3.6

dinner_list: list = ["giulia", "Leo", "Valerio"]

print(f"Ciao {dinner_list[0]}, {dinner_list[1]}, {dinner_list[2]} ho trovato un tavolo più grande! Vi aggiornerò sui nuovi invitati aggiuntivi.")

dinner_list.insert(0,"Amic")
dinner_list.insert(2,"Rona")
dinner_list.append("Ric")
print(dinner_list)

for amici in dinner_list:
    print(f" Caro {amici}, sei invitato stasera a cena")