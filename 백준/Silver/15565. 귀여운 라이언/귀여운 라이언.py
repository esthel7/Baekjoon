import sys
input=sys.stdin.readline

N,K=map(int,input().split())
l=list(map(int,input().split()))

start=0
while start<N:
  if l[start]==1:
    end=start+1
    cnt=1
    break
  start+=1

if start==N:
  print(-1)
  exit(0)
if K==1:
  print(1)
  exit(0)

answer=N+1
while end<N:
  if cnt==K:
    answer=min(answer,end-start)
    start+=1
    cnt-=1
    while start<=end:
      if l[start]==1:
        if end==start:
          end=start+1
          if end<N and l[end]==1:
            cnt+=1
        break
      start+=1
    continue
  if l[end]==1:
    cnt+=1
    end+=1
  else:
    end+=1

if cnt==K:
  answer=min(answer,end-start)

if answer==N+1:
  print(-1)
else:
  print(answer)
