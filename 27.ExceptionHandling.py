a = input("Enter the number: ")
print(f"Multiplication table of{a} is : ")

try:
    for i in range(1,11):
       print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input! ")

print("Some important lines of code")
print("End of program")


try:
    num=int(input("Enter an number"))
except ValueError:
    num=int(input("Entered num is not an number"))

