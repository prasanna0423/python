n=7524
prime_sum=0
while n>0:
   digit=n%10
   if digit==2 or digit==3 or digit==5 or digit==7:
      prime_sum +=digit
   n=n//10
print("the sum of prime digits is:", prime_sum)
