a=int(input("enter a value:"))
if a<=50:
    b=a*2
    print(b)
elif a>=50 and a<=150:
    b=100+(a-50)*3
    print(b)
elif a>300:
    b=400+(a-100)*5
    print(b)