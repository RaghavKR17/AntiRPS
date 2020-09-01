f = open("anti-rps.txt")
xlist = []
xlist2 = []
ans = ""
for i in range(11):
  x = f.read(1)
  xlist.append(x)
for i in range(len(xlist)):
  if "R" in xlist[i]:
    xlist2.append("S")
  if "P" in xlist[i]:
    xlist2.append("R")
  if "S" in xlist[i]:
    xlist2.append("P")
for i in range(len(xlist2)):
  ans = ans + (xlist2[i])
print(ans)          
