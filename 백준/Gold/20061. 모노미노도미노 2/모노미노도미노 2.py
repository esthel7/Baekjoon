import sys
input=sys.stdin.readline

def fullGreen(x):
  global answer
  flag=False
  for i in range(4):
    if not green[x][i]:
      flag=True
      break
  if not flag:
    answer+=1
    green.pop(x)
    green.insert(0,[False for i in range(4)])
    return True
  return False

def fullBlue(x):
  global answer
  flag=False
  for i in range(4):
    if not blue[x][i]:
      flag=True
      break
  if not flag:
    answer+=1
    blue.pop(x)
    blue.insert(0,[False for i in range(4)])
    return True
  return False


green=[[False for i in range(4)]for j in range(6)]
blue=[[False for i in range(4)]for j in range(6)]

answer=0
N=int(input())
for _ in range(N):
  t,x,y=map(int,input().split())
  greenFlag=False
  blueFlag=False
  if t==1:
    for i in range(1,5):
      if not green[i][y] and green[i+1][y]:
        green[i][y]=True
        if i==1:
          green.pop()
          green.insert(0,[False for j in range(4)])
        else:
          fullGreen(i)
        greenFlag=True
        break
    if not greenFlag:
      green[5][y]=True
      fullGreen(5)
    for i in range(1,5):
      if not blue[i][x] and blue[i+1][x]:
        blue[i][x]=True
        if i==1:
          blue.pop()
          blue.insert(0,[False for j in range(4)])
        else:
          fullBlue(i)
        blueFlag=True
        break
    if not blueFlag:
      blue[5][x]=True
      fullBlue(5)
  elif t==2:
    for i in range(1,5):
      if not green[i][y] and not green[i][y+1] and (green[i+1][y] or green[i+1][y+1]):
        green[i][y]=True
        green[i][y+1]=True
        if i==1:
          green.pop()
          green.insert(0,[False for j in range(4)])
        else:
          fullGreen(i)
        greenFlag=True
        break
    if not greenFlag:
      green[5][y]=True
      green[5][y+1]=True
      fullGreen(5)
    for i in range(1,5):
      if not blue[i][x] and blue[i+1][x]:
        blue[i][x]=True
        blue[i-1][x]=True
        if i==1:
          blue.pop()
          blue.pop()
          blue.insert(0,[False for j in range(4)])
          blue.insert(0,[False for j in range(4)])
        elif i==2:
          if not fullBlue(2):
            blue.pop()
            blue.insert(0,[False for j in range(4)])
        else:
          if fullBlue(i):
            fullBlue(i)
          else:
            fullBlue(i-1)
        blueFlag=True
        break
    if not blueFlag:
      blue[5][x]=True
      blue[4][x]=True
      if fullBlue(5):
        fullBlue(5)
      else:
        fullBlue(4)
  else:
    for i in range(1,5):
      if not green[i][y] and green[i+1][y]:
        green[i][y]=True
        green[i-1][y]=True
        if i==1:
          green.pop()
          green.pop()
          green.insert(0,[False for j in range(4)])
          green.insert(0,[False for j in range(4)])
        elif i==2:
          if not fullGreen(2):
            green.pop()
            green.insert(0,[False for j in range(4)])
        else:
          if fullGreen(i):
            fullGreen(i)
          else:
            fullGreen(i-1)
        greenFlag=True
        break
    if not greenFlag:
      green[5][y]=True
      green[4][y]=True
      if fullGreen(5):
        fullGreen(5)
      else:
        fullGreen(4)
    for i in range(1,5):
      if not blue[i][x] and not blue[i][x+1] and (blue[i+1][x] or blue[i+1][x+1]):
        blue[i][x]=True
        blue[i][x+1]=True
        if i==1:
          blue.pop()
          blue.insert(0,[False for j in range(4)])
        else:
          fullBlue(i)
        blueFlag=True
        break
    if not blueFlag:
      blue[5][x]=True
      blue[5][x+1]=True
      fullBlue(5)

print(answer)
cnt=0
for i in range(2,6):
  for j in range(4):
    if blue[i][j]:
      cnt+=1
    if green[i][j]:
      cnt+=1
print(cnt)
