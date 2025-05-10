d,n = map(int,input().split())
data = list(map(int,input().split()))
pizza = list(map(int,input().split()))
oven = [data[0]]
for i in range(1, len(data)):
    if data[i] > oven[i-1]:
        oven.append(oven[i-1])
    else:
        oven.append(data[i])

pidx = 0
i = d - 1
while i >= 0:
    if pizza[pidx] <= oven[i]:
        pidx += 1
        if pidx == n:
            break
    i -= 1

if pidx < n:
    print(0)
else:
    print(i + 1)