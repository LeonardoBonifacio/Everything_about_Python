from random import randint
import time
# Implementation of binary search algorithm!

# We will prove that binary search is faster than naive search!

# Naive search: scan entire list and ask if its equal to the target
# If yes, return the index
# If no, then return -1

def naive_search(lista, target):
    # example lista = [1, 3, 10, 12]
    for i in range(len(lista)):
        if(lista[i] == target):
            return i
    return -1


# binary serach uses divide and conquer!
# we will leverage the fact that our list SORTED

def binary_search(lista, target, low=None, high=None):
    if(low is None):
        low = 0
    if(high is None):
        high = len(lista) - 1
    if(high < low):
        return -1

    # example lista = [1, 3, 5, 10, 12] #Should return 3  because us were looking 10
    midpoint = (low + high) // 2 # 2

    if(lista[midpoint] == target):
        return midpoint
    elif(target < lista[midpoint]):
        return binary_search(lista, target, low, midpoint - 1)
    else:
        # target > lista[midpoint]
        return binary_search(lista, target, midpoint + 1, high)


if __name__ == '__main__':
    '''lista = [1, 3, 7, 10, 12]
    target = 10
    print(naive_search(lista,target))
    print(binary_search(lista,target))'''

    lenght = 10000
    # build a sorted list of lenght 10000
    sorted_list = set()
    while(len(sorted_list) < lenght):
        sorted_list.add(randint(-3 * lenght, 3 * lenght))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end = time.time()
    print(f"Naive search time: {(end - start)} seconds")
 
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()
    print(f"Binary search time: {(end - start)} seconds")