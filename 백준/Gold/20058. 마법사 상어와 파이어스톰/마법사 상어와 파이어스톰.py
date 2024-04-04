import sys
input=sys.stdin.readline

# 부분 격자를 시계 방향으로 90도 회전
# 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음양 -1

def change(x,y,lidx):
  prev=[]
  for i in range(x,x+lidx):
    prev.append([])
    for j in range(y,y+lidx):
      prev[i-x].append(l[i][j])

  for i in range(lidx):
    for j in range(lidx):
      l[x+j][y+lidx-1-i]=prev[i][j]


def find(lidx):
  global answer

  for i in range(0,N,lidx):
    for j in range(0,N,lidx):
      change(i,j,lidx)

  minus={}
  for i in range(N):
    for j in range(N):
      cnt=0
      for k in range(4):
        newI=i+xbox[k]
        newJ=j+ybox[k]
        if 0<=newI<N and 0<=newJ<N:
          if l[newI][newJ]>0:
            cnt+=1

      if cnt<3 and l[i][j]>0:
        if i in minus:
          minus[i].append(j)
        else:
          minus[i]=[j]

  for x in minus.keys():
    for y in minus[x]:
      l[x][y]-=1
      answer-=1


N,Q=map(int,input().split())
N=2**N

answer=0
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))
  answer+=sum(l[i])

L=list(map(int,input().split()))

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
for lidx in L:
  find(2**lidx)

print(answer)

root=[[0 for i in range(N)]for j in range(N)]
cnt=1
info={}
for i in range(N):
  for j in range(N):
    if l[i][j]==0:
      continue

    topI=i-1
    topJ=j
    if 0<=topI<N and 0<=topJ<N and root[topI][topJ]!=0:
      root[i][j]=root[topI][topJ]
      info[root[topI][topJ]].append([i,j])

    leftI=i
    leftJ=j-1
    if 0<=leftI<N and 0<=leftJ<N and root[leftI][leftJ]!=0:
      if root[i][j]==0:
        root[i][j]=root[leftI][leftJ]
        info[root[leftI][leftJ]].append([i,j])
        continue
      elif root[i][j]==root[leftI][leftJ]:
        continue
      else:
        Max=max(root[topI][topJ],root[leftI][leftJ])
        Min=min(root[topI][topJ],root[leftI][leftJ])
        for x,y in info[Max]:
          root[x][y]=Min
          info[Min].append([x,y])
        info.pop(Max)
        continue

    if root[i][j]==0:
      root[i][j]=cnt
      info[root[i][j]]=[[i,j]]
      cnt+=1

answer=0
for keys in info:
  if answer<len(info[keys]):
    answer=len(info[keys])
print(answer)
