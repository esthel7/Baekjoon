import sys
input=sys.stdin.readline

N=int(input())

for i in range(N):
  now=list(map(int,input().split()))

  if i==0:
    bp=now
    sp=now
    continue

  bp=[now[0]+max(bp[0],bp[1]),now[1]+max(bp[0],bp[1],bp[2]),now[2]+max(bp[1],bp[2])]
  sp=[now[0]+min(sp[0],sp[1]),now[1]+min(sp[0],sp[1],sp[2]),now[2]+min(sp[1],sp[2])]

print(max(bp),min(sp))
