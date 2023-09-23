def solution(citations):
    total=len(citations)
    maxNum=-1
    for i in range(max(citations)+1):
        up=0
        down=0
        for j in range(total):
            if citations[j]>=i:
                up+=1
            else:
                down+=1
        if up>=i:
            maxNum=i
    return maxNum