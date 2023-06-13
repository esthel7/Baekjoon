def solution(price, money, count):
    answer = -1
    total=0
    for i in range(count):
        newPrice=price*(i+1)
        total+=newPrice
    if total<=money:
        answer=0
    else:
        answer=total-money
    return answer