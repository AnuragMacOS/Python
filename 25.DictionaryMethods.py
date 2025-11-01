#Dictionary is ordered unlike Sets

emp1 = {122 : 45 , 123 : 89 , 567 : 69, 670 : 69}
emp2 = {222 : 67, 566 : 90}

emp1.update(emp2)
print(emp1)

#emp1.clear()

emp1.pop(122)
print(emp1)

# other methods are del , popitem() etc

