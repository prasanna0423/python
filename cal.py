a=int(input("enter a value:"))
if a<=50:
    b=a*2
    print(b)
elif a>=50 and a<150:
    b=100+(a-50)*3
    print(b)
elif a>=150 and a<=350:
    b=400+(a-150)*4
    print(b)
elif a>=350:
    b=1200+(a-350)*5
    print(b)



