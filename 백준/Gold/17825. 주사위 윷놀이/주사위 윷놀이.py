import sys
from collections import deque
input=sys.stdin.readline

# 말 4개
# 도착할때마다 점수 플러스
# 도착칸에 없는 말 하나 골라 이동
# 이동 마칠때 해당 칸에 말 있으면 고를수없음

def check(idx):
  if tracks[0][idx]==10:
    return [1,0]
  if tracks[0][idx]==20:
    return [2,0]
  if tracks[0][idx]==30:
    return [3,0]
  return [0,idx]


def continuePrev(trc,idx):
  if idx>=last[trc]:
    if trc==0 or trc==4: # 도착
      return [-1,trc,0]

    remain=idx-last[trc] # 25 기준 새로운 트랙 타기
    if remain>=last[4]:
      return [-1,4,0]
    return [remain,4,tracks[4][remain]]
  else:
    if trc==0:
      trc,idx=check(idx)
    return [idx,trc,tracks[trc][idx]]


def startNew(now):
  trc,idx=check(now)
  return [idx,trc,tracks[trc][idx]]


def samecheck(flag,remain):
  if flag[0]==-1:
    return False
  for [idx,trc] in remain:
    if idx==-1:
      continue
    if flag[0]==idx and flag[1]==trc:
      return True
    if tracks[flag[1]][flag[0]]==tracks[trc][idx]==40:
      return True
  return False


num=list(map(int,input().split()))

tracks=[
  [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
  [10,13,16,19],
  [20,22,24],
  [30,28,27,26],
  [25,30,35,40]
]

last=[len(tracks[0]),len(tracks[1]),len(tracks[2]),len(tracks[3]),len(tracks[4])]

answer=0
q=deque([[0,0,0,0,0,0,0,0,0,0]])
while q:
  [idx1,idx2,idx3,idx4,track1,track2,track3,track4,point,turn]=q.popleft()
  if turn==10:
    if answer<point:
      answer=point
    continue

  now=num[turn]

  if idx1==0 and track1==0: # 1번말 시작하기
    [idx1,track1,plus]=startNew(now)
    q.append([idx1,idx2,idx3,idx4,track1,track2,track3,track4,point+plus,turn+1])
    continue

  if idx1!=-1: # 1번말 이어가기
    [changeidx1,changetrack1,plus]=continuePrev(track1,idx1+now)
    if not samecheck([changeidx1,changetrack1],[[idx2,track2],[idx3,track3],[idx4,track4]]):
      q.append([changeidx1,idx2,idx3,idx4,changetrack1,track2,track3,track4,point+plus,turn+1])

  if idx2==0 and track2==0: # 2번말 시작하기
    [idx2,track2,plus]=startNew(now)
    if not samecheck([idx2,track2],[[idx1,track1],[idx3,track3],[idx4,track4]]):
      q.append([idx1,idx2,idx3,idx4,track1,track2,track3,track4,point+plus,turn+1])
    continue

  if idx2!=-1: # 2번말 이어가기
    [changeidx2,changetrack2,plus]=continuePrev(track2,idx2+now)
    if not samecheck([changeidx2,changetrack2],[[idx1,track1],[idx3,track3],[idx4,track4]]):
      q.append([idx1,changeidx2,idx3,idx4,track1,changetrack2,track3,track4,point+plus,turn+1])

  if idx3==0 and track3==0: # 3번말 시작하기
    [idx3,track3,plus]=startNew(now)
    if not samecheck([idx3,track3],[[idx1,track1],[idx2,track2],[idx4,track4]]):
      q.append([idx1,idx2,idx3,idx4,track1,track2,track3,track4,point+plus,turn+1])
    continue

  if idx3!=-1: # 3번말 이어가기
    [changeidx3,changetrack3,plus]=continuePrev(track3,idx3+now)
    if not samecheck([changeidx3,changetrack3],[[idx1,track1],[idx2,track2],[idx4,track4]]):
      q.append([idx1,idx2,changeidx3,idx4,track1,track2,changetrack3,track4,point+plus,turn+1])

  if idx4==0 and track4==0: # 4번말 시작하기
    [idx4,track4,plus]=startNew(now)
    if not samecheck([idx4,track4],[[idx1,track1],[idx2,track2],[idx3,track3]]):
      q.append([idx1,idx2,idx3,idx4,track1,track2,track3,track4,point+plus,turn+1])
    continue

  if idx4!=-1: # 4번말 이어가기
    [changeidx4,changetrack4,plus]=continuePrev(track4,idx4+now)
    if not samecheck([changeidx4,changetrack4],[[idx1,track1],[idx2,track2],[idx3,track3]]):
      q.append([idx1,idx2,idx3,changeidx4,track1,track2,track3,changetrack4,point+plus,turn+1])

print(answer)
