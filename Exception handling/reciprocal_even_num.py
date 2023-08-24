try:
    num=int(input("enter the num"))
    assert num%2==0
except:
     print("not a even num")
else:
    reciprocal=1/num
    print(reciprocal)
