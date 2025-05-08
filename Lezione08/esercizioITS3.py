# ### Classe Course:
# La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
# - Metodi:
#     - register(student): 
#     Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
#     - get_groups(): Restituisce la lista dei gruppi nel corso.
#     - add_group(group): Aggiunge un gruppo al corso.

from esercizioITS2 import Group,Student

class Course:
    def __init__(self,name:str):
        self.name=name
        self.groups:list[Group]=[]

    def register(self, student:Student):
        # Cerca il primo gruppo che ha posto disponibile
            for group in self.groups:
                if len(group.get_students()) < group.get_limit() and student.course is None:
                    group.add_student(student)
                    student.set_group(group)
                    student.set_course(self)
                else:
                    continue
       
    def get_groups(self):
        return self.groups

    def add_group(self, group:Group):
        self.groups.append(group)

