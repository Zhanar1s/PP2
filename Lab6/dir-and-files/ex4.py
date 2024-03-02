import os

path = r'C:\Users\ACER\Desktop\githowto\repositories\w3schools\Lab6\city.txt'

with open(path, 'r') as f:
	lines = len(f.readlines())
	print(lines)