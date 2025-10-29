for i in range(13):
    if(i==11):
        break
    print("5 X", i+1, "=", 5 * (i+1))

print("stopped ")

for i in range(13):
    if(i==10):
       print("Skipped the iteration")
       continue
    
    print("5 X", i, "=", 5 * i)
    