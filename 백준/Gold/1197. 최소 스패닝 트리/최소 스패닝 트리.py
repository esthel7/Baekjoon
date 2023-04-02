import sys
input=sys.stdin.readline

def find():
    root=[0 for i in range(V+1)]
    costs=0
    visited=[0 for i in range(V+1)]

    while len(q)>0:
        cost,start,end=q.pop(0)

        if root[start]!=0 and root[start]==root[end]:
            # 사이클임
            continue
        costs=costs+cost

        if visited[start]==0 and visited[end]==0:
            # 둘이 연결 후 같은 뿌리 갖기
            # print('new new',start,end,'append cost=',cost,'total costs=',costs)
            root[start]=start
            root[end]=root[start]

        elif visited[start]==0:
            # print('new old',start,end,'append cost=',cost,'total costs=',costs)
            root[start]=root[end]

        elif visited[end]==0:
            # print('old new',start,end,'append cost=',cost,'total costs=',costs)
            root[end]=root[start]

        else: # 서로 다른 뿌리 갖고있음
            # print('old old -> change root',start,end,'append cost=',cost,'total costs=',costs)
            change=root[end]
            for j in range(1,V+1):
                if root[j]==change:
                    root[j]=root[start]
                    
        visited[start]=1
        visited[end]=1
    print(costs)

# 가중치 합이 최소
# 간선을 가중치 오름차순 정렬, 낮은 것부터 순회하면서 사이클 발생하면 continue, 아니면 추가 -> Kruskal Algorithm
V,E=map(int,input().split())

q=[]
for i in range(E):
    A,B,C=map(int,input().split())
    if A<B:
        q.append([C,A,B])
    else:
        q.append([C,B,A])

q.sort() # 가격 낮은 순으로 정렬
find()

