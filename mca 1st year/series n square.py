# Write a Program to display series 1 4 9 16 …n ( using all looping controls) 
#for loop
  
n = int(input("enter the number : ")) 


def squareofseries(n):
    for i in range(1, n+1):
        print (i**2, end = " ")
    print()

def whilesquare(n):
    i= 1
    while i <= n:
        print(i**2 , end = " ")
        i += 1

squareofseries(n)
whilesquare(n)

  
