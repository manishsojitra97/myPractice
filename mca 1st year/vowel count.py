# Write a program to count number of vowels in a given string.
str = str(input("enter the string : "))
vowel = 0
for ch in str :
    if ch in 'aeiou':
        
         vowel += 1

if vowel > 0 :
    print("yes there is a wovel with the count of : " , vowel)
else:
    print("no vowel found")











