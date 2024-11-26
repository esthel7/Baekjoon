from collections import deque
import sys
input = sys.stdin.readline

def bfs(i):
    visited = [0] * (N + 1)
    q = deque([i])
    visited[i] = 1
    cnt = 1

    while q:
        x = q.popleft()

        for nx in computer[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = 1
                cnt += 1

    return cnt


N, M = map(int, input().split())
computer = [[] for _ in range(N+1)]


for _ in range(M):
    A, B = map(int,input().split())
    computer[B].append(A)

answer = []
max_hack = 0
for i in range(1, N+1):
    result = bfs(i)
    if max_hack < result:
        max_hack = result
        answer.clear()
        answer.append(i)
    elif max_hack == result:
        answer.append(i)

print(*answer)