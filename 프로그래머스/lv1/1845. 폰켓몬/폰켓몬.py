def solution(nums):
    answer = 0
    total=len(nums)
    nums=list(set(nums))
    if total//2<len(nums):
        return total//2
    else:
        return len(nums)
    # return answer