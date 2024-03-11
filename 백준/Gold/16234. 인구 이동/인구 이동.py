import sys
input=sys.stdin.readline

def check(i,j,nextI,nextJ):
  global L,R,cnt
  if visit[i][j]!=0 and visit[i][j]==visit[nextI][nextJ]:
    return
  if L<=abs(l[i][j]-l[nextI][nextJ])<=R:
    if visit[i][j]==0:
      if visit[nextI][nextJ]==0:
        cnt+=1
        visit[i][j]=cnt
        visit[nextI][nextJ]=cnt
        team[cnt]=[l[i][j]+l[nextI][nextJ],[[i,j],[nextI,nextJ]]]
      else:
        visit[i][j]=visit[nextI][nextJ]
        team[visit[nextI][nextJ]][0]+=l[i][j]
        team[visit[nextI][nextJ]][1].append([i,j])
    else:
      if visit[nextI][nextJ]==0:
        visit[nextI][nextJ]=visit[i][j]
        team[visit[i][j]][0]+=l[nextI][nextJ]
        team[visit[i][j]][1].append([nextI,nextJ])
      else:
        if visit[i][j]<visit[nextI][nextJ]:
          Min=visit[i][j]
          prev=visit[nextI][nextJ]
        else:
          Min=visit[nextI][nextJ]
          prev=visit[i][j]
        team[Min][0]+=team[prev][0]
        team[Min][1]+=team[prev][1]
        for [prevI,prevJ] in team[prev][1]:
          visit[prevI][prevJ]=Min
        team[prev][0]=0
        team[prev][1]=[]


N,L,R=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

team={}
visit=[[0 for i in range(N)]for j in range(N)]
cnt=0
time=0
while True:
  for i in range(N):
    for j in range(N):
      now=l[i][j]
      if i+1<N:
        check(i,j,i+1,j)
      if j+1<N:
        check(i,j,i,j+1)

  if not len(team):
    print(time)
    break

  for keys in team.keys():
    total=team[keys][0]
    if not total:
      continue
    cnt=len(team[keys][1])
    value=total//cnt
    for [i,j] in team[keys][1]:
      l[i][j]=value

  team={}
  visit=[[0 for i in range(N)]for j in range(N)]
  cnt=0
  time+=1
