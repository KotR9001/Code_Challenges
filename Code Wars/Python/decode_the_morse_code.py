def decodeMorse(morse_code):
    # Dictionary representing the morse code chart
    # Found at https://www.geeksforgeeks.org/morse-code-translator-python/ 
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                        'C':'-.-.', 'D':'-..', 'E':'.', 
                        'F':'..-.', 'G':'--.', 'H':'....', 
                        'I':'..', 'J':'.---', 'K':'-.-', 
                        'L':'.-..', 'M':'--', 'N':'-.', 
                        'O':'---', 'P':'.--.', 'Q':'--.-', 
                        'R':'.-.', 'S':'...', 'T':'-', 
                        'U':'..-', 'V':'...-', 'W':'.--', 
                        'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                        '1':'.----', '2':'..---', '3':'...--', 
                        '4':'....-', '5':'.....', '6':'-....', 
                        '7':'--...', '8':'---..', '9':'----.', 
                        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                        '?':'..--..', '/':'-..-.', '-':'-....-', 
                        '(':'-.--.', ')':'-.--.-'}
    #MORSE_CODE['.--'] = morse_code
    phrase = [MORSE_CODE_DICT.keys() for MORSE_CODE_DICT.values() in morse_code]             
    return print(phrase.replace('.', MORSE_CODE_DICT['.']).replace('-', MORSE_CODE_DICT['-']).replace(' ', ''))

decodeMorse('.... . -.--   .--- ..- -.. .')