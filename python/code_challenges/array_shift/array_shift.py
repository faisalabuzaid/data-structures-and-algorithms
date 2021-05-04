def insertShiftArray(list,value):
    """ this function will insert value in the middle of a list  """
    result = []
    if not len(list)%2:
        num=int(len(list)/2)
    else:
        num=int(len(list)/2) + 1

    for item in list:
        if len(result) < num  :
            result.append(item)
        elif len(result) == num:
            result.append(value)
            result.append(item)
        else:
            result.append(item)
    return result