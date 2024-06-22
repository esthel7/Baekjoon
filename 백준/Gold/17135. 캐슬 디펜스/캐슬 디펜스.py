import sys
import copy
input=sys.stdin.readline

# 궁수 3명
# 적 하나 공격 가능, 동시 공격
# 거리가 D이하 적 중 가장 가까운 적 (동일하면 가장 왼쪽) -> 맞으면 제외됨
# 적은 아래로 한칸 이동, 성으로 이동하면 제외됨
# 궁수 공격으로 제거할 수 있는 적의 최대수

def find(now,info,cnt):
  global answer

  if not info.keys():
    if answer<cnt:
      answer=cnt
    return

  attack=[[D+1],[D+1],[D+1]]
  for x in info:
    for y in info[x]:
      for k in range(3):
        value=N-x+abs(now[k]-y)
        if value<=D:
          if attack[k][0]>value:
            attack[k]=[value,x,y]
          elif attack[k][0]==value:
            if attack[k][2]>y:
              attack[k]=[value,x,y]

  for i in range(3):
    if attack[i][0]>D:
      continue
    x=attack[i][1]
    y=attack[i][2]
    if x in info and y in info[x]:
      info[x].pop(y)
      cnt+=1
      if not info[x]:
        info.pop(x)

  newInfo={}
  for x in info:
    if x+1==N:
      continue
    if x+1 not in newInfo:
      newInfo[x+1]={}
    for y in info[x]:
      newInfo[x+1][y]=True
  find(now,newInfo,cnt)



def loc(now,start):
  global info
  if len(now)==3:
    find(now,copy.deepcopy(info),0)
    return

  for i in range(start,M):
    now.append(i)
    loc(now,i+1)
    now.pop()


N,M,D=map(int,input().split())

l=[]
info={}
for i in range(N):
  now=list(map(int,input().split()))
  l.append(now)
  for j in range(M):
    if now[j]==1:
      if i in info:
        info[i][j]=True
      else:
        info[i]={j:True}

answer=0
loc([],0)
print(answer)
