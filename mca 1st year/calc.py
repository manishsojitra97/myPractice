def calc(x,y,operation):
    if operation == '+':
        return x+y
    elif operation == '-':
        return x-y
    else:
        return "no valid operation"
    
x = int(input("enter the first no. "))
y = int(input("enter the second num "))
operation = input("enter the operation sifn : ")
    
cal = calc(x,y,operation)

print(f"the result is {cal}")