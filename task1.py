nums = [1,-5,0,6,7,8]

def check_sign():
    for num in nums:
        if (num>0):
            print(f"{num} is positive number")
        elif (num<0):
            print(f"{num} is negative number")
        elif (num==0):
            print(f"{num} is zero")


check_sign()



