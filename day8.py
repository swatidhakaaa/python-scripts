#class Student:
#    name="Karan"

#s1=Student()
#print(s1.name)

#s2=Student()
#print(s2.name)

#class Car:
#    color="blue"
#    brand="mercedes"

#car1=Car()
#print(car1.color)
#print(car1.brand)

#class Student:
#    name="karan"
#    def __init__(self):
#        print(self)
#        print("adding new student in Database...")

#s1=Student()    
#print(s1) 

#class Student:
#    def __init__(self,fullname):
#        self.name=fullname
#        print("adding new student in database...")

#s1=Student("karan")
#print(s1.name)

#class Student:

#    def __init__(self,name,marks):
#        self.name=name
#        self.marks=marks
#        print("adding new student in database...")

#s1=Student("karan",97)
#print(s1.name,s1.marks)

#s2=Student("arjun",88)
#print(s2.name,s2.marks)

#class Student:
#    college_name="ABC College"

#    def __init__(self,name,marks):
#        self.name=name
#        self.marks=marks
#        print("adding new student in database...")

#s1=Student("karan",97)
#print(s1.name,s1.marks)

#s2=Student("arjun",88)
#print(s2.name,s2.marks)

#print(Student.college_name)

#class Student:
#    college_name="ABC College"
#    name="anonymous"
#    def __init__(self,name,marks):
#        self.name=name
#        self.marks=marks
#        print("adding new student in database...")

#s1=Student("karan",97)
#print(s1.name)

#class Student:
#    college_name="ABC College"

#    def __init__(self,name,marks):
#        self.name=name
#        self.marks=marks

#    def welcome(self):
#        print("welcome student")    

#s1=Student("karan",97)
#s1.welcome()

#class Student:
#    college_name="ABC College"

#    def __init__(self,name,marks):
#        self.name=name
#        self.marks=marks

#    def welcome(self):
#        print("welcome student,", self.name)

#    def get_marks(self):
#        return self.marks        

#s1=Student("karan",97)
#s1.welcome()
#print(s1.get_marks())

#class Student:
#    def __init__(self, name, marks):
#        self.name=name
#        self.marks=marks

#    def get_avg(self):
#        sum=0
#        for val in self.marks:
#            sum += val
#        print("Hi",self.name,"your avg score is:",sum/3)

#s1=Student("Tony Stark",[99,98,97])
#s1.get_avg()

#s1.name="ironman"
#s1.get_avg()

#class Car:
#    def __init__(self):
#        self.acc=False
#        self.brk=False
#        self.clutch=False

#    def start(self):
#        self.clutch=True
#        self.acc=True
#        print("car started")

#car1=Car()
#car1.start()    

class Account:
    def __init__(self, bal, acc):
        self.balance=bal
        self.account_no=acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())
    
    def credit(self, amount):
            self.balance += amount
            print("Rs.",amount,"was credited")
            print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(10000,123456)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)