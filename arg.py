m=int(input("enter m value:"))
n=int(input("enetr n value:"))
ans=0
i=0
while(i<=n):
    if(i>=m):
        ans+=i
    i+=15
print(ans)