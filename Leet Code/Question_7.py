def reverse1(number):
    string = str(number)
    digits = list(string)
    rev = reversed(digits)
    new_num = "".join(rev)
    new_int = int(new_num)
    return new_int

reverse1(234)