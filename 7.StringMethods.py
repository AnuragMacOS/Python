#string are immutable, we cant change them

a = "Anurag"
print(len(a))
print(a.upper()) #gives all in uppercase

print(a.replace("Anurag", "John"))

b = "!!!!!Hancy!!!!!!"
print(a.rstrip("!"))


blogHeading = "intro to python"
print(blogHeading.capitalize()) #turns first letter as capital

str1 = "Welcome to the console!!"
print(str1.center(50))

print(a.count("Anurag")) # says how many times Anurag is in a string


str1 = "Welcome to the console!!"
print(str1.endswith("to",4,10)) #between 4 to 10 th character, is there "to"-->yes, so gives TRUE

print(str1.find("is")) # "is" is not in it thus gives-->-1

str1 = "WelcometotheConsole" 
print(str1.isalnum()) # true if entire string us A-Z,a-z,0-9

str1 = "WelcometotheConsole"
print(str1.isalpha())  # true if entire string us A-Z,a-z

str1 = "WelcometotheConsole\n"
print(str1.isprintable())  # true if entire string can be printed(if \n is present
                           #then it gives false because \n cant be printed)


