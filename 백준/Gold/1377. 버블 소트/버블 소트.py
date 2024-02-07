import sys
input=sys.stdin.readline

N=int(input())
l=[]
sortL=[]

for i in range(N):
  a=int(input())
  l.append([a,i])
  sortL.append([a,i])

sortL.sort()

Max=1
for i in range(N):
  now=sortL[i][1]-l[i][1]+1
  if Max<now:
    Max=now

print(Max)

