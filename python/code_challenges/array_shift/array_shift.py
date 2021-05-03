def insertShiftArray(list,value):
    """ this function will insert value in the middle of a list  """
    num = len(list)/2
    if not len(list)%2:
        list.insert(int(num), value)
    else:
        list.insert((int(num)+1), value)
    return list




