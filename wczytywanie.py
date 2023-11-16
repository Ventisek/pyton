f=open("text.txt", "r")
print(f.read())
f.close()

f=open("text.txt", "a")
f.write("sss\n")
f.close()

f=open("text.txt", "r")
print(f.read())
