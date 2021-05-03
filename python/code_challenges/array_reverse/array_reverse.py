user_array=list(input().split(","))
result = []

def reverseArray(list):
  for i in range(len(list)):
    result.insert(0, list.pop(0))
  return(result)

print(reverseArray(user_array))