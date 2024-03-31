import sys
input=sys.stdin.readline

# 이동 후 비 내려 구름칸 바구니 물 양 1 증가, 구름 없어짐
# 비 내린 칸에서 유효한 칸 내에서 대각선에 물 있으면 1씩 증가
# 물이 2이상인 모든 칸에 구름 생기고 물 양이 2 줄어듦, 구름은 방금 구름이 사라진 자리에선 안생김

N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

rain=[[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
xbox=[-1,-1,1,1]
ybox=[-1,1,-1,1]

for _ in range(M):
  d,s=map(int,input().split())
  s%=N
  newRain={}

  if d==1: # left
    for x,y in rain:
      if y-s>=0:
        y-=s
      else:
        y=N+y-s
      l[x][y]+=1
      if x in newRain:
        newRain[x][y]=True
      else:
        newRain[x]={y:True}
  elif d==2: # topleft
    for x,y in rain:
      if x-s>=0:
        x-=s
      else:
        x=N+x-s
      if y-s>=0:
        y-=s
      else:
        y=N+y-s
      l[x][y]+=1
      if x in newRain:
        newRain[x][y]=True
      else:
        newRain[x]={y:True}
  elif d==3: # top
    for x,y in rain:
      if x-s>=0:
        x-=s
      else:
        x=N+x-s
      l[x][y]+=1
      if x in newRain:
        newRain[x][y]=True
      else:
        newRain[x]={y:True}
  elif d==4: # topright
    for x,y in rain:
      if x-s>=0:
        x-=s
      else:
        x=N+x-s
      if y+s<N:
        y+=s
      else:
        y=y+s-N
      l[x][y]+=1
      if x in newRain:
        newRain[x][y]=True
      else:
        newRain[x]={y:True}
  elif d==5: # right
    for x,y in rain:
      if y+s<N:
        y+=s
      else:
        y=y+s-N
      l[x][y]+=1
      if x in newRain:
        newRain[x][y]=True
      else:
        newRain[x]={y:True}
  elif d==6: # bottomright
    for x,y in rain:
      if x+s<N:
        x+=s
      else:
        x=x+s-N
      if y+s<N:
        y+=s
      else:
        y=y+s-N
      l[x][y]+=1
      if x in newRain:
        newRain[x][y]=True
      else:
        newRain[x]={y:True}
  elif d==7: # bottom
    for x,y in rain:
      if x+s<N:
        x+=s
      else:
        x=x+s-N
      l[x][y]+=1
      if x in newRain:
        newRain[x][y]=True
      else:
        newRain[x]={y:True}
  else: # bottomleft
    for x,y in rain:
      if x+s<N:
        x+=s
      else:
        x=x+s-N
      if y-s>=0:
        y-=s
      else:
        y=N+y-s
      l[x][y]+=1
      if x in newRain:
        newRain[x][y]=True
      else:
        newRain[x]={y:True}

  for x in newRain.keys():
    for y in newRain[x]:
      cnt=0
      for i in range(4):
        newX=x+xbox[i]
        newY=y+ybox[i]
        if 0<=newX<N and 0<=newY<N and l[newX][newY]!=0:
          cnt+=1
      l[x][y]+=cnt

  rain=[]
  for i in range(N):
    for j in range(N):
      if l[i][j]>=2 and (i not in newRain or (i in newRain and j not in newRain[i])):
        l[i][j]-=2
        rain.append([i,j])

answer=0
for i in range(N):
  for j in range(N):
    answer+=l[i][j]
print(answer)
