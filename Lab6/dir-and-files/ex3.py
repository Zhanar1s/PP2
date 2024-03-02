import os

path = r'C:\Users\ACER\Desktop\githowto\repositories\w3schools\Lab6\city.txt'
if os.access(path, os.F_OK):
     print("\n" + os.path.basename(path))
     print("\n" + os.path.dirname(path) + "\n")
else:
     print(f"{path} do not exists")