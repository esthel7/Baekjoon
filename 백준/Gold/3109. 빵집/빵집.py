import sys
input=sys.stdin.readline

def find(x,y):
  global answer
  if y==C-1:
    answer+=1
    return True

  if x-1>=0 and l[x-1][y+1]!='x' and not visited[x-1][y+1]:
    visited[x-1][y+1]=True
    if find(x-1,y+1):
      return True
  if l[x][y+1]!='x' and not visited[x][y+1]:
    visited[x][y+1]=True
    if find(x,y+1):
      return True
  if x+1<R and l[x+1][y+1]!='x' and not visited[x+1][y+1]:
    visited[x+1][y+1]=True
    if find(x+1,y+1):
      return True
  return False


R,C=map(int,input().split())
l=[]
for i in range(R):
  l.append(list(input().rstrip()))

answer=0
visited=[[False for i in range(C)]for j in range(R)]
for i in range(R):
  visited[i][0]=True
  find(i,0)

print(answer)
