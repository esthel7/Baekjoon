n, k = map(int, input().split())
array = [0] * 1000002 # 1 ~ 100001 까지 저장 

for i in range(n):
    a, b = map(int, input().split())
    array[a+1] += 1
    array[b+1] -= 1

for i in range(1, 1000002):
    array[i] += array[i-1]

flag = False
left = 0
right = 0
t = 0
while True:
    if t < k:
        right += 1
        t += array[right]
    elif t > k:
        left += 1
        t -= array[left]
    else:
        flag = True
        break
    if right == 1000001:
        break
    
if flag:
    print(left, right)
else:
    print(0, 0)