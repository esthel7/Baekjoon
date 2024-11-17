import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x,y):
  global answer
  if visited[x][y]!=0:
    return visited[x][y]
  visited[x][y]=1
  for i in range(4):
    newX=x+xbox[i]
    newY=y+ybox[i]
    if 0<=newX<n and 0<=newY<n and l[x][y]<l[newX][newY]:
      visited[x][y]=max(visited[x][y],find(newX,newY)+1)
  if answer<visited[x][y]:
    answer=visited[x][y]
  return visited[x][y]


n=int(input())
l=[]
for i in range(n):
  l.append(list(map(int,input().split())))

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

visited=[[0 for i in range(n)]for j in range(n)]
answer=0
for i in range(n):
  for j in range(n):
    if visited[i][j]==0:
      find(i,j)

print(answer)
