n = int(input())
histogram = list(map(int, input().split()))
lengthOfStair = 0
result = 0
for x in histogram:
    lengthOfStair = lengthOfStair+1 if lengthOfStair+1 <= x else x
    result = max(result, lengthOfStair)
print(result)