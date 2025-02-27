current_users:list[str]=["Yzma", "Kronk", "Ade", "Zeus", "Bilbo"]
new_users:list[str]= ["Steered", "Kronk", "Yzma", "Kirito", "Clorella"]
copia_l1=[]

for n in current_users:
    copia_l1.append(n.lower())
print(copia_l1)
    
for n in new_users:
    if n in current_users and copia_l1:
        print(f"{n} username usato")
    else:
        #current_users.append(n)
        print(f"L'username {n} è disponibile")