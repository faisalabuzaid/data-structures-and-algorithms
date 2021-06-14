# Merge sort algorithms

**`We have this list [4, 1, 5, 3, 9]`**

```
step1:

[4, 1, 5, 3, 9]

"mid = 2"

divided into:

[4,1,5] and [3,9]


step2:

[4, 1, 5]

mid = 2

divided into:

[4, 1] and [5]

step3:

[4, 1]

mid = 1

divided into:
[4] amd [1]

step4:
 compare if 1 < 4  then left[0] will be 1
 and left[1] = 4

 left will be after merge [1, 4]

 step4:

left [1, 4] , right [5]

after merge left now is [1, 4, 5]

step5:
right [3, 9]
left [3] and right [9]
after merge right [3, 9]

step6
left [1, 4, 5]
right [3, 9]

after merge 
[1, 3, 4, 5, 9]
