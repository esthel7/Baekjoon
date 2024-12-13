import sys
input=sys.stdin.readline

N,M=map(int,input().split())

loc=[]
for i in range(N):
  x,y=map(int,input().split())
  loc.append([x,y])

cnt=0
root=[-1 for i in range(N)]
for i in range(M):
  x,y=map(int,input().split())
  x-=1
  y-=1
  if root[x]==-1:
    if root[y]==-1:
      Min=min(x,y)
      if Min==0:
        cnt+=2
      root[x]=Min
      root[y]=Min
    else:
      if root[y]==0:
        cnt+=1
      root[x]=root[y]
  else:
    if root[y]==-1:
      if root[x]==0:
        cnt+=1
      root[y]=root[x]
    elif root[x]!=root[y]:
      Min=min(root[x],root[y])
      Max=max(root[x],root[y])
      if Min==0:
        for j in range(N):
          if root[j]==Max:
            root[j]=Min
            cnt+=1
      else:
        for j in range(N):
          if root[j]==Max:
            root[j]=Min

q=[]
for i in range(N):
  for j in range(i+1,N):
    value=((loc[i][0]-loc[j][0])**2+(loc[i][1]-loc[j][1])**2)**0.5
    q.append([value,i,j])

q.sort()

answer=0
for [value,a,b] in q:
  if cnt==N:
    break
  if root[a]==-1:
    answer+=value
    if root[b]==-1:
      Min=min(a,b)
      if Min==0:
        cnt+=2
      root[a]=Min
      root[b]=Min
    else:
      if root[b]==0:
        cnt+=1
      root[a]=root[b]
  else:
    if root[a]==root[b]:
      continue
    elif root[b]==-1:
      answer+=value
      if root[a]==0:
        cnt+=1
      root[b]=root[a]
    else:
      answer+=value
      Min=min(root[a],root[b])
      Max=max(root[a],root[b])
      if Min==0:
        for j in range(N):
          if root[j]==Max:
            root[j]=Min
            cnt+=1
      else:
        for j in range(N):
          if root[j]==Max:
            root[j]=Min


# print('%.2lf'%answer)
print(format(answer, ".2f"))
