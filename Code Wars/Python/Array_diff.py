def array_diff(a, b):
    #your code here
    #Learned About List Comprehensions at https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
    try:
        a = [i for i in a if i not in b]
    except Exception as e:
        print(e)
    return a

print("Basic Tests")
array_diff([1,2], [1])
array_diff([1,2,2], [1])
array_diff([1,2,2], [2])
array_diff([1,2,2], [])
array_diff([], [1,2])