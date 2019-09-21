# find unique vowels in string entered by user using a list

vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to searcdh for vowels:")

found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)
