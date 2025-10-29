#Basically it is switch case -->but in match case , no need to add break in it

x = int(input("Enter a number : "))
match x:

    case 0:
        print("x is zero")

    case 3:
        print("x is 3")

   # case _ :   -->this is default
   #     print(x)
    
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, " is not 80")
    case _:
        print(x)
        

# we can also add if else in it 
#lets add 4 cases of default case

