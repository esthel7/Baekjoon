def solution(price, money, count):
    answer = 0
    total=0
    for i in range(count):
        total+=price*(i+1)
    if money<total:
        answer=total-money
    return answer