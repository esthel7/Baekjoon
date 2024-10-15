import sys
import heapq
input=sys.stdin.readline

N=int(input())
q=[]
for i in range(N):
  L,H=map(int,input().split()) # 위치, 높이
  heapq.heappush(q,[-H,L])

s=[0 for i in range(1001)]
h,l=heapq.heappop(q)
h*=(-1)
s[l]=h

left=l
right=l
mid=l

while q:
  h,l=heapq.heappop(q)
  h*=(-1)
  if s[l]>h:
    continue
  if l<left:
    s[l]=h
    left=l
    for i in range(left+1,mid):
      if s[i]<h:
        s[i]=h
      else:
        break
  elif right<l:
    s[l]=h
    right=l
    for i in range(right-1,mid,-1):
      if s[i]<h:
        s[i]=h
      else:
        break
  elif left<l<mid:
    for i in range(l,mid):
      if s[i]<h:
        s[i]=h
      else:
        break
  elif mid<l<right:
    for i in range(l,mid,-1):
      if s[i]<h:
        s[i]=h
      else:
        break

print(sum(s))
