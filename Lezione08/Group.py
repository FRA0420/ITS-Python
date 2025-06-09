from Lecturer import Lecturer
from Student import Student

class Group:
    def __init__(self,name:str,n_studenti:int):
        self._name=name
        self._n_studenti=n_studenti
        self._students:list[Student] = list()
        self._lecturers:list[Lecturer] = list()
    
    def getName(self):
        return self._name
    def getLimit(self)->int:
        return self._n_studenti
    def get_students(self)->int:
        return self._students
    def get_limit_lecturer(self)->int:
        if len(self._students) == 0:
            return 0
        elif len(self._students) < 10:
            return 1
        else:
            return len(self._students) // 10
    