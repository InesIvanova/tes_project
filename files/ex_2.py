with open("numbers.txt", "r") as file:
    name, person_id = file.readline().split()
    print(name, person_id)

print("Hello")



