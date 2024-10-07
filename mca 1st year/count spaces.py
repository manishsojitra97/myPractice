# Write a program to count number of spaces, comma, lines, words and characters in a
#  given string.

def count(str):
  spaces = str.count(" ")
  coma = str.count(",")
  words = len(str.split())
  lines = str.count("\n") +1
  char = len(str)
  return spaces , coma , words, lines , char
str1 = str(input("enter the string value : "))
result = count(str1)
print(result)