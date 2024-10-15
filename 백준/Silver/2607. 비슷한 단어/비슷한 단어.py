import sys
import copy
input=sys.stdin.readline

N=int(input())
word=list(input().rstrip())
info={}
for item in word:
  if item in info:
    info[item]+=1
  else:
    info[item]=1

answer=0
for i in range(N-1):
  now=list(input().rstrip())
  remain=copy.deepcopy(info)
  plus={}
  flag=True
  for item in now:
    if item in remain:
      remain[item]-=1
      if remain[item]==0:
        remain.pop(item)
    else:
      if item in plus:
        flag=False
        break
      else:
        plus[item]=1

  if not flag:
    continue
  Remain=list(remain.keys())
  Plus=list(plus.keys())
  if not Remain:
    if len(Plus)>1:
      continue
    if Plus and plus[Plus[0]]!=1:
      continue
  else:
    if len(Remain)>1:
      continue
    if remain[Remain[0]]!=1:
      continue
    if len(Plus)>1:
      continue
    if Plus and plus[Plus[0]]!=1:
      continue
  answer+=1

print(answer)
