numbers_dictionary = {}


while True:
    number_as_string = input()
    if number_as_string == "Search":
        break
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    except TypeError:
        print("This is not the type we are looking for")
    except (KeyError, Exception):
        print("Invalid operation")

line = input()

while line != "Remove":
    searched = line

    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)
