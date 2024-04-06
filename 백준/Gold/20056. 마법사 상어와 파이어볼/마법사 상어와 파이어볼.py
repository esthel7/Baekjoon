import sys
input=sys.stdin.readline

# 파이어볼 M개 발사
# 각자 위치에서 이동 대기

# 모든 파이어볼은 방향, 속력만큼 이동
# 같은 칸에 여러 파이어볼 가능
# 여러개가 있는 칸에서는 모두 하나로 합쳐지고 4개로 나눠짐
# 질량은 5로 나눈 몫, 속력은 속력/개수 몫
# 질량 0이라면 소멸돼 없어짐

N,M,K=map(int,input().split())
total=0
exist={}
for i in range(M):
  r,c,m,s,d=map(int,input().split()) # x,y,질량,속력,방향
  total+=m
  if r-1 in exist:
    exist[r-1][c-1]=[[m,s,d]]
  else:
    exist[r-1]={c-1:[[m,s,d]]}

for t in range(K):
  moving={}
  for r in exist:
    for c in exist[r]:
      for m,s,d in exist[r][c]:
        move=s%N

        if d==0: # top
          x=(r-move+N)%N
          y=c
        elif d==1: # topright
          x=(r-move+N)%N
          y=(c+move)%N
        elif d==2: # right
          x=r
          y=(c+move)%N
        elif d==3: # bottomright
          x=(r+move)%N
          y=(c+move)%N
        elif d==4: # bottom
          x=(r+move)%N
          y=c
        elif d==5: # bottomleft
          x=(r+move)%N
          y=(c-move+N)%N
        elif d==6: # left
          x=r
          y=(c-move+N)%N
        else: # topleft
          x=(r-move+N)%N
          y=(c-move+N)%N

        if x in moving:
          if y in moving[x]:
            moving[x][y][0]+=m
            moving[x][y][1]+=s
            moving[x][y][2]+=1
            if moving[x][y][3]!='diff':
              if (d+2)%2==0 and moving[x][y][3]!='even':
                moving[x][y][3]='diff'
              elif (d+2)%2==1 and moving[x][y][3]!='odd':
                moving[x][y][3]='diff'
          else:
            if (d+2)%2==0:
              moving[x][y]=[m,s,1,'even',d]
            else:
              moving[x][y]=[m,s,1,'odd',d]
        else:
          if (d+2)%2==0:
            moving[x]={y:[m,s,1,'even',d]}
          else:
            moving[x]={y:[m,s,1,'odd',d]}

  exist={}
  for r in moving:
    for c in moving[r]:
      if moving[r][c][2]==1:
        if r in exist:
          exist[r][c]=[[moving[r][c][0],moving[r][c][1],moving[r][c][4]]]
        else:
          exist[r]={c:[[moving[r][c][0],moving[r][c][1],moving[r][c][4]]]}
        continue

      m=moving[r][c][0]//5
      if m==0:
        total-=moving[r][c][0]
        continue
      total-=moving[r][c][0]-m*4
      s=moving[r][c][1]//moving[r][c][2]
      if moving[r][c][3]!='diff': # 0,2,4,6
        if r in exist:
          exist[r][c]=[[m,s,0],[m,s,2],[m,s,4],[m,s,6]]
        else:
          exist[r]={c:[[m,s,0],[m,s,2],[m,s,4],[m,s,6]]}
      else:
        if r in exist:
          exist[r][c]=[[m,s,1],[m,s,3],[m,s,5],[m,s,7]]
        else:
          exist[r]={c:[[m,s,1],[m,s,3],[m,s,5],[m,s,7]]}

print(total)
