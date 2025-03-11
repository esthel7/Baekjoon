from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
topologic_parts = [0]*N
needed_parts = [defaultdict(int) for _ in range(N)]
basic_parts = [defaultdict(int) for _ in range(N)]
q = deque()

for _ in range(M) :
  x, y, k = map(int, input().split())
  topologic_parts[x-1] += 1
  needed_parts[y-1][x-1] += k

for i in range(N) :
  if topologic_parts[i] == 0 :
    q.append(i)
    basic_parts[i][i] = 1

while q :
  node = q.popleft()
  for nxt, mul in needed_parts[node].items() :
    for key, val in basic_parts[node].items() :
      basic_parts[nxt][key] += val*mul
    topologic_parts[nxt] -= 1
    if topologic_parts[nxt] == 0 :
      q.append(nxt)

for key, val in sorted(basic_parts[-1].items()) :
  print(key+1, val)
