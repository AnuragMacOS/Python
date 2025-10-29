def average(a,b):
    print("The average is : ", (a+b)/2)

average(4,6)


# -----------default Argument----------

def average(a=12,b=8):
    print("The average is : ", (a+b)/2)
average()


def average(a=12,b=8):
    print("The average is : ", (a+b)/2)
average(6) # overrides the a=12 to a = 6 and b same


def average(a,b,c=1):
    print("The average is : ", (a+b+c)/2)
average(5,6) # value for a and b


#----------Variable length Argument------------


def average(*numbers):
    sum =0
    for i in numbers:
        sum = sum + i
        print("Average is:",sum/len(numbers))

average(5,6,4)