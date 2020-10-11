import itertools
import operator

def product_sum(a, m):
    #Initialize the Product Sum
    product_sum = 0
    #Loop Through the Indices of Every Combination
    #Method Found at https://stackoverflow.com/questions/30820997/efficient-pythonic-way-of-finding-all-possible-sublists-of-a-list-in-given-ran
    subsequence_list = [list(listy) for listy in itertools.combinations(a, m)]
    print(f"The subsequence list is: {subsequence_list}")
    #[print(f"The listy_sliced is: {listy_sliced}") for listy_sliced in subsequence_list]
    for listy_sliced in subsequence_list:
        for l in range(len(listy_sliced)):
            if l == 0:
                subsequence = listy_sliced[l]
                #print(f"The subsequence is: {subsequence}")
            if l > 0:
                subsequence = listy_sliced[l] * subsequence
                #print(f"The subsequence is: {subsequence}")
        product_sum = subsequence + product_sum
    product_sum = [map(itertools.accumulate, listy_sliced[l]) for listy_sliced in subsequence_list for l in range(len(listy_sliced))]
    print(f"The product sum is: {product_sum}")
    return product_sum

tc = [
    ([2,3, 4, 5],3, 154 ),
    ([1, 2, 3], 2, 11),
    ([5, 7, 2, 3], 3, 247),
    ([3,10,7,9,1,4,5,2,8,6], 7, 8409500),
    ([10,7,8,5,6,9,4,1,2,3], 8, 12753576),
    ([1,7,6,10,21,5,9,8,5,4], 2, 2469),
    ([6,7,8,5,2,4,9,3,1,10], 6, 3416930),
    ([3,2,9,1,7,10,5,6,8,4], 4, 157773),
    ([9,8,10,4,2,7,5,1,3,6], 3, 18150),
    ([3,3,1,7,6,8,1,4,6,10], 4, 94837),
    ([6,8,1,7,2,10,5,9,3,4], 5, 902055),
    ([10,3,4,9,5,8,6,7,1,2], 1, 55),
    ([7,9,4,2,3,10,8,6,5,1], 9, 10628640)
]

for arr, m, res in tc:
    product_sum(arr,m)