import sys
input=sys.stdin.readline

def sky(x,y):
  # -
  first=0
  if y+3<M:
    for i in range(y,y+4):
      first+=l[x][i]
  # ㅣ
  second=0
  if x+3<N:
    for i in range(x,x+4):
      second+=l[i][y]
  return max(first,second)

def yellow(x,y):
  if x+1<N and y+1<M:
    return l[x][y]+l[x+1][y]+l[x][y+1]+l[x+1][y+1]
  return 0

def group3(x,y):
  # 3*2
  first=0
  if x+2<N and y+1<M:
    base=0
    for i in range(x,x+3):
      for j in range(y,y+2):
        base+=l[i][j]
    Min=min(l[x][y+1]+l[x+1][y+1],l[x+1][y+1]+l[x+2][y+1],l[x][y]+l[x+1][y],l[x+1][y]+l[x+2][y],
            l[x][y+1]+l[x+2][y],l[x][y]+l[x+2][y+1],
            l[x][y+1]+l[x+2][y+1],l[x][y]+l[x+2][y])
    first=base-Min

  # 2*3
  second=0
  if x+1<N and y+2<M:
    base=0
    for i in range(x,x+2):
      for j in range(y,y+3):
        base+=l[i][j]
    Min=min(l[x+1][y+1]+l[x+1][y+2],l[x+1][y]+l[x+1][y+1],l[x][y+1]+l[x][y+2],l[x][y]+l[x][y+1],
            l[x][y]+l[x+1][y+2],l[x][y+2]+l[x+1][y],
            l[x+1][y]+l[x+1][y+2],l[x][y]+l[x][y+2])
    second=base-Min

  return max(first,second)

N,M=map(int,input().split())
answer=0
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

for i in range(N):
  for j in range(M):
    value=max(sky(i,j),yellow(i,j),group3(i,j))
    if answer<value:
      answer=value
print(answer)
