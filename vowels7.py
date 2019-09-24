# using sets and the intersection method to find out if a string contains vowels

vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Provide a word to search for vowels:")

vowels_in_string = vowels.intersection(set(word))

print(vowels_in_string)
