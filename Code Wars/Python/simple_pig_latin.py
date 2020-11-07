def pig_it(text):
    #Split the Text Into a Word List
    word_list = text.split(" ")
    #print(word_list)

    #Create a List for the New Words
    new_word_list = []
    #Split the Words in word_list into Separate Letters
    for i in range(len(word_list)):
        letter_list = list(word_list[i])
        #print(letter_list)
        #Create a New Letter List to Append Letters To
        new_letter_list = []
        #Move the First Letter in letter_list[i] to the Back
        for j in range(len(letter_list)):
            #Append All Letters Past the First into new_letter_list
            if j > 0:
                new_letter_list.append(letter_list[j])
            #print(new_letter_list)
        #Append the First Letter to the End of new_letter_list
        new_letter_list.append(letter_list[0])
        #Recombine Each Letter List
        new_word = "".join(new_letter_list)
        #Create a List of Special Characters to Check Against
        special_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', '<', ',', '>', '.', '?', '/']
        #Check to See if 'Word' is Actually a Word or Instead, a Special Character
        if new_word in special_char_list:
            #Add 'ay' to the End of Each Word
            new_word_alt = new_word
        else:
            #Don't Modify Special Character
            new_word_alt = new_word + 'ay'
        #Append the Final Word into new_word_list
        new_word_list.append(new_word_alt)
        #print(new_word_list)
    #Recombine the Words in new_word_list into a New Sentence
    new_text = " ".join(new_word_list)
    print(new_text)
    #Return the New Sentence
    return new_text

pig_it('Pig latin is cool')
pig_it('This is my string')
pig_it("Quis custodiet ipsos custodes ?")