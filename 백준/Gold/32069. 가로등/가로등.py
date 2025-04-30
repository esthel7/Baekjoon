from collections import deque
from sys import stdin
input = stdin.readline

l, n, k = map(int, input().split())
coor = list(map(int, input().split()))

visit = set() # 이미 방문한 위치 저장
q = deque()
light = dict() # {위치: 어두운 정도}
for i in range(n):
    visit.add(coor[i])
    light[coor[i]] = 0
    q.append(coor[i])

count = 0
while q:
    i = q.popleft()
    count += 1
    if i - 1 >= 0 and i - 1 not in visit:
        light[i - 1] = light[i] + 1
        visit.add(i - 1)
        q.append(i - 1)
    if i + 1 <= l and i + 1 not in visit:
        light[i + 1] = light[i] + 1
        visit.add(i + 1)
        q.append(i + 1)
    if count == k: # k번째까지 출력할 것이기 때문에 k번 반복 후 종료
        break

light = sorted(light.items(), key=lambda x:x[1]) # 딕셔너리를 value 기준으로 오름차순 정렬
for i in range (k) :
    print(light[i][1])