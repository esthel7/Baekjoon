def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        minLen=min(len(phone_book[i]),len(phone_book[i+1]))
        if phone_book[i][0:minLen]==phone_book[i+1][0:minLen]:
            return False
    return answer