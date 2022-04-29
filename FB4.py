def findEncryptedWord(s):
  # Write your code here
  s = encryptionUtil(s, 0, len(s)-1)
  return s

def encryptionUtil(s, start, end):
  if start == end or end == start+1:
     return s
  if len(s) %2 == 0:
    mid = start+((end-start)//2)
    l = encryptionUtil(s[start: mid], start, mid-1)
    r = encryptionUtil(s[mid+1:end+1], mid+1, end)
    return s[mid] + l + r
  else :
    mid = start+((end-start+1)//2)
    l = encryptionUtil(s[start: mid], start, mid - 1)
    r = encryptionUtil(s[mid+1:end+1], mid + 1, end)
    return s[mid] + l + r

ans = findEncryptedWord("abc")
print(ans)