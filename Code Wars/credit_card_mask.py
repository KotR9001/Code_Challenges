# return masked string
def maskify(cc):
    cc_digits = []
    for digit in cc:
        cc_digits.append(digit)
    pass
    #print(cc_digits[-1])
    cc_digits1 = ['#' for i in range(len(cc_digits)) if i not in range(-4, 0)]

    separator = ""
    return separator.join(cc_digits1)
    

cc = ''
print(maskify(cc))

cc = '123'
print(maskify(cc))

cc = 'SF$SDfgsd2eA'
print(maskify(cc))