import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
l=deque(map(int,input().split()))
P=l.popleft() # 진실을 아는 사람 수

party=[[]for i in range(N+1)] # 사람 별 참석한 파티
people=[] # 파티 별 참석한 사람
for i in range(M):
  now=deque(map(int,input().split()))
  total=now.popleft()
  for j in range(total):
    party[now[j]].append(i)
  people.append(list(now))

truth=[] # 진실을 말해야하는 파티
while l:
  person=l.popleft()
  for partyidx in party[person]:
    if partyidx in truth:
      continue
    truth.append(partyidx)
    for peopleidx in people[partyidx]:
      if person==peopleidx:
        continue
      l.append(peopleidx)

print(M-len(truth))
