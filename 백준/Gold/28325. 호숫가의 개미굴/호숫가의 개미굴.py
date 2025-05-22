from sys import stdin
input = stdin.readline

n = int(input())
c = list(map(int, input().split()))

spare = set() # 쪽방이 있는 굴의 index
for i in range (n) :
    if c[i] != 0:
        spare.add(i)

if len(spare) == 0: # 쪽방이 아예 없는 경우
    print(n // 2)

else:
    memo = [-1] * n # 개미가 살지 않는 경우: -1, 쪽방이 있는 경우: 0, 개미가 사는 경우: 1
    count = 0 # 살 수 있는 개미의 수
    for i in range (n) :
        if i in spare:
            count += c[i] # 쪽방을 모두 채우는 것이 효율적이므로, 쪽방 수만큼 count 증가
            memo[i] = 0
    if n == 2:
        if len(spare) == 1:
            count += 1 # n이 2이고 쪽방이 한 굴에만 있는 경우는 쪽방 수 + 1(쪽방이 없는 굴) 출력
        print(count)
    else:
        index = 0 # 쪽방이 있는 굴의 첫 번째 index
        for i in range (n) :
            if i in spare:
                index = i
                break
        for i in range (index, n + index): # 쪽방이 있는 굴의 index부터 한 바퀴 돌기
            if memo[i % n] == -1: # 만약 현재 index에 개미가 살지 않는다면
                if memo[(i - 1) % n] != 1 and memo[(i + 1) % n] != 1: # 현재 index의 양옆에 쪽방이나 개미가 있지 않다면
                    memo[i % n] = 1 # 현재 index에 개미가 살 수 있음
                    count += 1
        print(count)