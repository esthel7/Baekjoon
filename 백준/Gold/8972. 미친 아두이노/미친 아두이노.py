import sys
import copy
input=sys.stdin.readline

# 한칸 이동하거나 그대로
# 미친 아누이노 칸으로 이동 시 패배
# 미친 아두이노는 종수 방향으로 한칸 이동
# 미친 아두이노가 종수 칸으로 올 경우 종수 패배
# 2개 이상의 아두이노가 같은 칸에 있으면 그 칸의 아두이노 모두 파괴

def save(x,y,time):
  global jsx, jsy
  if x==jsx and y==jsy:
    print('kraj',time)
    exit(0)

  if x in newCrazy:
    if y in newCrazy[x]:
      newCrazy[x][y]+=1
    else:
      newCrazy[x][y]=1
  else:
    newCrazy[x]={y:1}

R,C=map(int,input().split())

l=[]
jsx=0
jsy=0
crazy={}
board=['.' for i in range(C)]
for i in range(R):
  now=list(input().rstrip())
  for j in range(C):
    if now[j]=='R':
      if i in crazy:
        crazy[i][j]=1
      else:
        crazy[i]={j:1}
    elif now[j]=='I':
      jsx=i
      jsy=j
  l.append(list(board))

moves=list(input().rstrip())

for i in range(len(moves)):
  move=moves[i]
  if move=='1': # bottomleft
    jsx+=1
    jsy-=1
  elif move=='2': # bottom
    jsx+=1
  elif move=='3': # bottomright
    jsx+=1
    jsy+=1
  elif move=='4': # left
    jsy-=1
  elif move=='6': # right
    jsy+=1
  elif move=='7': # topleft
    jsx-=1
    jsy-=1
  elif move=='8': # top
    jsx-=1
  elif move=='9': # topright
    jsx-=1
    jsy+=1

  if jsx in crazy:
    if jsy in crazy[jsx]:
      if crazy[jsx][jsy]==1:
        print('kraj',i+1)
        exit(0)

  newCrazy={} # 우선 다 이동 후 겹치는것만 터지는것으로 구현
  for x in crazy:
    for y in crazy[x]:
      if crazy[x][y]!=1:
        continue

      if x==jsx:
        if y>jsy:
          save(x,y-1,i+1)
        else: # y<jsy
          save(x,y+1,i+1)
      elif x>jsx:
        if y==jsy:
          save(x-1,y,i+1)
        elif y>jsy:
          save(x-1,y-1,i+1)
        else:
          save(x-1,y+1,i+1)
      else:
        if y==jsy:
          save(x+1,y,i+1)
        elif y>jsy:
          save(x+1,y-1,i+1)
        else:
          save(x+1,y+1,i+1)
  crazy=copy.deepcopy(newCrazy)

l[jsx][jsy]='I'
for x in crazy:
  for y in crazy[x]:
    if crazy[x][y]!=1:
      continue
    l[x][y]='R'

for i in range(R):
  print(''.join(l[i]))
