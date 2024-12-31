a=int(input("enter the start range:"))
b=int(input("enter the end range:"))
x=int(input("enetr the divisor:"))
i=a
s=0
c=0
while i<=b:
    if i%x==0:
        s=s+i
        c=c+i
print(i)
