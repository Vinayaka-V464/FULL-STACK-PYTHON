# class student:
#     name ="vinay"
#     def study(self):
#         print("studying")
# student1 = student()  #student1 is object of student class
# print(student1.name)
# student1.study()   #study is method 


# class student:
#     def details(self):
#         print("had breakfast")
# s1=student()
# s1.details()

# student.details(s1)  #another way to call method

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student("vinay",20)
# s2=student("sai",21)
# print(s1.name,s1.age,s2.name,s2.age)

# class bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def check_balance(self):
#         print("balance is:",self.balance)

# account1=bank(1000)
# account1.check_balance()

# Parent class (Base class)
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating.")

# # Child class (Derived class) inheriting from Animal
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} says Woof!")

# # Create an object of the child class
# my_dog = Dog("Buddy")

# # Call the inherited method from the parent class
# my_dog.eat()

# # Call the specific method from the child class
# my_dog.bark()



# class father:
#     def house(self):
#         print("Father has a house")

# class son(father):
#     def bike(self):
#         print("Son has a bike")
# s=son()
# s.house()
# s.bike()
# class thatta:
#     def land(self):
#         print("thatta has land")

# class appa(thatta):
#     def car(self):
#         print("appa has car")

# class maga(appa):
#     def bike(self):
#         print("maga has bike")
# obj=maga()
# obj.land()
# obj.car()
# obj.bike()



# class appa:
#     def house(self):
#         print("appa has house")
# class amma:
#     def car(self):
#         print("amma has car")
# class maga(appa,amma):
#     def bike(self):
#         print("maga has bike")

# thirdclass=maga()

# thirdclass.house()
# thirdclass.car()
# thirdclass.bike()


class student:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return self.name
s=student("king")
print(s)





