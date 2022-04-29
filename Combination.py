arr = [1,2,3]

def combination(arr, index, length, resarr):
    if index == length:
        print(resarr)
        return
    resarr.append(arr[index])
    combination(arr, index+1, length, resarr)
    resarr.pop()
    combination(arr, index+1, length, resarr)


def combination2(arr, index, length, resarr):
    print(resarr)
    for i in range(index, length):
        resarr.append(arr[i])
        combination2(arr, i+1, length, resarr)
        resarr.pop()
        # combination2(arr, index+1, length, resarr)


def permute(arr, length, resarr, used):
    if len(resarr) == length:
      print(resarr)
      # return
    for i in range(0, length):
        if not used[i] :
          resarr.append(arr[i])
          used[i] = True
          permute(arr, length, resarr, used)
          resarr.pop()
          used[i] = False


resarr = []
combination(arr, 0, 3, resarr)
# used = [False] * 3
# permute(arr, 3, resarr, used)

a


