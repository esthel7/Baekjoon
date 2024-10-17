import sys
input=sys.stdin.readline

N,M=map(int,input().split())

info={}
idx=[]
for i in range(N):
  name,num=input().rstrip().split()
  num=int(num)
  if num in info:
    continue
  info[num]=name
  idx.append(num)

Idx=len(idx)
for i in range(M):
  now=int(input())
  if now<=idx[0]:
    print(info[idx[0]])
    continue
  left=0
  right=Idx-1
  answer=''
  while left<=right:
    mid=(left+right)//2
    if now<=idx[mid]:
      answer=info[idx[mid]]
      right=mid-1
      continue
    else:
      left=mid+1
  print(answer)



