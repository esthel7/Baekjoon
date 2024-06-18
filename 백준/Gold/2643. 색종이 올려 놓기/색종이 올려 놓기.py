import sys
input=sys.stdin.readline

def find(start):
  if start==N:
    return
  x,y=l[start]
  for i in range(len(info)-1,-1,-1):
    for j in range(len(info[i])):
      px,py=info[i][j]
      if px>=x and py>=y:
        visited[start]=i+2
        if len(info)<i+2:
          info.append([[x,y]])
        else:
          info[i+1].append([x,y])
        return find(start+1)
  visited[start]=1
  info[0].append([x,y])
  find(start+1)

N=int(input())
l=[]
for i in range(N):
  a,b=map(int,input().split())
  if a>=b:
    l.append([a,b])
  else:
    l.append([b,a])
l.sort(reverse=True)

visited=[0 for i in range(N)]
visited[0]=1
info=[[[l[0][0],l[0][1]]]]
find(1)
print(max(visited))
