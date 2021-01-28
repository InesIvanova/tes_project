import os

try:
    os.remove("my_first_file.txt")
    print("Deleted")
except FileNotFoundError:
    print("File already deleted!")

# if os.path.exists("my_first_file.txt"):
#     os.remove("my_first_file.txt")
#     print("Deleted successfully")
# else:
#     print("File already deleted!")

