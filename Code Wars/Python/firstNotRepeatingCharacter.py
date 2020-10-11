def firstNotRepeatingCharacter(s):
    string_list = list(s)
    
    unique_list = []
    #for letter in string_list:
        #letter_count = string_list.count(letter)
        #if letter_count == 1:
            #unique_list.append(letter)
        #else:
            #unique_list.append('_')
    unique_list = [unique_list.append(letter) if string_list.count(letter) == 1 else unique_list.append('_') for letter in string_list]
            
    unique_char_list = []
    #for char in unique_list:
        #if char != '_':
            #unique_char_list.append(char)
    unique_char_list = [unique_char_list.append(char) for char in unique_list if char != '_']
            
    if unique_char_list == []:
        unique_char_list = ["_"]
            
    return unique_char_list[0]