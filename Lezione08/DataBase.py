from Course import Course
from Facoltà import Faculty

class DataBase:
    def __init__(self,name:str,id:str):
        self._name=name
        self._id=id
        self._courses = dict()
    
    def get_name(self)->int:
        return self._name
    
    def get_id(self):
        return self._id
    
    def add_courses(self,f:Faculty, c:Course):
        if f.get_id() not in self._courses:
            self._courses[f.get_id()] = dict()

        self._courses[f.get_id()][c.get_id()]=c

    def 
    