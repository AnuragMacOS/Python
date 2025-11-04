# TO LOOP
#  to print 5th number if the 5th index comes

marks = [12,56,32,98,12,45,69,40]

#index = 0
#for mark in marks:
#   print(mark)
#    if(index == 3):
#     print("Anurag here !!!")
#  index +=1

# to do this in easier way , USE ENUMERATE


for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
      print("Anurag here !!!")

