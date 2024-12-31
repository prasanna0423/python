n=int(input())
h=n-1
for i in range(n):
    for k in range(h):
        print("#",end="")
        for j in range(i+1):
            print("*",end="")
    print()