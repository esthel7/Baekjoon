import sys
input=sys.stdin.readline

# 4개이상 상하좌우 연결되면 없어짐

def makeList():
  for i in range(11,-1,-1):
    breakFlag=True
    for j in range(6):
      if first[i][j]=='.':
        continue
      breakFlag=False
      l[5-j][i]=first[i][j]
    if breakFlag:
      break


def find(x,y,color):
  q=[[x,y]]
  emptyFlag=True
  emptyBox=[]

  while q:
    [x,y]=q.pop()
    visit[x][y]=True

    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<6 and 0<=newY<12 and not visit[newX][newY] and color==l[newX][newY]:
        if emptyFlag:
          emptyBox.append([x,y])
          emptyFlag=False
        q.append([newX,newY])
        emptyBox.append([newX,newY])
        visit[newX][newY]=True
  
  if len(emptyBox)>=4:
    for [x,y] in emptyBox:
      empty.append([x,y])


def popEmpty():
  while empty:
    [x,y]=empty.pop()
    l[x].pop(y)
    l[x].insert(0,'.')


first=[]
for i in range(12):
  first.append(list(input().rstrip()))
l=[['.' for i in range(12)] for j in range(6)] # 오른쪽에 닿으면 빠짐
makeList()

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
total=0
while True:
  visit=[[False for i in range(12)]for j in range(6)]
  empty=[]
  for i in range(6):
    for j in range(11,-1,-1):
      if l[i][j]=='.':
        break
      if visit[i][j]:
        continue
      find(i,j,l[i][j])
  if len(empty)==0:
    break
  total+=1
  empty=sorted(empty, key=lambda x:x[1],reverse=True) # y 작은 순서대로 정렬
  popEmpty()

print(total)
