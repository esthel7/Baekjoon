import sys
import heapq
input=sys.stdin.readline

T=int(input())
plus60=0
plus10=1
minus10=2
plus1=3
minus1=4
for i in range(T):
  N=int(input())
  value=N//60
  l=[0 for j in range(5)]
  l[0]+=N//60
  N%=60
  if N==0:
    print(*l)
    continue

  q=[]
  l[plus60]+=1
  heapq.heappush(q,[1,list(l),N-60,plus60+1])
  l[plus60]-=1
  value=N//10
  l[plus10]+=value
  heapq.heappush(q,[value,list(l),N-(10*value),plus10+1])
  l[plus10]-=value
  l[plus10]+=value+1
  heapq.heappush(q,[value+1,list(l),N-(10*(value+1)),plus10+1])
  l[plus10]-=value+1
  l[plus1]+=N
  heapq.heappush(q,[N,list(l),0,plus1+1])
  
  while q:
    cnt,l,left,after=heapq.heappop(q)
    if left==0:
      print(*l)
      break
    if left<0:
      now=left*(-1)
      value=now//10
      if value!=0:
        l[minus10]+=value
        heapq.heappush(q,[cnt+value,list(l),left+10*value,minus10+1])
        l[minus10]-=value
      l[minus10]+=value+1
      heapq.heappush(q,[cnt+value+1,list(l),left+10*(value+1),minus10+1])
      l[minus10]-=value+1
      l[minus1]+=now
      heapq.heappush(q,[cnt+now,list(l),0,minus1+1])
      continue
    if after<=plus10 and left>=6:
      value=left//10
      if value!=0:
        l[plus10]+=value
        heapq.heappush(q,[cnt+value,list(l),left-(10*value),plus10+1])
        l[plus10]-=value
      l[plus10]+=value+1
      heapq.heappush(q,[cnt+value+1,list(l),left-(10*(value+1)),plus10+1])
      l[plus10]-=value+1
    if after<=plus1:
      l[plus1]+=left
      heapq.heappush(q,[cnt+left,list(l),0,plus1+1])
      l[plus1]-=left
