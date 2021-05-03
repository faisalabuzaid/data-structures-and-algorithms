user_array=list(input().split(","))
result = []

def reverseArray(list):
  result = user_array[::-1]
  return(result)

print(reverseArray(user_array))