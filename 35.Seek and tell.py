# seeks moves the read to particular byte

with open('file.txt','r') as f:
    print(type(f))

   #move to the 10th byte in the file
   
    f.seek(10)
   
   #read the next 5 bytes

# My name is anurag --> a is at 11th byte (count from start,count spaces as well)
    data=f.read(5)
    print(data)

    print(f.tell()) # tells the seek number

    
    # truncate

    f.write("hello world!")
#   f.truncate (5) -->it truncates whole file to 5 bytes
