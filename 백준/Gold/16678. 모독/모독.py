N = int(input())
honors = []
for _ in range(N):
    honors.append(int(input()))

max_honor = 1
action = 0

for num in sorted(honors): #정렬 먼저
    if num >= max_honor: 
        action += num - max_honor
        max_honor += 1

print(action)