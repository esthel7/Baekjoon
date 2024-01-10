import sys
input=sys.stdin.readline

def find(x,y,n,m):
  xbox=[-1,1,0,0]
  ybox=[0,0,-1,1]
  cnt=0
  q=[[x,y]]
  while q:
    [x,y]=q.pop()
    if 0<=x<n and 0<=y<m:
      if l[x][y]==1:
        cnt+=1
        l[x][y]=0
        for i in range(4):
          q.append([x+xbox[i],y+ybox[i]])
  return cnt

n,m=map(int,input().split())
l=[]
for i in range(n):
  l.append(list(map(int,input().split())))

cnt=0
maximum=0
for i in range(n):
  for j in range(m):
    if l[i][j]==1:
      value=find(i,j,n,m)
      cnt+=1
      if maximum<value:
        maximum=value
print(cnt)
print(maximum)
