# 'is' ==> compares "exact location" of object in memory
# '==' ==> compares "values" of it

a = [1,2,49]
b = [1,2,49] # list can be changes so location assigned is different

print( a is b)  #False
print(a==b) # True

print("-----------")
 

a = 3
b = 3

print( a is b) #true
print(a==b) #true

print("-----------")


a = (1,2)
b = (1,2) # tuple cant be changes so location assigned is same

print( a is b) #true
print(a==b) #true

