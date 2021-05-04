def BinarySearch(list, key):
    result=-1
    count=0
    for item in list:
        count+=1
        if not key:
            result=item
            break
        elif key < len(list) and key > -1:
            result = item
            if key==(count-1):
                break
    return result

