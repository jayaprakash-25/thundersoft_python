f = open("doc.txt","a")
print(f.write("This is the appending statement"))

f = open("doc.txt","r")
for x in f:
    print(x)
