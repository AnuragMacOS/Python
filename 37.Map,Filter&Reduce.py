def cube(x):
    return x*x*x
print(cube(2))

l = [1,2,4,6,4,3]
# newl = []
# for item in l:
#     newl.append(cube(item))

# print(newl) -->[1, 8, 64, 216, 64, 27]

# -----Shortcut for this ------

# ------------> M A P <---------------


#convert to list first

newl = list(map(cube,l))
print(newl)

# ------------> F I L T E R <---------------


def filter_function(a):
   return a > 2
#convert to list first
newnewl = list(filter(filter_function,l))

print(newnewl) #--> 4



# ------------> R E D U C E <---------------


# we need to import reduce first

from functools import reduce

nums = [1,2,3,4]
def mysum(x,y):
  return x + y
sum = reduce(mysum,nums)

print(sum) # --> adds all of nums ==>10






