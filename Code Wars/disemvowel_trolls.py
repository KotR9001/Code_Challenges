def disemvowel(string):
    letters = []
    for letter in string:
        letters.append(letter)
    print(letters)
    consonants = []
    for letter in letters:
        if letter not in ['a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U']:
            consonants.append(letter)
    print(consonants)
    separator = ""
    string = separator.join(consonants)
    print(string)
    return string

disemvowel("This website is for losers LOL!")