import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

answer=[0]
s=deque([[l[0],0]]) # 0번이 가장 큰 값
for i in range(1,N):
  if l[i]>=s[0][0]:
    s=deque([[l[i],i]])
    answer.append(0)
  else:
    while s:
      last=s.pop()
      if last[0]<=l[i]:
        continue
      else:
        answer.append(last[1]+1)
        s.append(last)
        s.append([l[i],i])
        break

for i in range(N):
  print(answer[i],end=' ')

