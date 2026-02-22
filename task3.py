"""
List Filter 
**Problem:** Given a list of numbers, create a new list containing only 
numbers greater than 50.

"""


list1 = [70,70,90,100,50,40,30,20,10]
list2 = []

def filter_list():
    for nums in list1:
        if (nums>50):
            list2.append(nums)
            
    print(f"{list2}")
        

filter_list()