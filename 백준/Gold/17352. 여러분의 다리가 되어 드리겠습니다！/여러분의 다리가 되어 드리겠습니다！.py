# 입력 속도 개선
import sys
input = sys.stdin.readline

n = int(input())
parents = list(range(n+1)) # 부모 노드 저장

# 부모 노드 찾기
def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

# 두 섬 중 작은 숫자를 기준으로 같은 부모를 갖게 함
def union(x,y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 다리가 연결되어 있는 두 섬은 같은 부모를 갖게 함
for _ in range(n-2):
    island1, island2 = map(int,input().split())
    union(island1, island2)

# 1번 섬이 포함된 집합과 부모 노드가 다른 섬 찾아 정답 도출
# 작은 숫자가 부모 노드가 되도록 설정하였음으로 
# 1번이 1번이 포합된 집합의 부모 노드가 됨
for i in range(2,n+1):
    if find(1) != find(i):
        print(1,i)
        break