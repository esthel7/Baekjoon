n=int(input())
num=[0 for i in range(10)]
prev=1
for i in range(n):
  if i==0:
    for j in range(1,10):
      num[j]=1
  else:
    newNum=list(num)
    for j in range(10):
      if j==0:
        num[j]=newNum[j+1]
      elif j==9:
        num[j]=newNum[j-1]
      else:
        num[j]=newNum[j-1]+newNum[j+1]

total=0
for i in range(10):
  total+=num[i]
print(total%1000000000)
