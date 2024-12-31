n=7524
odd_sum=0
while n>0:
   digit=n%10
   if digit %2!=0:
      odd_sum +=digit
   n=n//10
print("the sum of odd digits is:", odd_sum)
