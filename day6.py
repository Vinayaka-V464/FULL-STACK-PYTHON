# class bank:
#     def __init__(self):
#         self.balance=1000
# account=bank()
# print(account.balance)

# class employee:
#     def __init__(self,salary):
#         self.__salary=salary
    
#     def get_salary(self):
#         return self.__salary
    
# emp=employee(52836)
# print(emp.get_salary())

# class employee:
#     def __init__(self):
#         self.__salary=0
#     def set_salary(self,amount):
#         if amount>0:
#             self.__salary=amount
#         else:
#             print("invalid salary")

#     def get_salary(self):
#         return self.__salary
    
# emp=employee()
# emp.set_salary(52836)
# print(emp.get_salary())

class dog:
    def sound(self):
        print("dog barks")

class cat:
    def sound(self):
        print("cat meows")

class animal:
    def sound(self):
        print("animal makes sound")

Dog=dog()
Cat=cat()
Animal=animal()

Dog.sound()
Cat.sound()
Animal.sound()
Cat.sound()