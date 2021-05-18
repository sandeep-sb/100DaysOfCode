vowels = {'a', 'e', 'i', 'o', 'u'}
word = input('Provide a word to search for a vowel: ').lower()

found = (vowels.intersection(set(word)))
for vowel in found:
    print(vowel)