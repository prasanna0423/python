x=int(input("enter x-axis: "))
y=int(input("enter y-axis: "))
if x>0 and y>0:
    print("q1")
if x<0 and y>0:
    print("q2")
if x<0 and y<0:
    print("q3")
if x>0 and y<0:
    print("q4")
if x==0 and y==0:
    print("origin")
if x==0 and y!=0:
    print("on y-axis")
if y==0 and x!=0:
    print("on x-axis")
else:
    print("")