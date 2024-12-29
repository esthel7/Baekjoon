from sys import stdin

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

ans = 0
A.sort()
# 3명으로 구성된 경우만 출전 가능
for i in range(N-2):
    # 투 포인터 알고리즘으로 합이 -A[i] 인 요소들을 구함
    start = i+1
    end = N-1
    while start < end:
        s = A[start] + A[end]
        if s == -A[i]:
            if A[start] == A[end]:
                ans += (end-start)
                start += 1
            else:
                j,k = start, end
                while A[j] == A[start] and j < end:
                    j += 1
                while A[k] == A[end] and k > start:
                    k -= 1
                ans += (j-start)*(end-k)
                start,end = j,k
        elif s < -A[i]:
            start += 1
        else:
            end -= 1
print(ans)