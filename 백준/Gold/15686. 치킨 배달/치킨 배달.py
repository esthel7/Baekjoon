from collections import deque

N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

# 도시의 치킨 거리는 모든 집의 치킨 거리의 합

chickhen=[]
home=[]
for i in range(N):
  for j in range(N):
    if l[i][j]==0:
      continue
    elif l[i][j]==1:
      home.append([i,j,[]]) # 치킨집 순서대로 거리 들어감
    else:
      chickhen.append([i,j])


def find(x,y): # 치킨집 별 거리
  s=[]
  for i in range(len(chickhen)):
    far=abs(x-chickhen[i][0])+abs(y-chickhen[i][1])
    s.append(far)
  return s

for i in range(len(home)):
  [x,y,fars]=home[i]
  home[i][2]=list(find(x,y)) # 치킨집 별 거리

def calculate(lefts):
  fars=[-1 for i in range(len(home))]
  for idx in lefts:
    for i in range(len(home)):
      now=home[i][2][idx]
      if fars[i]==-1 or fars[i]>now:
        fars[i]=now

  now=0
  for i in range(len(home)):
    now+=fars[i]
  return now

def select(start,lefts):
  if len(lefts)==M:
    value=calculate(lefts)
    if answer[0]==-1 or answer[0]>value:
      answer[0]=value
    return

  for i in range(start,len(chickhen)):
    if i not in lefts:
      lefts.append(i)
      select(i+1,lefts)
      lefts.pop()

answer=[-1]
select(0,[]) # 장사할 치킨집 결정 및 거리 계산
print(answer[0])
