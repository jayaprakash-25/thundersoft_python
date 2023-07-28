
#Working with String functions:
'String indexing and slicing'

s="hyderabad"
print(s[0])
print(s[-1])
print(s[8])

s="hyderbad"
print(s[2:7])
print(s[:6])
print(s[1:])
print(s[:])
print(s[0:9:1])
print(s[::-1])
print(s[7:1])
print(s[-1:-5])
print(s[-5:-1])


' String Concatenation and Multiplication'
s1="durga"
s2="soft"
print(s1+s2)
print(s1+" "+s2)
print("mohan"+" "+"kumar")
print(s1*3)
print((s1+" ")*3)
print(("mohan"+" ")*3)

'String split and max split'
s="python is very easy and it is oop and it is interpreter"
print(s)
s1=s.split(" ",3)
print(s1)
print(type(s1))
for i in s1:
 print(i)


'String capitalize and title'
s="pyThon is vEry eaSy"
print(s.capitalize())
print(s.title())

'String upper and lower'
s="durgasoft"
print(s)
print(s.upper())
s="DURGASOFT"
print(s)
print(s.lower())

'String Count'
s="python is very easy and it is oop and it is interpreter"
substring="is"
print(s.count(substring))
print(s.count("and"))
print(s.count("is"))
print(s.count("x"))
print(s.count(" "))
print(s.count('a'))


'String replace'
s="my name is durga"
s1=s.replace("durga","mohan")
print(s1)

'String join'
print(",".join("MOHAN"))
print(" ".join(["sai","mohan","raj","durga"]))


'String reverse'
s='sai'
print(s[::-1])

'String sort'
s="python is very easy"
print(s)
s1=s.split(" ")
print(s1)
print(type(s1))
s1.sort()
print(s1)
s1.sort(reverse=True)
print(s1)

'Swap case'
s="DuRgAsOfT"
print(s)
print(s.swapcase())

' String strip , lstrip, rstrip'

s=" durga "
print(s)
print(s.strip(" "))
s="adurga"
print(s)
print(s.strip('a'))
print(s.lstrip('a'))
print(s.rstrip('a'))

'string length'
print(len("durga soft"))

'String find , index ,rindex'

s="python is very easy and it is oop and it is interpreter"
print(s.find("is"))
print(s.find("x"))
print(s.index("is"))
print(s.rindex("is"))

'String max min'
s="durgasoft"
print(max(s))
print(min(s))
s="DURGASOFT"
print(max(s))
print(min(s))

'String partion'
s="python is very easy and it is oop"
s1=s.partition("is")
print(s1)
print(type(s1))

'String startswith , endswith'
s="durgasoft"
print(s.startswith('a'))
print(s.startswith('D'))
print(s.startswith('d'))
print(s.endswith('T'))
print(s.endswith('t'))

' String isdigit ,isalpha, isalnum'

s="12345"
print(s.isdigit())
s="12345a"
print(s.isdigit())
s="abcd"
print(s.isalpha())
s='abcd12'
print(s.isalpha())
s="abcd"
print(s.isalnum())
s="1234"
print(s.isalnum())
s="123abc"
print(s.isalnum())
s="$%#%"
print(s.isalnum())














