import sys
from collections import deque
input=sys.stdin.readline

N=int(input())

l=[]
for i in range(N):
  l.append(list(map(int,input().split())))
l.sort()

answer=0
total=deque([l[0]])
for i in range(1,N):
  if l[i][0]==total[0][0]:
    total[0][1]=l[i][1]
  elif l[i][0]<=total[0][1]:
    total[0][1]=max(total[0][1],l[i][1])
  else:
    answer+=total[0][1]-total[0][0]
    total.appendleft(l[i])

answer+=total[0][1]-total[0][0]
print(answer)
