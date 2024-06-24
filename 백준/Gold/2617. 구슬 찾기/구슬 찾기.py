import sys
input=sys.stdin.readline

N,M=map(int,input().split())
light={} # 해당 노드보다 가벼운 것 저장
heavy={}
for i in range(1,N+1):
  light[i]={}
  heavy[i]={}

for i in range(M):
  a,b=map(int,input().split())
  light[a][b]=True
  heavy[b][a]=True

# 1 2 4
# 1 5
# 3 4
  
def make(lists):
  for i in range(1,N+1):
    visited=[False for j in range(N+1)]
    visited[i]=True
    q=[i]
    while q:
      idx=q.pop()
      for item in list(lists[idx].keys()):
        if not visited[item]:
          visited[item]=True
          lists[i][item]=True
          q.append(item)

make(light)
make(heavy)

answer={}
for item in light.keys():
  if len(light[item].keys())>=(N+1)//2:
    answer[item]=True

for item in heavy.keys():
  if len(heavy[item].keys())>=(N+1)//2:
    answer[item]=True

print(len(answer.keys()))
