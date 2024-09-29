import sys
input=sys.stdin.readline

def check():
  for tx, ty in teachers:
    for i in range(4):
      newX=tx+xbox[i]
      newY=ty+ybox[i]
      while True:
        if 0<=newX<N and 0<=newY<N:
          if l[newX][newY]=='S':
            return False
          elif l[newX][newY]=='X':
            newX+=xbox[i]
            newY+=ybox[i]
          else: # T, O
            break
        else:
          break
  print('YES')
  exit(0)

def find(x,y,cnt):
  if cnt<=3:
    check()
    if cnt==3:
      return
  for i in range(x,N):
    start=0
    if i==x:
      start=y
    for j in range(start,N):
      if possible[i][j]:
        empty=[]
        for key in possible[i][j].keys():
          if key in left:
            continue
          left[key]=True
          empty.append(key)
        if empty:
          l[i][j]='O'
          find(i,j+1,cnt+1)
          l[i][j]='X'
          for emptyKey in empty:
            left.pop(emptyKey)


N=int(input())
l=[]
teachers=[]
for i in range(N):
  now=list(input().rstrip().split())
  l.append(now)
  for j in range(N):
    if now[j]=='T':
      teachers.append([i,j])

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

possible=[[{} for i in range(N)]for j in range(N)]

for idx in range(len(teachers)):
  for i in range(4):
    cnt=1
    while True:
      newX=teachers[idx][0]+xbox[i]*cnt
      newY=teachers[idx][1]+ybox[i]*cnt
      if 0<=newX<N and 0<=newY<N:
        if l[newX][newY]=='T':
          break
        elif l[newX][newY]=='X':
          cnt+=1
        else:
          for j in range(cnt-1,0,-1):
            newX=teachers[idx][0]+xbox[i]*j
            newY=teachers[idx][1]+ybox[i]*j
            possible[newX][newY][idx*10+i+1]=True
          break
      else:
        break

left={}
find(0,0,0)
print('NO')
