x = 4

def hello():
    x = 5
    print(f"The local x is {x}")
    print("Hello Anurag")


print(f"The global x is {x}")
hello()
print(f"The global x is {x}")


print("!!!!!lets make the gloabal x as 5!!!!!!")

x = 4

def hello():
    x = 5
    y=1
    print(f"The local x is {x}")
    print("Hello Anurag")


print(f"The global x is {x}")
hello()
x =5
print(f"The global x is {x}")
# print(y) --> we can't print y because y is a local var


