from collections import deque

n,w,L=map(int,input().split())
l=list(map(int,input().split()))

# 길이 w, 최대하중 L
# 다 건넌 시간 출력

now=deque([0 for i in range(w)])
now[0]=l[0]
q=deque([[1,now,1,l[0]]])
answer=0
while q:
  [idx,now,time,total]=q.popleft()
  if idx==n:
    if total!=0:
      while total!=0:
        left=now.pop()
        total-=left
        time+=1
    answer=time
    break

  left=now.pop()
  total-=left
  if total+l[idx]<=L:
    now.appendleft(l[idx])
    q.append([idx+1,now,time+1,total+l[idx]])
  else:
    now.appendleft(0)
    q.append([idx,now,time+1,total])

print(answer)
