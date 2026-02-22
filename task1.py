"""
Positive, Negative, or Zero Checker

Create a function named `check_sign` that accepts an integer. 
The function should print whether the number is **positive**, **negative**, or **zero**.

"""


nums = [1,-5,0,6,7,8]

def check_sign():
    for num in nums:
        if (num>0):
            print(f"{num} is positive number")
        elif (num<0):
            print(f"{num} is negative number")
        else:
            print(f"{num} is zero")


check_sign()



