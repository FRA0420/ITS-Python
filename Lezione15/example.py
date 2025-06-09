# file = open("example.txt", "a")
# print(file)

# file.close()

with open("example.txt", "r") as file:
    print(file.read())