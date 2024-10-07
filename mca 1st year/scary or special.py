# a number is special if it is divisible by 15, big if it is greater than 999, weird if it is divisible by 5 and 6 but not 18, and scary
# if it is big or weird. The task is to write a program to determine which of the numbers 450, 540, 600, and 675 are special but not scary.

def special(n):
    return n%15 == 0
def big(n):
    return n>999
def weird(n):
    return n%5==0 and n%6==0 and n%18!= 0
def scary(n):
    return big(n) or weird(n)
def spc(n):
    return special(n) and not scary(n)

n1 = [450,540,600,675]


for  i in n1 :
    if spc(i):
        print(f"{i} is special but not scafry") 
    else:
        print(f"{i} is not that")