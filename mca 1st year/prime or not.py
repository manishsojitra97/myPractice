# Write a function prime that returns 1 if its argument is a prime no. and returns 0

def primeornot(n):
    if n<= 1 :
        return 0

    else :
        for i in range (2, int(n**0.5)+1):
            if n%i == 0:
                return 0
     
    return 1
n1 = int(input("enter the no, ;   "))

result = primeornot(n1)
print(result)