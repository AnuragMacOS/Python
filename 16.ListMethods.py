l = [1,2,4,3]
print(l)



l.append(7)

l.sort()
print(l)

l.reverse()
print(l)

print(l.index(1)) # gives the index no. where 1 is

print(l.count(1)) #returns count of 1(how many times it appears)

m =l
m[0]=0
print(l) # -->[0, 2, 4, 3] m is acting as reference to l
         # so whatever changes you make to m, it will affect to l as well

m= l.copy()
m[0]= 0
print(l) #-->[1, 2, 4, 3]

 # l.insert(1,899)

m=[900,1000,1100] 
l.extend(m) #-->[1, 2, 4, 3, 900, 1000, 1100]
print(l)

