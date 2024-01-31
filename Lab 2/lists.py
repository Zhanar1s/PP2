#1. Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])     #output: banana


#2. Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)   #output: ['kiwi', 'banana', 'cherry'] 

#3. Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)   #output: ['apple', 'banana', 'cherry', 'orange']


#4. Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)   #output: ['apple', 'lemon', 'banana', 'cherry']


#5. Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)   #output: ['apple', 'cherry']


#6. Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])   #output: cherry


#7. Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])  #output: ['cherry', 'orange', 'kiwi']


#8. Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  #output: 3
