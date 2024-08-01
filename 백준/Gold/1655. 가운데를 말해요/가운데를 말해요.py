import sys
import heapq
input=sys.stdin.readline

def make(a):
  global mid, Left, Right
  if a<mid:
    Left+=1
    heapq.heappush(left,-a)
    if Left>Right:
      heapq.heappush(right,mid)
      mid=heapq.heappop(left)*(-1)
      Right+=1
      Left-=1
  else: # a>=mid
    Right+=1
    heapq.heappush(right,a)
    if Right>Left+1:
      heapq.heappush(left,-mid)
      mid=heapq.heappop(right)
      Left+=1
      Right-=1

N=int(input())
left=[]
right=[]
Left=0
Right=0
mid=int(input())
# print('answer',mid,left,right)
print(mid)
for i in range(1,N):
  a=int(input())
  make(a)
  # print('answer',mid,left,right)
  print(mid)
