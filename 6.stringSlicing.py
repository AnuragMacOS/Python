name = "Anurag"
nameLen = len(name)

print(nameLen)

#slicing
print(name[0:6])
print(name[0:-3]) # same as print(name[0:len(name)-3]) 
                     # [0:3] gives 'An'

print(name[-1:-3])  #6-1= 5--> 6-3=3. 5 to 3 print doesnt make sense. So python gets confused.
