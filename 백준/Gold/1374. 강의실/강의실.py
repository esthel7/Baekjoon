import sys
import heapq
input = sys.stdin.readline

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x: x[1])

mh = []
cnt = 0
for i in l:
    while mh and mh[0] <= i[1]: # 가장 일찍 끝나는 시간보다 시작 시간이 크면
        heapq.heappop(mh)       # mh에서 가장 작은 원소 pop & return
    heapq.heappush(mh, i[2])    # mh에 i[2]=끝나는 시간을 추가
    cnt = max(cnt, len(mh))

print(cnt)