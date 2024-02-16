import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

if l[0]>0:
  print(l[0],l[1])
  exit(0)
if l[-1]<0:
  print(l[-2],l[-1])
  exit(0)

start=0
end=N-1
answer=[2000000000,-1,-1]
while start<end:
  if l[start]+l[end]<0:
    now=abs(l[start]+l[end])
    if now<answer[0]:
      answer=[now,start,end]
    start+=1
  elif l[start]+l[end]==0:
    answer=[0,start,end]
    break
  else:
    now=abs(l[start]+l[end])
    if now<answer[0]:
      answer=[now,start,end]
    end-=1

print(l[answer[1]],l[answer[2]])
