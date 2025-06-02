# 22352번 항체 인식
from collections import deque
import sys

input = sys.stdin.readline

dxys = ((1,0),(-1,0),(0,1),(0,-1))

m, n = map(int, input().split())
grid_before = [input().split() for _ in range(m)]
grid_after = [input().split() for _ in range(m)]

def bfs(sx, sy, new_num):
    queue = deque([[sx,sy]])
    visited = [[False]*n for _ in range(m)] 
    visited[sy][sx] = True
    target = grid_before[sy][sx]
    while queue:
        cx, cy = queue.pop()
        grid_before[cy][cx] = new_num
        for dx, dy in dxys:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < n and 0 <= ny < m and visited[ny][nx] == False:
                if grid_before[ny][nx] == target:
                    queue.appendleft([nx, ny])
                    visited[ny][nx] = True

def checkAll():
    for i in range(m):
        for j in range(n):
            if grid_after[i][j] == grid_before[i][j]:
                continue
            else:
                return False
    return True


def solve():
    for i in range(m):
        for j in range(n):
            if grid_before[i][j] != grid_after[i][j]:
                bfs(j,i,grid_after[i][j])
                if checkAll():
                    return "YES"
                else:
                    return "NO"
    return "YES"

print(solve())