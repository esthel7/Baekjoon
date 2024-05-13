import sys
input=sys.stdin.readline

# 첫째 날과 마지막 날에는 무조건 1cm

X,Y=map(int,input().split())
left=Y-X
half=left/2

if left==0:
  print(0)
  exit(0)
if left==1:
  print(1)
  exit(0)

start=1
while left:
  left-=start*2
  if left==0:
    print(start*2)
    exit(0)
  if left<=start+1:
    print(start*2+1)
    exit(0)
  if left>(start+1)*2:
    start+=1
    continue
  print(start*2+2)
  exit(0)

