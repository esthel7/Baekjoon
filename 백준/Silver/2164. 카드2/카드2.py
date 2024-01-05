from collections import deque

N=int(input())
l=deque()
for i in range(1,N+1):
  l.append(i)

if N==1:
  print(l[0])
else:
  while True:
    f=l.popleft()
    if len(l)==1:
      print(l[0])
      break
    s=l.popleft()
    l.append(s)
