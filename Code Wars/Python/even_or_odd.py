def even_or_odd(s):
    #Split Digits
    digit_list = list(s)

    #Convert Digits to Integers
    for element in range(len(digit_list)):
        digit_list[element] = int(digit_list[element])
    #print(digit_list)

    #Create Even & Odd Element
    even_list = []
    odd_list = []

    #Loop Through Digits and Assign Them to their Respective Lists
    for digit in digit_list:
        if digit %2 == 0:
            even_list.append(digit)
        else:
            odd_list.append(digit)

    #Initialize the Sum of the Even & Odd Lists
    even_sum = 0
    odd_sum = 0

    #Compute the Sum of the Even & Odd Lists
    for digit in even_list:
        even_sum = even_sum + digit

    for digit in odd_list:
        odd_sum = odd_sum + digit

    #Compare the Sums
    if even_sum > odd_sum:
        message = 'Even is greater than Odd'
    if even_sum < odd_sum:
        message = 'Odd is greater than Even'
    if even_sum == odd_sum:
        message = 'Even and Odd are the same'
    return message

even_or_odd('12')
even_or_odd('123')
even_or_odd('112')