# find vowel frequency in string entered by user using a dictionary
# uses setdefault() so that we only create a key/value pair when we need one

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels:")

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, ' was found', v, ' time(s).')
