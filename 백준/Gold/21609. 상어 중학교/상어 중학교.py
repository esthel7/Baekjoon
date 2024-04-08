import sys
input=sys.stdin.readline

# 검은색, 무지개, 일반 블록, 일반 블록은 M가지 색상

# 블록 그룹은 연결된 블록의 집합, 일반 블록은 적어도 한개 있고 일반 블록 색 모두 동일
# 검은색 블록은 블록 그룹에 포함x
# 블록 그룹은 2개 이상, 기준 블록은 일반 블록 중 가장 위&왼쪽 블록

# 크기가 가장 큰 블록그룹(여러개라면 무지개가 가장 많은 그룹, 가장 아래, 가장 오른쪽)
# 가장 큰 블록그룹 모두 제거, 블록개수**2 점수 획득
# 검은색 제외 모든 블록이 아래로 이동
# 반시계 회전
# 검은색 제외 모든 블록이 아래로 이동

def down():
  for i in range(N):
    now=list(l[i])
    j=N-1
    while j>=0:
      while now:
        if now[-1]==empty:
          now.pop()
        else:
          break

      if not now:
        for k in range(j,-1,-1):
          l[i][k]=empty
        break

      if now[-1]==-1:
        for k in range(j,len(now)-1,-1):
          l[i][k]=empty
        j=len(now)-1
        l[i][j]=-1
        now.pop()
      else:
        l[i][j]=now.pop()
      j-=1


def rotate():
  global l
  newL=[[0 for i in range(N)]for j in range(N)]
  for i in range(N):
    for j in range(N):
      newL[j][N-i-1]=l[i][j]
  l=list(list(arr)for arr in newL)


def findGroup():
  # print()
  # print(l)
  global answer
  size=0
  rainbow=0
  bottom=-1
  right=-1
  group=[]

  visit=[[False for i in range(N)]for j in range(N)]
  for i in range(N):
    for j in range(N):
      if visit[i][j] or l[i][j] in [empty,-1,0]:
        continue

      q=[[i,j]]
      flag=l[i][j]
      nowsize=0
      nowrainbow=0
      nowbottom=j
      nowright=i
      nowgroup=[]
      while q:
        x,y=q.pop()
        if (visit[x][y] and l[x][y]!=0) or l[x][y]==-1 or l[x][y]==empty or l[x][y] not in [0,flag]:
          continue
        if visit[x][y] and l[x][y]==0 and [x,y] in nowgroup:
          continue
        visit[x][y]=True

        nowgroup.append([x,y])
        nowsize+=1
        if l[x][y]==0:
          nowrainbow+=1
        else:
          if nowbottom>y:
            nowright=x
            nowbottom=y
          elif nowbottom==y and nowright>x:
            nowright=x

        for k in range(4):
          nextx=x+xbox[k]
          nexty=y+ybox[k]
          if 0<=nextx<N and 0<=nexty<N:
            q.append([nextx,nexty])
      if nowsize>size:
        size=nowsize
        rainbow=nowrainbow
        bottom=nowbottom
        right=nowright
        group=list(list(arr) for arr in nowgroup)
      elif nowsize==size and nowrainbow>rainbow:
        rainbow=nowrainbow
        bottom=nowbottom
        right=nowright
        group=list(list(arr) for arr in nowgroup)
      elif nowsize==size and nowrainbow==rainbow and nowbottom>bottom:
        bottom=nowbottom
        right=nowright
        group=list(list(arr) for arr in nowgroup)
      elif nowsize==size and nowrainbow==rainbow and nowbottom==bottom and nowright>right:
        right=nowright
        group=list(list(arr) for arr in nowgroup)

  if size<=1:
    return answer

  answer+=len(group)**2
  # print('append',len(group),group,answer)
  for x,y in group:
    l[x][y]=empty

  down()
  rotate()
  down()
  return findGroup()


N,M=map(int,input().split())
l=[[]for i in range(N)] # 세로줄 기준으로 들어있음
for i in range(N):
  now=list(map(int,input().split()))
  for j in range(N):
    l[j].append(now[j])

answer=0
empty=M+1
xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
print(findGroup())
