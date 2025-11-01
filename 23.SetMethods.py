# methods used to manipulate sets

s1 = {1,2,5,6}
s2 = {3,6,7}

print(s1.union(s2))

print(s1.intersection(s2))

s1.update(s2) # the s2 values goes to s1
print(s1)

s3 = s1.difference(s2)
print(s3)

# if no element common then they are disjoint
print(s1.isdisjoint(s2)) # false since 6 is common

s1.add(9)
print(s1)

s1.remove(9)
print(s1)

# if we want to remove an item that is not in set ,Removing will give error
# But discard wont give error(it will be quiet)

s1.discard(89)
print(s1)

# other methods are pop(), del-->deletes entire set,clear-->it clears all elements of the set

if 6 in s1:
    print("its here")
else:
    print("its not here")


