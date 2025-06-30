try:
    a = input("Enter file name: ")
    file = open(a, "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: The file",a,"was not found.")
