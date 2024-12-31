a=int(input("enter a value: "))
b=int(input("enter b value: "))
c=int(input("enter c value: "))
if a<90 and b<90 and c<90:
    print("acute triangle")
if a==90 or b==90 or c==90:
    print("right angle triangle")
if a>90 or b>90 or c>90:
    print("obtuse angle")
else:
    print("")