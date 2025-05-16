import sys
N = int(sys.stdin.readline())
result =''
while N > 0:
    m = N % 2 # 짝수인지 홀수인지 판별
    N = N // 2 # 2로 나눈 몫
    if m == 0: # 짝수면
        N -= 1 # N에 1을 빼고
        result = '7'+ result # 7을 왼쪽에 더하기
    else: #홀수면
        result = '4'+ result # 4를 오른쪽에 더하기
print(result)
