import sys
input=sys.stdin.readline

def find():
    for i in range(1,N+1):
        costs[i]=max(costs[i],costs[i-1]) # 현재와 어제의 비교 -> 기존 수들 바탕으로 도달한 현재값이랑, 어제의 값이랑 비교하여 큰 값 선택 (기존 값들을 버릴지, 어제 값을 버릴지)
        if i+t[i]-1<=N: # i번째 날의 일을 선택해도 시간 안에 끝낼 수 있다면
            costs[i+t[i]-1]=max(costs[i+t[i]-1],costs[i-1]+p[i]) # 기존 값이랑 i번째 일을 하는 것(i번째날의 일을 하므로 i-1번째날의 costs값) 중에 선택
    
    print(costs[N])

# 1일차까지의 최댓값, 2일차까지의 최댓값 ... 으로 구하기
N=int(input())
t=[0]
p=[0]
for i in range(N):
    time,pay=map(int,input().split())
    t.append(time)
    p.append(pay)

costs=[0]*(N+1)
find()
