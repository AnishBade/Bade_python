class Employee:
    inc=1.5
    num=0


    def __init__(self,fn,ln,salary):
        self.firstName=fn
        self.lastName=ln
        self.salary=salary
        Employee.num+=1
        self.num=Employee.num

    def printname(self):
        print(self.firstName,self.lastName)

    def increase(self):
        self.salary = int(self.salary*Employee.inc)

    @classmethod
    def change(clsan,increment):
        clsan.inc=increment


anish=Employee('Anish', 'Bade', 5000)
#anish.printname()
# print(anish.__dict__)
sayera=Employee('Sayera','Bhandari',10000)
# shriniva=Employee('Shrinva','Serafina',20000)
# print(sayera.__dict__)
# print(shriniva.__dict__)
# print(sayera.salary)

print(sayera.salary)
sayera.increase()
print(sayera.salary)
Employee.change(2)
sayera.increase()
print(sayera.salary)
