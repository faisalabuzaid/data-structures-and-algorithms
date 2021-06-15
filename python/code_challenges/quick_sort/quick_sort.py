
def quick_sort(arr, left, right):
    if len(arr) == 1:
        return arr
    if left < right:

        position = partition(arr, left, right)

        quick_sort(arr, left, position-1)
        quick_sort(arr, position+1, right)

def partition(arr, left, right):
    i = (left-1)
    pivot = arr[right]
  
    for j in range(left, right):
  
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return (i+1)
  

