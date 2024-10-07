# print("hello world")

# print("name : manish ")

# x = int(input("enter the no1 :  "))
# y = int(input("enter the number2 : "))
# 110
# sum = x +y
# sub = x-y
# div = x/y
# mul = x*y
# pow = x**y
# mod = x%y

# print (sum)
# print(sub)
# print(pow)

# def convert(rupee):
#     return int(rupee*100)

# rupee = float(input("enter the rupee :"))

# paisa = convert(rupee)
# print(paisa)



# def convert_dollar(dollar):
#     return int(dollar*84)

# dollar = int(input("enter the no. of dollar : "))


# rupee = convert_dollar(dollar)
# print(rupee)


# Write a Program to swap two numbers using temporary variable.

# a = 10
# b =20

# d = b 
# b = a
# a = d

# print(a)
# print(b)

# Write a Program to check whether given Number is an odd or Even Number

# x = int(input("enter the number :"))

# if x%2 == 0:
#     print("given number is even")
# else :
#     print("given number is odd ")

# Write a Program to find maximum number from user entered 3 numbers.

a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = int(input("enter the 3rd number : "))

if a>=b and a>= c :
     max = a
elif b >= a and b>= c :
     max = b
else :
     max = c
print(f"the highest given number is {max}")
