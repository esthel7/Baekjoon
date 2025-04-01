import sys
input = sys.stdin.readline

MOD = 987_654_321
Catalan = [0 for _ in range(5002)]
Catalan[0], Catalan[1] = 1, 1
for i in range(2, 5002):
    C = 0
    for j in range(i):
        C += (Catalan[j]*Catalan[i-j-1])%MOD
    C %= MOD
    Catalan[i] = C
N = int(input())
print(Catalan[N//2])