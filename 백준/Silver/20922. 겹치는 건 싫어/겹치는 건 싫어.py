import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())
l=list(map(int,input().split()))

info={}
q=deque([])
start=0
end=1

info[l[start]]=1
q.append(l[start])
answer=1
while end<N:
  if l[end] not in info:
    q.append(l[end])
    info[l[end]]=1
    end+=1
    answer=max(answer,end-start)
  else:
    if info[l[end]]<K:
      q.append(l[end])
      info[l[end]]+=1
      end+=1
      answer=max(answer,end-start)
    else:
      left=q.popleft()
      info[left]-=1
      if info[left]==0:
        info.pop(left)
      start+=1

print(answer)
