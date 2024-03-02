import os

path = r"C:\Users\ACER\Desktop\githowto\repositories\w3schools\Lab6\new_folder"

for i in range(65,91):
    name = os.path.join(path, chr(i) + ".txt")
    f = open(name, "a")