import sys
input=sys.stdin.readline

Top=0
Bottom=1
Left=2
Right=3

def block(now,dir):
  if dir==Top:
    if now=='|' or now=='+':
      return Top
    elif now=='1':
      return Right
    elif now=='4':
      return Left
  elif dir==Bottom:
    if now=='|' or now=='+':
      return Bottom
    elif now=='2':
      return Right
    elif now=='3':
      return Left
  elif dir==Left:
    if now=='-' or now=='+':
      return Left
    elif now=='1':
      return Bottom
    elif now=='2':
      return Top
  else: # Right
    if now=='-' or now=='+':
      return Right
    elif now=='3':
      return Top
    elif now=='4':
      return Bottom
  return -1

def dirCheck(now,dir):
  if now=='|':
    if dir in [Top,Bottom]:
      return True
  elif now=='-':
    if dir in [Left,Right]:
      return True
  elif now=='+':
    return True
  elif now=='1':
    if dir in [Top,Left]:
      return True
  elif now=='2':
    if dir in [Bottom,Right]:
      return True
  elif now=='3':
    if dir in [Bottom,Right]:
      return True
  elif now=='4':
    if dir in [Right,Top]:
      return True
  return False


R,C=map(int,input().split())
l=[]
startx=0
starty=0
endx=0
endy=0
for i in range(R):
  now=list(input().rstrip())
  l.append(now)
  for j in range(C):
    if now[j]=='M':
      startx=i
      starty=j
    elif now[j]=='Z':
      endx=i
      endy=j

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

startDir=-1

q=[]
for i in range(4):
  nextx=startx+xbox[i]
  nexty=starty+ybox[i]
  if 0<=nextx<R and 0<=nexty<C and l[nextx][nexty]!='.':
    startDir=block(l[nextx][nexty],i)
    if startDir!=-1:
      if startDir==Top:
        q.append([nextx-1,nexty,startDir])
      elif startDir==Bottom:
        q.append([nextx+1,nexty,startDir])
      elif startDir==Left:
        q.append([nextx,nexty-1,startDir])
      else: # Right
        q.append([nextx,nexty+1,startDir])
      break

if startDir==-1: # 시작 주위에서 없어짐
  l[startx][starty]='Z'
  l[endx][endy]='M'
  cntx=startx
  cnty=starty
  startx=endx
  starty=endy
  endx=cntx
  endy=cnty

  for i in range(4):
    nextx=startx+xbox[i]
    nexty=starty+ybox[i]
    if 0<=nextx<R and 0<=nexty<C and l[nextx][nexty]!='.':
      startDir=block(l[nextx][nexty],i)
      if startDir!=-1:
        if startDir==Top:
          q.append([nextx-1,nexty,startDir])
        elif startDir==Bottom:
          q.append([nextx+1,nexty,startDir])
        elif startDir==Left:
          q.append([nextx,nexty-1,startDir])
        else: # Right
          q.append([nextx,nexty+1,startDir])
        break

while q:
  x,y,dir=q.pop()
  if l[x][y]=='.': # 빈칸
    if dir==Top:
      if x-1>=0 and y+1<C and y-1>=0 and dirCheck(l[x-1][y],Top) and ((dirCheck(l[x][y+1],Right) and dirCheck(l[x][y-1],Left))or (dirCheck(l[x][y+1],Left) and dirCheck(l[x][y-1],Right))):
        print(x+1,y+1,'+')
      elif x-1>=0 and l[x-1][y] in ['|','+','1','4','M']:
        print(x+1,y+1,'|')
      elif y+1<C and l[x][y+1] in ['-','+','3','4','M']:
        print(x+1,y+1,'1')
      elif x+1<R and l[x+1][y] in ['|','+','2','3','M']:
        print(x+1,y+1,'4')
    elif dir==Bottom:
      if x+1<R and y+1<C and y-1>=0 and dirCheck(l[x+1][y],Bottom) and ((dirCheck(l[x][y+1],Right) and dirCheck(l[x][y-1],Left)) or (dirCheck(l[x][y+1],Left) and dirCheck(l[x][y-1],Right))):
        print(x+1,y+1,'+')
      elif x+1<R and l[x+1][y] in ['|','+','2','3','M']:
        print(x+1,y+1,'|')
      elif y+1<C and l[x][y+1] in ['-','+','3','4','M']:
        print(x+1,y+1,'2')
      elif y-1>=0 and l[x][y-1] in ['-','+','1','2','M']:
        print(x+1,y+1,'3')
    elif dir==Left:
      if y-1>=0 and x-1>=0 and x+1<R and dirCheck(l[x][y-1],Left) and ((dirCheck(l[x-1][y],Top) and dirCheck(l[x+1][y],Bottom)) or (dirCheck(l[x-1][y],Bottom) and dirCheck(l[x+1][y],Top))):
        print(x+1,y+1,'+')
      elif y-1>=0 and l[x][y-1] in ['-','+','1','2','M']:
        print(x+1,y+1,'-')
      elif x+1<R and l[x+1][y] in ['|','+','2','3','M']:
        print(x+1,y+1,'1')
      elif y+1<C and l[x][y+1] in ['-','+','3','4','M']:
        print(x+1,y+1,'2')
    else: # Right
      if y+1<C and x-1>=0 and x+1<R and dirCheck(l[x][y+1],Right) and ((dirCheck(l[x-1][y],Top) and dirCheck(l[x+1][y],Bottom)) or (dirCheck(l[x-1][y],Bottom) and dirCheck(l[x+1][y],Top))):
        print(x+1,y+1,'+')
      elif y+1<C and l[x][y+1] in ['-','+','3','4','M']:
        print(x+1,y+1,'-')
      elif x-1>=0 and l[x-1][y] in ['|','+','1','4','M']:
        print(x+1,y+1,'3')
      elif x+1<R and l[x+1][y] in ['|','+','2','3','M']:
        print(x+1,y+1,'4')

  else:
    dir=block(l[x][y],dir)
    if dir==Top:
      q.append([x-1,y,dir])
    elif dir==Bottom:
      q.append([x+1,y,dir])
    elif dir==Left:
      q.append([x,y-1,dir])
    else: # Right
      q.append([x,y+1,dir])
