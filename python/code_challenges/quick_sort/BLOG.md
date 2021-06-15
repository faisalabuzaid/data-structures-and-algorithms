# Quick sort algorithms

**`We have this list [10, 7, 8, 9, 1, 5]`**


step1:

arr = [10, 7, 8, 9, 1, 5]

left =0

right = 5

pivot = 5

loop from 0 to 4

j | i 
---|---
0 | -1
1 | -1
2 | -1
3 | -1
4 | 0

i=0
[1, 7, 8, 9, 10, 5]

[1, 5, 8, 9, 10, 7]

return "1" from partition


step2:

position = 1

arr = [1, 5, 8, 9, 10, 7]

left = 2

right = 5

j | i 
---|---
2 | 1
3 | 1
4 | 1

arr = [1, 5, 7, 9, 10, 8]

return 2 

step3:

arr = [1, 5, 7, 9, 10, 8]

left = 3

right = 5

j | i 
---|---
3 | 2
4 | 2

arr = [1, 5, 7, 8, 10, 9]

return 3

left =4
right =5

j | i 
---|---
4 | 3

arr = [1, 5, 7, 8, 9, 10]

return 4





