import sys
input=sys.stdin.readline

xbox=[1,0,-1,0]
ybox=[0,-1,0,1]

N=int(input())
line=[[False for i in range(101)]for j in range(101)]
for i in range(N):
  x,y,d,g=map(int,input().split())
  now=[d]
  for j in range(g):
    newArr=[]
    for k in range(len(now)-1,-1,-1):
      newArr.append((now[k]+1)%4)
    now+=newArr

  line[x][y]=True
  for j in range(len(now)):
    x+=xbox[now[j]]
    y+=ybox[now[j]]
    if 0<=x<=100 and 0<=y<=100:
      line[x][y]=True

answer=0
for i in range(100):
  for j in range(100):
    if line[i][j] and line[i+1][j] and line[i][j+1] and line[i+1][j+1]:
      answer+=1

print(answer)
