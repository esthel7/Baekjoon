import sys
input=sys.stdin.readline

# 뒤에 오는 수의 진입차수(degree)를 1씩 증가시킴 -> 순서 결정 위함

# 진입차수가 0인 정점을 큐에 삽입 -> 맨앞에 위치함
# 큐에서 원소를 꺼내 해당 원소와 연결된 간선을 모두 제거 -> 진입차수 1씩 감소
# 제거한 후에 진입차수가 0인 정점을 큐에 삽입

N,M=map(int,input().split())
degree=[0 for i in range(32001)]
graph=[[]for i in range(32001)]
for i in range(M):
    a,b=map(int,input().split())
    degree[b]=degree[b]+1 # 진입차수 증가
    graph[a].append(b)

q=[]
for i in range(1,N+1):
    if degree[i]==0:
        q.append(i)

while len(q)>0:
    first=q.pop(0)
    print(first,end=' ')
    for i in range(len(graph[first])):
        back=graph[first][i]
        degree[back]=degree[back]-1
        if degree[back]==0:
            q.append(back)

# flag=0
# while flag<N:
#     for i in range(1,N+1):
#         if degree[i]==0: # 맨 앞에 위치
#             print(i,end=' ')
#             flag=flag+1
#             degree[i]=-1
#             for j in range(len(graph[i])): # 해당 번호 뒤에 오는 번호의 degree 감소시켜주기
#                 back=graph[i][j]
#                 degree[back]=degree[back]-1
#                 if degree[back]==0:
#                     print(back,end=' ')
#                     flag=flag+1
#                     degree[back]=-1


