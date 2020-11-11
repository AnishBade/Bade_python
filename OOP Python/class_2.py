class Employee:
    inc=1.5
    def __init__(self,fn,ln,salary):
        self.fname=fn
        self.lname=ln
        self.salary=salary

    def increase(self):
        self.salary=int(self.salary*Employee.inc)
    @classmethod
    def change_increment(cls,val):
        cls.inc=val
    @classmethod
    def emp_string(cls,str):        #We can create constructor like this also
        fname,lname,salary=str.split("-")
        return cls(fname,lname,salary)
# anish=Employee('Anish','Bade',10000)
# print(anish.salary)
# anish.increase()
# print(anish.salary)
# anish.change_increment(2)
# anish.increase()
# print(anish.salary)

sayera=Employee.emp_string("Sayera-Bhandari-50000")
print(sayera.salary)
sayera=Employee("Sayera","Bhandari","80000")
print(sayera.salary)