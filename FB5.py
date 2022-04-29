from collections import deque
def canGetExactChange(targetMoney, denominations):
  # Write your code here
  if targetMoney == 0:
    return True
  elif targetMoney < 0:
    return False
  res = False
  l = len(denominations)
  for i in range(l):
    if denominations[i] <= targetMoney:
       res = canGetExactChange(targetMoney-denominations[i], denominations) or canGetExactChange(targetMoney, denominations[i+1:])
    else:
       res = canGetExactChange(targetMoney, denominations[i+1:])
  return res

target = 94
arr= [5, 10, 25, 100, 200]

# k = canGetExactChange(target, arr)
# print(k)

def rotateU(arr):
  arr = deque(arr)
  for i in range(len(arr)):
    print(arr)
    arr.rotate(1)

def rotateU1(arr):
  l = len(arr)
  temp = arr[l-1]
  for i in range(l):
    print(arr)
    temp = arr[l-1]
    for j in range(l-1, -1, -1):
       if j == 0:
         arr[j] = temp
       else:
         arr[j] = arr[j-1]

arr = [1,2,3,4]
rotateU1(arr)

