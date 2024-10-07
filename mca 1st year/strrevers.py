#WriteaprogramtoreverseagivenString(oneword)andfindfrequencyof
#Characters found in it.

def reversestr(str):
    return str[ : : -1]




def frequency(str):
    frequency = {}
    for char in str:

        if char in frequency:
            frequency[char] +=1
        else :
            frequency =1

str1 = input("enter one word :  ")
result = reversestr(str1)
print(result)


result = frequency(str1)
print(result)