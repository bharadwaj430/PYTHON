class student:
  def __init__(self):
    self.name = "Ram"
    self.__marks = 80
  def get_marks(self):
    return self.__marks
s = student()
print(s.name)
print(s.get_marks())


#private variable

class Employee:
    def __init__(self):
       self.__sal = 50000
    def get_sal(self):
        return self.__sal
    def set_sal(self,sal):
            self.__sal = sal
e = Employee()
print(e.get_sal())



     


        


