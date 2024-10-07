n = int(input("enter the three digit number :  "))

hundred = n//100
tens = (n//10)%10
unit = n%10


sum = hundred + tens + unit

print(sum)