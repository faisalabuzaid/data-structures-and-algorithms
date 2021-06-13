def sort(lst):
    n = len(lst)
    dic = {}
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if lst[j] < lst[i]:
                min = j

        temp = lst[min]
        lst[min] = lst[i]
        lst[i] = temp

