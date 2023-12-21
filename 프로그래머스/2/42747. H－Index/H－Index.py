def solution(citations):
    answer = 0
    citations=sorted(citations,reverse=True)
    for i in range(len(citations)):
        if citations[i]==i+1:
            return citations[i]
        if citations[i]<i+1:
            return i
    return len(citations)