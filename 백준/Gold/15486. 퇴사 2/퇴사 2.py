import sys
input=sys.stdin.readline

def find():
    for i in range(1,N+1):
        costs[i]=max(costs[i-1],costs[i]) # 어제값쓸지 기존 수들 바탕으로 도달한 현재값 쓸지 결정
        x=i+t[i]-1
        if x<=N:
            costs[x]=max(costs[i-1]+p[i],costs[x]) # 일 할지 안할지

N=int(input())
t=[]
p=[]
costs=[0 for i in range(N+1)]
t.append(0)
p.append(0)
for i in range(N):
    T,P=map(int,input().split())
    t.append(T)
    p.append(P)

find()
print(max(costs))
