def solution(citations):
    answer = 0
    n=len(citations)
    citations=sorted(citations,reverse=True)
    for i in range(n):
        # citations[i]번 이상 인용된 횟수가 i+1번
        # citations[i+1]번 이상 인용된 횟수가 i+2번
        if citations[i]>=i+1:
            answer=i+1
        else:
            break

    return answer