import sys
from collections import deque
input=sys.stdin.readline

def find(n):
  for i in range(n):
    for j in range(3):
      for k in range(4):
        newX=i+xbox[k]
        newY=j+ybox[k]
        if 0>newX or newX>=n or 0>newY or newY>=3:
          continue
        if cost[newX][newY]==-1 or cost[newX][newY]>cost[i][j]+l[newX][newY]:
          cost[newX][newY]=cost[i][j]+l[newX][newY]

xbox=[0,1,1,1]
ybox=[1,-1,0,1]
test=0
while True:
  test+=1
  n=int(input())
  if n==0:
    break
  l=[]
  for i in range(n):
    l.append(list(map(int,input().split())))
  cost=[[-1 for i in range(3)]for j in range(n)]
  cost[0][0]=10000
  cost[0][1]=l[0][1]
  cost[0][2]=l[0][1]+l[0][2]

  find(n)
  print('%d. %d'%(test,cost[n-1][1]))
