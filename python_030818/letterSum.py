import collections
word = str(input("Enter a word: ")).lower()
letters = collections.Counter(word)
print(letters)


def countLetters(word):
    letterdict={}
    for letter in word:
        letterdict[letter] = 0
    for letter in word:
        letterdict[letter] += 1
    return letterdict
word = str(input("Enter a word: ")).lower()
print(countLetters(word))