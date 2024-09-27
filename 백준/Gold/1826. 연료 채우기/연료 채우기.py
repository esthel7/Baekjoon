import heapq
n = int(input())
station = []
for _ in range(n+1):
    location, gas = map(int, input().split())
    station.append([location, gas])

station.sort()
fuel = station[n][1] #처음에 가지고 있는 연료량
current_location = 0 #초기 위치
cnt = 0

h = []  #힙을 이용해 최대값을 빠르게 찾아내기.
for i in range(n+1):
    distance = station[i][0] - current_location
    current_location = station[i][0]
    if fuel < distance: #연료가 부족할때. 빌려와야하는데, 지나간 주유소들중에서 가장 연료를 많이 채울수 있는 주유소를 선택.
        while fuel < distance:
            if len(h) > 0:
                fuel += (-1*heapq.heappop(h))
                cnt += 1
            else:
                cnt = -1
                break
        if cnt == -1:
            break
    fuel -= distance
    heapq.heappush(h, -1 * station[i][1]) #일부러 -1을 곱해 최대값을 찾기 쉽게 해줬음.
print(cnt)