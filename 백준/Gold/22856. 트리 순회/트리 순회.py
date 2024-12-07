import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(node,flag):
  global lastnode
  if graph[node]['right']==-1 and not flag:
    lastnode=node
    flag=True
  answers.append(node)
  if graph[node]['left']!=-1:
    find(graph[node]['left'],flag)
    answers.append(node)
  if graph[node]['right']!=-1:
    find(graph[node]['right'],flag)
    answers.append(node)


N=int(input())
graph={}
for i in range(N):
  a,b,c=map(int,input().split())
  graph[a]={'left':b,'right':c}

answers=[]
lastnode=-1
if graph[1]['right']==-1:
  flag=True
  lastnode=1
else:
  flag=False
find(1,flag)
while True:
  if answers[-1]==lastnode:
    break
  answers.pop()

print(len(answers)-1)
