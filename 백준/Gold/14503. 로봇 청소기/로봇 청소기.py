import sys
input=sys.stdin.readline

# 청소 안되었다면 청소
# 주변칸 중 다 청소가 되어있다면 한칸 후진 / 후진 불가면 멈추기
# 주변칸 중 청소가 안되어있는 칸 있으면 반시계방향 회전 및 앞칸이 청소 안되었다면 전진

def clean(r,c,N,M):
  for i in range(4):
    newX=r+xbox[i]
    newY=c+ybox[i]
    if 0<=newX<N and 0<=newY<M and l[newX][newY]==0:
      return False
  return True


def back(r,c,d,N,M):
  if d==0:
    if r+1<N and l[r+1][c]==0 or l[r+1][c]==-1:
      return [r+1,c]
  elif d==1:
    if c-1>=0 and l[r][c-1]==0 or l[r][c-1]==-1:
      return [r,c-1]
  elif d==2:
    if r-1>=0 and l[r-1][c]==0 or l[r-1][c]==-1:
      return [r-1,c]
  else:
    if c+1<M and l[r][c+1]==0 or l[r][c+1]==-1:
      return [r,c+1]
  return [-1,-1]

def find(r,c,d,N,M):
  if l[r][c]==0:
    l[r][c]=-1
    answer[0]+=1
  if clean(r,c,N,M):
    value=back(r,c,d,N,M)
    if value[0]!=-1:
      find(value[0],value[1],d,N,M)
  else:
    for i in range(4):
      d=(d-1+4)%4
      if d==0:
        if r-1>=0 and l[r-1][c]==0:
          return find(r-1,c,d,N,M)
      elif d==1:
        if c+1<M and l[r][c+1]==0:
          return find(r,c+1,d,N,M)
      elif d==2:
        if r+1<N and l[r+1][c]==0:
          return find(r+1,c,d,N,M)
      else:
        if c-1>=0 and l[r][c-1]==0:
          return find(r,c-1,d,N,M)


N,M=map(int,input().split())
r,c,d=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
answer=[0]
find(r,c,d,N,M)
print(answer[0])
