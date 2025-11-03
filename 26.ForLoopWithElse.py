for i in range(5):
    print(i)
else: # bcz i =5 wont executed
    print("Sorry no i")

# Else execute hone ka matlab ye hai ki LOOP KHATAM HO CHUKI HAI
# LAST VALUE TAK GAYA HAI, LAST ITERATION PROCESS HO CHUKI HAI

for i in range(5):
    print(i)
    if i==4:
        break
else: 
    print("Sorry no i")  # 0,1,2,3,4
# since loop wasnt completely finished hence else wasnt printed

