prime_list = ["2", "&"]
non_prime_list = []

bool_list_list = []
for num in range(2, 100):
    bool_list = []
    for num1 in range(2, 100):
        while num1 < num:
            #print(f"num: {num}, num1: {num1}, mod: {num % num1}")
            if num % num1 == 0:
                bool_list.append(True)
            else:
                bool_list.append(False)
            num1 += 1
    #print(f"bool_list: {bool_list}")
    bool_list_list.append(bool_list)
#print(f"bool_list_list: {bool_list_list}")

for listy in range(1, len(bool_list_list)):
    #print(f"bool_list_list[listy]: {bool_list_list[listy]}")
    if any(bool_list_list[listy]) == True:
        non_prime_list.append(str(listy+2))
    else:
        prime_list.append(str(listy+2))
        prime_list.append("&")
    num1 += 1
prime_list.pop(-1)
print(f"prime_list: {prime_list}")
prime_string = "".join(prime_list)
print(f"prime_string: {prime_string}")