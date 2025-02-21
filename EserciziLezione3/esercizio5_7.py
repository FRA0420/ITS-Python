fruits:list[str] = ["fragole", "melone" , "uva" , "mela"]

if "fragole" in fruits:
    print("c'è")
if "melone" in fruits:
    print("c'è")
if "uva" in fruits:
    print("c'è")
if "mela" in fruits:
    print("c'è")

favoruite_fruits:list[str] = ["fragole" , "melone", "mela"]

print("Che frutta ti piace?")

if "fragole" and "melone" and "mela" in favoruite_fruits:
    print("You really like fruits!")
else:
    print("You don't like fruits")

