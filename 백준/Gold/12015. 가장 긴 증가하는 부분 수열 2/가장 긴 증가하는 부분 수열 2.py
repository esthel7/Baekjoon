import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

rank=[]
for item in l:
  if not rank or rank[-1]<item:
    rank.append(item)
    continue
  if rank[-1]==item:
    continue

  left=0
  right=len(rank)-1
  while left<=right:
    mid=(left+right)//2
    if mid==0:
      if rank[mid]>=item:
        rank[mid]=item
      elif right>=1 and rank[mid+1]>=item:
        rank[mid+1]=item
      break
    if rank[mid]==item:
      break
    elif rank[mid]<item:
      if rank[mid+1]>=item:
        rank[mid+1]=item
        break
      left=mid+1
    else:
      if rank[mid-1]<item:
        rank[mid]=item
        break
      right=mid-1

print(len(rank))

"""
6
10 60 10 30 20 50
1  2  1  2  2   3

7
1 10 20 2 3 4 5
1 2  3  2 3 4 5
"""
