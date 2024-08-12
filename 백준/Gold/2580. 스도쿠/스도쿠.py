import sys
input=sys.stdin.readline

def checkX(line,num):
  for i in range(9):
    if l[line][i]==num:
      return False
  return True


def checkY(line,num):
  for i in range(9):
    if l[i][line]==num:
      return False
  return True


def checkBox(x,y,num):
  for i in range(x,x+3):
    for j in range(y,y+3):
      if l[i][j]==num:
        return False
  return True


def fill(start):
  if start==Empty:
    for i in range(9):
      for j in range(9):
        print(l[i][j],end=' ')
      print()
    exit(0)

  x=empty[start][0]
  y=empty[start][1]
  for k in range(1,10):
    if checkX(x,k) and checkY(y,k) and checkBox(x//3*3,y//3*3,k):
      l[x][y]=k
      fill(start+1)
      l[x][y]=0


l=[]
for i in range(9):
  l.append(list(map(int,input().split())))

empty=[]
for i in range(9):
  for j in range(9):
    if l[i][j]==0:
      empty.append([i,j])

Empty=len(empty)
fill(0)
