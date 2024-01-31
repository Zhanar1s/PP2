#1. Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!") #output: Yes, apple is a fruit!


#2. Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)   #output: {'orange', 'banana', 'apple', 'cherry'}


#3. Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)   #output: {'orange', 'cherry', 'banana', 'grapes', 'apple', 'mango'}
print(more_fruits)  #output: ['orange', 'mango', 'grapes']


#4. Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)   #output: {'apple', 'cherry'}


#5. Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)   #output: {'cherry', 'apple'}