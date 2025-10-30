#-----Manipulating Tuples-------
# we cant change tuples but if we wish to,first convert tuple to list then do operations

countries=("Spain","India","USA","UAE","Italy")
print(countries)
temp = list(countries)
temp.append("Russia")
temp.pop(3)
countries = tuple(temp)
print(countries)

countries2 = ("Chile", "Oman","Czech")
totalCountries = countries + countries2
print(totalCountries)

