def fib(index):
    if index > 0:
        x, y = 0, 1
        for i in range(index):
            x, y = y , y+x
        return (x)
