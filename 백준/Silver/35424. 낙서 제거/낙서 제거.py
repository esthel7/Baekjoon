import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

i = 0
answer = 0

while i < N:
    j = i
    min_val = a[i]
    max_val = a[i]

    while j < N:
        min_val = min(min_val, a[j])
        max_val = max(max_val, a[j])

        area = (j - i + 1) * (max_val - min_val + 1)

        if area > K:
            break

        j += 1

    answer += 1
    i = j

print(answer)