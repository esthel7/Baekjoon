n, x = map(int, input().split())
bob = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda b: (b[0] - b[1]), reverse=True)
x -= 1000 * n # 천 원짜리 전부 구매
answer = sum([i[1] for i in bob]) # 천 원짜리 합
for b in bob:
    if x >= 4000 and b[0] > b[1]:
        answer += b[0] - b[1]
        x -= 4000
    else:
        break
print(answer)