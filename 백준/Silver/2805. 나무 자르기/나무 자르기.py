import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=list(map(int,input().split()))
start=0
end=2000000000
answer=0
while start<=end:
  mid=(start+end)//2
  cnt=0
  for tree in l:
    if tree>mid:
      cnt+=tree-mid
  if cnt>=M:
    answer=mid
    start=mid+1
  else:
    end=mid-1
print(answer)
