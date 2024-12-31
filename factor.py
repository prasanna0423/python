n=int(input())
i=1
c=0
while i<=n:
    if n%i==0:
        c=c+i
    i+=1
print(c)