students=[]
while True:
    name=input("Enter student name (or 'exit' to finish): ")
    if name.lower() == 'exit':
        break
    students.append(name)
print("List of students:", students)
search_name=input("Enter a name to search: ")
if search_name in students:
    print(f"{search_name} is in the list.")
else:
    print(f"{search_name} is not in the list.")
