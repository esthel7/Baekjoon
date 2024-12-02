import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  stick,n=map(int,input().split())

  fast=[]
  l=[]
  for i in range(n):
    now=int(input())
    fast.append(min(now,stick-now))
    l.append(now)
  fast=max(fast)
  l.sort()
  late=max(stick-l[0],l[-1])
  print(fast,late)
