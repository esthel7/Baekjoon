def run(a):
    if a==1:
        return -1
    for i in range(1,a//2+1):
        if a%i==0 and i*i==a:
            return (-1)*a
    return a

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer+=run(i)
    return answer