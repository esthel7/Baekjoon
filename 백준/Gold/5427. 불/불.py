import sys
input=sys.stdin.readline

def calculate(l,w,h,fires,person):
  xbox=[-1,1,0,0]
  ybox=[0,0,-1,1]
  cnt=0
  visit=[[False for i in range(w)]for j in range(h)]

  while True:
    newFires=[]
    while fires:
      [x,y]=fires.pop()
      if x<0 or y<0 or x>=h or y>=w:
        continue
      if l[x][y]=='#' or l[x][y]=='*':
        continue

      l[x][y]='*'
      for i in range(4):
        newFires.append((x+xbox[i],y+ybox[i]))

    newPerson=[]
    while person:
      [x,y]=person.pop()
      if x<0 or y<0 or x>=h or y>=w:
        print(cnt)
        return

      if l[x][y]=='#' or l[x][y]=='*' or visit[x][y]:
        continue

      visit[x][y]=True
      for i in range(4):
        newPerson.append((x+xbox[i],y+ybox[i]))

    if len(newPerson)==0:
      print('IMPOSSIBLE')
      return

    person=newPerson
    fires=newFires
    cnt+=1


def find(l,w,h):
  fires=[]
  person=[]
  for i in range(h):
    for j in range(w):
      if l[i][j]=='#' or l[i][j]=='.':
        continue
      elif l[i][j]=='*':
        l[i][j]='.'
        fires.append((i,j))
      else:
        l[i][j]='.'
        person.append((i,j))
  calculate(l,w,h,fires,person)

T=int(input())
for i in range(T):
  w,h=map(int,input().split())
  l=[]
  for j in range(h):
    l.append(list(input().rstrip()))
  find(l,w,h)
