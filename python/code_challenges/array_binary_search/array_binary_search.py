import math

def BinarySearch(lis, key):
    start = 0
    last = len(lis)-1

    while last >= start:
        mid = start+(last-start)//2
        if lis[mid] == key:
            return mid
            break
        elif lis[mid] > key:
            last = mid -1
        else:
            start = mid +1
    else:
        return -1


