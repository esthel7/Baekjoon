import heapq

def solution(scoville, K):
    answer = 0
    if len(scoville)==0:
        return 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0]>=K:
            return answer
        if len(scoville)<2:
            return -1
        answer+=1
        f=heapq.heappop(scoville)
        s=heapq.heappop(scoville)
        new=f+s*2
        heapq.heappush(scoville,new)