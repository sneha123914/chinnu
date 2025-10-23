class Student:
   
   def __init__(self,name):
      self.name = name
   def show(self):
       print("My name : ",self.name)
   def __del__(self):
       print("object destroyed")
s1 = Student("iot")
s2 = student("iotab")
s1.show()
s2.show()
