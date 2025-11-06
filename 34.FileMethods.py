f = open('myfile1.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


# writelines()

f = open('myfile2.txt','r')
lines = ['line 1\n','line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
        