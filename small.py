n=5784
biggest_digit=9
while n>0:
    digit=n%10
    if digit < smallest_digit:
        smallest_digit=digit
    n=n//10
print("the smallest digit is: ",smallest_digit)
