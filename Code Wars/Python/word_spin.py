def spin_words(sentence):
    word_list = sentence.split(" ")

    new_word_list = []
    for word in word_list:
        letter_list = list(word)
        if len(letter_list) >= 5:
            letter_list.reverse()
        new_word = "".join(letter_list)
        new_word_list.append(new_word)

    new_sentence = " ".join(new_word_list)
    print(new_sentence)
    return new_sentence

spin_words("Welcome")
spin_words('Hey fellow warriors')