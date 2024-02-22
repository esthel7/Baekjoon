import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

answer=0
end=0
info={}
now=deque([])
while end!=N:
  if l[end] not in info.keys() or not info[l[end]]:
    now.append(l[end])
    info[l[end]]=True
    answer+=len(now)
    end+=1
  else:
    while True:
      left=now.popleft()
      info[left]=False
      if left==l[end]:
        break
    now.append(l[end])
    info[l[end]]=True
    answer+=len(now)
    end+=1

print(answer)
