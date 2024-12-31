a=int(input("enter amount: "))
if a<=1000:
    print("no discount")
elif a>=1000 and a<5000:
    print(a-a*0.05)
elif a>=5000:
    print(a-a*0.01)

