import sys
from collections import deque
input=sys.stdin.readline

def DFS(start,node,stack):
    print(start+1, end=' ')
    stack[start]=1
    if start in node:
        for i in range(len(node[start])):
            nextNode=node[start][i]
            if stack[nextNode]==1:
                continue
            else:
                DFS(nextNode,node,stack)

def BFS(start,node,q,inQ):
    q.append(start)
    inQ[start]=1
    while len(q):
        start=q.popleft()
        print(start+1,end=' ')
        if start in node:
            for i in range(len(node[start])):
                nextNode=node[start][i]
                if inQ[nextNode]!=1:
                    q.append(nextNode)
                    inQ[nextNode]=1

N,M,V=map(int,input().split())
node={}
for i in range(M):
    a,b=map(int,input().split())
    if (a-1) in node:
        node[a-1].append(b-1)
        node[a-1]=sorted(set(node[a-1]))
    else:
        node[a-1]=[b-1]
    if (b-1) in node:
        node[b-1].append(a-1)
        node[b-1]=sorted(set(node[b-1]))
    else:
        node[b-1]=[a-1]

# DFS
start=V-1
stack=[0 for i in range(N)]
DFS(start,node,stack)
print()

# BFS
q=deque()
inQ=[0 for i in range(N)]
start=V-1
BFS(start,node,q,inQ)
