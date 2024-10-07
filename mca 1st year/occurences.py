# Write a program that will read a text and count all occurrences of a particular word


def occurencefind(text,word):

    text = text.lower()
    word = word.lower()

    wordss = text.split()

    occurences = wordss.count(word)

    return occurences


text1 = input("enter the text :  ")
word1 = input("enter the word to count its occurences : ")

result = occurencefind(text1,word1)
print(f"the given {word1} is repeated {result} times in given {text1}")

