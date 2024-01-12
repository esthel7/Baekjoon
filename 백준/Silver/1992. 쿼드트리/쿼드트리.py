import sys
input=sys.stdin.readline

def find(N,x,y):
  if N==1:
    print(l[x][y],end='')
    return

  first=l[x][y]
  breakFlag=False
  for i in range(x,x+N):
    for j in range(y,y+N):
      if first!=l[i][j]:
        breakFlag=True
        break
    if breakFlag:
      break
  if not breakFlag:
    print(l[x][y],end='')
    return

  newN=N//2
  print('(',end='')
  for i in range(4):
    find(newN,x+xbox[i]*newN,y+ybox[i]*newN)
  print(')',end='')

N=int(input())
l=[]
for i in range(N):
  l.append(list(input().rstrip()))
xbox=[0,0,1,1]
ybox=[0,1,0,1]

find(N,0,0)

