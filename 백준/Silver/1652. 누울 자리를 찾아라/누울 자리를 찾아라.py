import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(input().rstrip()))

x=0
for i in range(N):
  cnt=0
  for j in range(N):
    if l[i][j]=='X':
      if cnt>=2:
        x+=1
      cnt=0
    else:
      cnt+=1
  if cnt>=2:
    x+=1

y=0
for i in range(N):
  cnt=0
  for j in range(N):
    if l[j][i]=='X':
      if cnt>=2:
        y+=1
      cnt=0
    else:
      cnt+=1
  if cnt>=2:
    y+=1

print(x,y)
