import sys
input=sys.stdin.readline

# N은 가로, H는 세로

def check(l,cnt):
  global answer
  success=True
  for i in range(N):
    start=i
    for j in range(H):
      if l[j][start]:
        start+=1
      elif start-1>=0 and l[j][start-1]:
        start-=1
    if start!=i:
      success=False
      break

  if success:
    answer=cnt

def find(l,cnt,x,y):
  if answer!=-1 and answer<=cnt:
    return
  check(l,cnt)
  if cnt==3:
    return

  for i in range(x,H):
    if i==x:
      start=y
    else:
      start=0
    for j in range(start,N-1):
      if l[i][j] or (j-1>=0 and l[i][j-1]) or l[i][j+1]:
        continue
      l[i][j]=True
      find(l,cnt+1,i,j+1)
      l[i][j]=False


N,M,H=map(int,input().split())
l=[[False for i in range(N)]for j in range(H)]
for i in range(M):
  a,b=map(int,input().split())
  a-=1
  b-=1
  l[a][b]=True

answer=-1
find(l,0,0,0)
print(answer)
