import sys
input=sys.stdin.readline

def find(W,K):
  info={}
  for i in range(len(W)):
    if W[i] in info:
      info[W[i]].append(i)
    else:
      info[W[i]]=[i]

  Min=20000
  Max=0
  answer=[-1,-1]
  for key in info.keys():
    if len(info[key])<K:
      continue
    for i in range(len(info[key])-K+1):
      now=info[key][i+K-1]-info[key][i]+1
      if Min>now:
        Min=now
        answer[0]=now
      if Max<now:
        Max=now
        answer[1]=now

  if answer[0]==-1:
    print(-1)
  else:
    for item in answer:
      print(item,end=' ')
    print()



T=int(input())
for _ in range(T):
  W=input().rstrip()
  K=int(input())
  find(W,K)
