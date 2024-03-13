import sys
input=sys.stdin.readline

def find(x,y,cnt):
  global answer
  if answer<cnt:
    answer=cnt
  for i in range(4):
    newX=x+box[i][0]
    newY=y+box[i][1]
    if 0<=newX<R and 0<=newY<C and l[newX][newY] not in info:
      info.add(l[newX][newY])
      find(newX,newY,cnt+1)
      info.remove(l[newX][newY])


R,C=map(int,input().split())
l=[]
for i in range(R):
  l.append(list(input().rstrip()))

box=((-1,0),(1,0),(0,-1),(0,1))
answer=1
info=set()
info.add(l[0][0])
find(0,0,1)

print(answer)
