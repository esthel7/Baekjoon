from collections import deque

N,K=map(int,input().split())
l=[False for i in range(100001)]

if N<=K:
  q=deque([[N,0,[]]])
  while q:
    [N,time,num]=q.popleft()
    num=list(num)

    if N==K:
      num.append(N)
      print(time)
      for answer in num:
        print(answer,end=' ')
      break

    l[N]=True
    num.append(N)
    if N+1<100001 and not l[N+1]:
      q.append([N+1,time+1,num])
    if N-1>=0 and not l[N-1]:
      q.append([N-1,time+1,num])
    if N*2<100001 and not l[N*2]:
      q.append([N*2,time+1,num])

else:
  print(N-K)
  for answer in range(N,K-1,-1):
    print(answer,end=' ')
