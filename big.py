n=7542
biggest_digit=0
while n>0:
    digit=n%10
    if digit > biggest_digit:
        biggest_digit=digit
    n=n//10
print("the biggest digit is: ",biggest_digit)


