class Student:
    def __init__(self,name:str,studyProgram:str,age:int,gender:str):
        self.name=name
        self.studyProgram=studyProgram
        self.age=age
        self.gender=gender

    def printInfo(self):
       print(self.name,self.studyProgram,self.age,self.gender) 
    
chiara = Student("Chiara","Inglese",26,"female") 
chiara.printInfo()

riccardo = Student("Riccardo","gym",24,"male")
riccardo.printInfo()

leonardo = Student("Leonardo","Psicologia",27,"male")
leonardo.printInfo()