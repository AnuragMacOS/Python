marks = [3,5,6] 
print(type(marks))
print(marks[0])


# also we can appends different types of data types in it.

lists = [3,5,6,"Anurag",True] 
print(lists[3])
print(lists[4])

# If Negative Index => length - X
lists = [3,5,6,"Anurag",True] 
print (lists[-3]) # 5-3= 2 & 2 is 6


if 7 in lists:
    print("yes")
else:
    print("No")



if "nu" in "Anurag":
    print("yes")
    

print(lists[1:5:2]) #jumps two place