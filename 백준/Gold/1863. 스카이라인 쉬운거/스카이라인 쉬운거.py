import sys
input=sys.stdin.readline

n=int(input())
l=[[0,0]]
maxY=0
for i in range(n):
  x,y=map(int,input().split())
  if maxY<y:
    maxY=y
  l.append([x,y])

D=l[-1][0]+1
d=[0 for i in range(D)]
for i in range(1,n+1):
  for j in range(l[i-1][0]+1,l[i][0]):
    d[j]=l[i-1][1]
  d[l[i][0]]=l[i][1]

# print(d)
save={}
answer=0
idx=0
Max=0
while idx<D:
  # print(idx,save)
  if d[idx]<Max:
    Keys=list(save.keys())
    for keys in Keys:
      if keys>d[idx]:
        answer+=1
        save.pop(keys)
  if d[idx]==0:
    idx+=1
    continue
  if d[idx] in save:
    idx+=1
    continue
  else:
    save[d[idx]]=True
    Max=d[idx]
    idx+=1
    continue

# print(idx,save)
answer+=len(save)
print(answer)
