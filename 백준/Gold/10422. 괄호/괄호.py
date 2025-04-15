N = int(input())
a = list(int(input()) for _ in range(N))
dp = [0] * (max(a) + 1)
dp[0] = 1

for n in range(2, max(a) + 1, 2):
    for j in range(2, n + 1, 2):
        dp[n] += dp[j - 2] * dp[n - j]
    dp[n] %= 1000000007
for i in a:
    print(dp[i])
