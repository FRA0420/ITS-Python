from persona import Persona
from alieno import Alieno

#creo un oggetto p della classe Persona
p:Persona=Persona("Chiara","Macciocchi",26)

#dobbiamo visualizzare le informazioni relative alla Persona p
print(p)

#creo un oggetto ET della classe Alieno
ET:Alieno=Alieno("Andromeda")

#visualizziamo le info relative all'alieno ET
print(ET)

#l'oggetto p invoca il metodo speak()
p.speak()

#l'oggetto Et invoca il metodo speak()
ET.speak()