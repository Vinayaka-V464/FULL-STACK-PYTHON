# student = ('ram','sam','john','peter')
# print(student)

# numbers = (1, 2, 3, 4, 5)
# print(numbers[-3])

# data = (1, 2, 3, 4, 5)
# data[0] = 10  # This will raise an error because tuples are immutable
# print(data)

# x = (1, 2, 3)
# print(x.count(2))  # Output: 1

# X=('vinay','dhoni','rohit','virat','dhoni','dhoni')
# print(X.count('dhoni'))
# print(X.index('rohit'))  # Output: 2

# num=(1, 2, 3, 4, 5)
# print(num[1:4])  # Output: (2, 3, 4)

#sets
# set is a collection of unique elements, meaning it does not allow duplicate values. Sets are unordered, which means that the items do not have a defined order, and they cannot be accessed by index. 
# x={1, 2, 3, 4, 5}
# print(x)
# data={1, 2, 3, 4, 5, 5, 5}
# data.add(6)
# data.remove(3)
# print(data)  # Output: {1, 2, 3, 4, 5, 6}

# a={1, 2, 3}
# b={3, 4, 5}
# print(a & b)  
# print(a | b) 
# print(a - b)
# print(a ^ b)

# def greet():  #function
#     print("hello")
# greet() 

# def sub():
#     return 10-5
# result=sub()
# print(result)

# def add(a, b):
#     print(a + b)
# add(10, 5)


# def add(*args):
#     print(args)
# add(10, 20, 30, 40)  # Output: (10, 20, 30, 40)



# def add(*numbers):
#     total =0
#     for i in numbers:
#         total += i
#     print("Sum:", total)
# add(10, 20, 30, 40)  

# def student(**details):
#     print("name",details['name'])
#     print("age",details['age'])
#     print("job",details['job']
#     )
# student(name="John", age=20, job="Student")

# def squareroot(num):
#     return num ** 0.5
# print(squareroot(16))  # Output: 4.0

# add=lambda a,b:a+b
# print(add(10,20))

# check_num = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(check_num(7))   
# print(check_num(12))

# name=lambda x:x.upper()
# print(name("dhoni"))  


# file = open("test.txt", "w")
# file.write("hello")
# file.close()
# print("file created successfully")

# file = open("test.txt", "r")
# data = file.read()
# print(data)
# file.close()

# file = open("test.txt", "a")
# file.write("\nworld")
# print("data appended successfully")
# file.close()

# file = open("test.txt", "r")
# print(file.read())
# file.close()
# try:
#     a=10
#     b=0
#     print(a/b)  # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# try:
#     num = int(input("Enter a number: "))
#     print("You entered:", num)
# except ValueError:
#     print("only numbers are allowed")
# try:
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer.")

# try:
#     file =open("non_existent_file.txt", "r")
#     print(file.read())
# except FileNotFoundError:
#     print("Error: The file does not exist.")
# finally:
#     print("File operation completed.")


try:
    print(10/2)
except:
    print("error")
else:
    print("no error")
