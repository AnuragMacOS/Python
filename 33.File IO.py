# READING A FILE

f = open('myfile.txt', 'r') # r means read mode and its default mode
                            #even if we remove r , we can still read file
print(f)
text = f.read()
print(text)
f.close()


# WRITING IN A FILE
f = open('myfile.txt', 'a') # r means read mode 
f.write("Good Luck dawg")
f.close()

# if we don't want to write close() , We can say --> with open('myfile.text','a')
