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
    @staticmethod
    def open(day):
        if(day=='saturday'):
            return True
        else: return False
anish=Employee.emp_string('Anish-Bade-100000')
print(anish.open('sunday'))
print(Employee.open('saturday'))