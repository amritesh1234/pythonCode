def getMilestoneDays(revenues, milestones):
  # Write your code here
  res = []
  currRev = 0
  mc = 0
  for i,rev in enumerate(revenues):
    currRev+=rev
    while mc < len(milestones) and currRev >= milestones[mc]:
      res.append(i+1)
      mc+=1
  return res

revenues = [100, 200, 300, 400, 500]
milestones = [300, 800, 1000, 1400]

k = getMilestoneDays(revenues, milestones)
print(k)
