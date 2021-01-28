try:
    with open("test_file.txt"):
        print("File found!")
except FileNotFoundError:
    print("File not found")