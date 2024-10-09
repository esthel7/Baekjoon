import sys
input=sys.stdin.readline

Min,Max=map(int,input().split())
remain=[1 for i in range(Max-Min+1)]
Last=int(Max**(0.5))+1

for i in range(2,Last):
  if i<Min or (i>=Min and remain[i-Min]==1):
    square=i*i
    if Min%square!=0:
      cnt=Min//square+1
    else:
      cnt=Min//square

    while True:
      value=square*cnt
      if value>Max:
        break
      remain[value-Min]=0
      cnt+=1

print(sum(remain))
