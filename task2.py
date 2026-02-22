"""
Odd or Even Checker Function

**Problem:** Create a Python function named `check_number` that accepts a single integer parameter.
The function should check whether the provided number is even or odd and then print the result.

"""

nums =[1,2,3,4,5,6,7,8,9,10]
def evod(nums):
    for num in nums:
        if (num%2==0):
            print (num, 'is even')
        else:
            print (num, 'is odd')

evod(nums)