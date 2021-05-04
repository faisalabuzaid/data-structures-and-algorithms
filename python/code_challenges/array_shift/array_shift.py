import math

def insertShiftArray(list,value):
    """ this function will insert value in the middle of a list  """
    sub_arr = list[:math.ceil(len(list)/2)] + [value] + list[math.ceil(len(list)/2):]
    return sub_arr
