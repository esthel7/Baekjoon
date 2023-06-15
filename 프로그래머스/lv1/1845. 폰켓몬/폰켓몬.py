def solution(nums):
    answer = 0
    N=len(nums)
    nums=list(set(nums))
    afterN=len(nums)
    if afterN>=N//2:
        answer=N//2
    else:
        answer=afterN
    return answer