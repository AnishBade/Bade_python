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


class Programmer(Employee):
    def __init__(self,fname,lname,salary,lang,exp):
        super().__init__(fname,lname,salary)
        self.lang=lang
        self.exp=exp

    def increase(self):
        self.salary=self.salary*(Employee.inc+0.5)

anish=Employee('anish','bade',50000)
sayera=Programmer('sayera1','bhandari',50000,'python','5 yrs')
Employee.change_increment(2.5)
anish.increase()
print(anish.salary)
sayera.increase()
print(sayera.salary)

print(help(Programmer))
