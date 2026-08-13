#class Student:
#    def __init__(self,name):
#        self.name=name

#s1=Student("Swati")
#print(s1.name)

#del s1.name
#print(s1.name)

#class Account:
#    def __init__(self,acc_no,acc_pass):
#        self.acc_no=acc_no
#        self.__acc_pass=acc_pass

#    def reset_pass(self):
#        print(self.__acc_pass)

#acc1=Account("12345","abcde")

#print(acc1.acc_no)
#print(acc1.reset_pass())

#class Person:
#    __name="anonymous"

#    def __hello(self):
#        print("hello person!")

#    def welcome(self):
#        self.__hello()

#p1=Person()
#print(p1.welcome())

#class Person:
#    __name="anonymous"

#    def __hello(self):
#        print("hello person!")

#    def welcome(self):
#        self.__hello()

#p1=Person()
#print(p1.welcome())

#class Car:
#    color="black"
#    @staticmethod
#    def start():
#        print("car started...")

#    @staticmethod
#    def stop():
#        print("car stopped")

#    class ToyotaCar(Car):
#        def __init__(self,name):
#            self.name=name

#car1=ToyotaCar("fortuner")
#car2=ToyotaCar("prius")
#print(car1.name)

#class Car:
#    color="black"
#    @staticmethod
#    def start():
#        print("car started...")

#    @staticmethod
#    def stop():
#        print("car stopped")

#class ToyotaCar(Car):
#    def __init__(self,brand):
#        self.brand=brand

#class Fortuner(ToyotaCar):
#    def __init__(self,type):
#        self.type=type

#car1=Fortuner("Diesel")
#car1.start()

#class A:
#    varA="welcome to class A"

#class B:
#    varB="welcome to class B"

#class C(A,B):
#    varC="welcome to class C" 

#c1=C()
#print(c1.varC)
#print(c1.varA)
#print(c1.varB)  

#class Car:
#    def __init__(self,type):
#        self.type=type

#    @staticmethod
#    def start():
#        print("car started...")

#    @staticmethod
#    def stop():
#        print("car stopped")

#class ToyotaCar(Car):
#    def __init__(self,name,type):
#        super().__init__(type)
#        self.name=name

#car1=ToyotaCar("prius","electric")
#print(car1.type)

#class Person:
#    name="anonymous"

#    def changeName(self,name):
#        self.name=name

#p1=Person()
#p1.changeName("Swati")
#print(p1.name)
#print(Person.name)

#class Person:
#    name="anonymous"

#    def changeName(self,name):
#        Person.name=name

#p1=Person()
#p1.changeName("Swati")
#print(p1.name)
#print(Person.name)

#class Person:
#    name="anonymous"

#    @classmethod
#    def changeName(cls,name):
#       cls.name=name

#p1=Person()
#p1.changeName("Swati")
#print(p1.name)
#print(Person.name)

#class Person:
#    name="anonymous"
    
#    def changeName(self,name):
#        self.__class__.name="Swati"

#p1=Person()
#p1.changeName("Dhaka")
#print(p1.name)
#print(Person.name)

#class Student:
#    def __init__(self,phy,chem,maths):
#        self.phy=phy
#        self.chem=chem
#        self.maths=maths

#    def calcPercentage(self):
#        self.percentage=str((self.phy + self.chem + self.maths)/3) + "%"

#stu1=Student(98,97,99)

#stu1.phy=86
#print(stu1.phy)
#stu1.calcPercentage()
#print(stu1.percentage)

#class Student:
#    def __init__(self,phy,chem,maths):
#        self.phy=phy
#        self.chem=chem
#        self.maths=maths

#    @property
#    def percentage(self):
#        return str((self.phy + self.chem + self.maths)/3) + "%"

#stu1=Student(98,97,99)
#print(stu1.percentage)

#stu1.phy=86
#print(stu1.percentage)

#print(1+2)
#print("apna" + "college")
#print([1,2,3] + [4,5,6])

#class Complex:
#    def __init__(self,real,img):
#        self.real=real
#        self.img=img

#    def showNumber(self):
#        print(self.real, "i+", self.img, "j")

#    def add(self,num2):
#        newReal=self.real + num2.real
#        newImg=self.img + num2.img
#        return Complex(newReal,newImg)

#num1=Complex(1,3)
#num1.showNumber()

#num2=Complex(4,6)
#num2.showNumber()

#num3=num1.add(num2)
#num3.showNumber()

#class Circle:
#    def __init__(self,radius):
#        self.radius=radius

#    def area(self):
#        return (22/7) * self.radius ** 2
#    def perimeter(self):
#        return 2 * (22/7) * self.radius

#c1=Circle(21)
#print(c1.area())
#print(c1.perimeter())

#class Employee:
#    def __init__(self,role,dept,salary):
#        self.role=role
#        self.dept=dept
#        self.salary=salary

#    def showDetails(self):
#        print("Role=",self.role)
#        print("Dept=",self.dept)
#        print("Salary=",self.salary)

#e1=Employee("accountant","finance","60,000")
#e1.showDetails()

#class Employee:
#    def __init__(self,role,dept,salary):
#        self.role=role
#        self.dept=dept
#        self.salary=salary

#    def showDetails(self):
#        print("Role=",self.role)
#        print("Dept=",self.dept)
#        print("Salary=",self.salary)

#class Engineer(Employee):
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#        super().__init__("Engineer","IT","80,000")

#e1=Employee("accountant","finance","60,000")
#e1.showDetails()

#eng1=Engineer("Alice",25)
#eng1.showDetails()

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 =  Order("Laptop",50000)
odr2 = Order("Mobile",30000)
print(odr1 > odr2)