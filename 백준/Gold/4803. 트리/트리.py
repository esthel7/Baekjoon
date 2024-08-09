import sys
input=sys.stdin.readline

time=0
while True:
  time+=1
  n,m=map(int,input().split())
  if n==0 and m==0:
    break

  info={} # 각 노드별 루트 저장
  root={} # 해당 루트에 속하는 노드 저장
  for i in range(1,n+1):
    info[i]=i
    root[i]=[i]

  for i in range(m):
    a,b=map(int,input().split())
    if info[a]==info[b]:
      item=info[a]
      if item==-1:
        continue
      for node in root[item]:
        info[node]=-1
      root.pop(item)
      continue
  
    if info[a]==-1:
      change=info[b]
      for node in root[change]:
        info[node]=-1
      root.pop(change)
      continue
    elif info[b]==-1:
      change=info[a]
      for node in root[change]:
        info[node]=-1
      root.pop(change)
      continue

    if len(root[info[a]])>=len(root[info[b]]):
      change=info[b]
      origin=info[a]
    else:
      change=info[a]
      origin=info[b]
    for node in root[change]:
      info[node]=origin
      root[origin].append(node)
    root.pop(change)

  cnt=len(root.keys())
  print('Case %d: '%(time),end='')
  if cnt==0:
    print('No trees.')
  elif cnt==1:
    print('There is one tree.')
  else:
    print('A forest of %d trees.'%(cnt))
