# in python , by default input accepts string
# so we need to convert it to int or float if needed
name = input("Enter your name: ")
print(f"Hello, {name}!")

age = int(input("Enter your age: "))
print(f"You are {age} years old.")

height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")

# basic boolean operation
age = True if age >= 18 else False
print (f"Is adult: {age}")

# variable binding in python
x = 5
y = 5
#both x and y point to the same object in memory

# list slicing in python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[1:4])  
print(my_list[:3])   
print(my_list[2:])  
print(my_list[-2:]) 
# list slicing with step
# [start:stop:step]
print(my_list[::2])  
print(my_list[1::2])  
my_list.append(11)  # adding an element to the list
print(my_list)
my_list.remove(5)  # removing an element from the list
print(my_list)
my_list.insert(0, 0)  # inserting an element at a specific position
print(my_list)

# types of listing 
# tuple 
my_tuple = (1, 2, 3, 4, 2, 5)
print(my_tuple[1:4])
my_tuple.count(2)  # count occurrences of an element
print(my_tuple.count(2))
my_tuple.index(3)  # find the index of an element
print(my_tuple.index(3))

# tuple slicing with step
print(my_tuple[::2])    


# set 
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)  # adding an element to the set
print(my_set)
my_set.remove(3)  # removing an element from the set
print(my_set)
# set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))  # union
print(set_a.intersection(set_b))  # intersection
print(set_a.difference(set_b))  # difference
# no duplicate elements in set
set_c = {1, 2, 2, 3, 4}
print(set_c) 
# frozen set
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)

# range 
my_range = range(1, 11)
print(list(my_range))

# range(start, stop, step)
my_range = range(1, 11, 2)
print(list(my_range))


# dictionary
my_dictionary = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dictionary["name"])
print(f"Name: {my_dictionary["name"]}")  
print(my_dictionary.get("age"))
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())
my_dictionary["age"] = 31  # updating a value
print(my_dictionary)
my_dictionary["country"] = "USA"  # adding a new key-value pair
print(my_dictionary)
del my_dictionary["city"]  # deleting a key-value pair
print(my_dictionary)
for key, value in my_dictionary.items():
    print(f"{key}: {value}")