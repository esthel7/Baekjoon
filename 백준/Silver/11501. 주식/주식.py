import sys
from collections import deque
input=sys.stdin.readline

def find(N):
  money=0
  count=0
  for i in range(N):
    if Max[0]==l[i]:
      money+=count*l[i]
      count=0
      # if i+1<N and l[i+1]==l[i]:
      #   continue
      Max.popleft()
    else:
      count+=1
      money-=l[i]
  print(money)


def make(N):
  Max=deque([])
  Max.append(l[0])
  for i in range(1,N):
    if l[i]>=Max[-1]:
      while len(Max)>0 and l[i]>Max[-1]:
        Max.pop()
      Max.append(l[i])
    else:
      Max.append(l[i])
  return Max


T=int(input())
for i in range(T):
  N=int(input())
  l=list(map(int,input().split()))
  reverseL=sorted(l,reverse=True)
  MaxBox=deque(reverseL)
  Max=make(N)
  find(N)
