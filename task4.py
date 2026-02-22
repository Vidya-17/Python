"""
**List Manipulation**
**Problem:** Create a function named `remove_duplicates` that takes a list of numbers as input.
The function should remove any duplicate numbers from the list and return a new list with only 
unique numbers.

"""



def remove_duplicates(numbers):
    return list(set(numbers))

print(remove_duplicates([2,4,5,5,5,6,6,7,8,3,2,2,4]))