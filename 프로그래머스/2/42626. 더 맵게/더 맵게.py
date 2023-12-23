import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        f=heapq.heappop(scoville)
        if f>=K:
            break
        if len(scoville)==0:
            answer=-1
            break
        s=heapq.heappop(scoville)
        heapq.heappush(scoville,f+s*2)
        answer+=1
    return answer