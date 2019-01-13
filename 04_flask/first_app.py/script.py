from os import open

f = open("hi.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()