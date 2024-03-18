import sys
input=sys.stdin.readline

N,M,L,K=map(int,input().split())

Max=0
star=[]
for _ in range(K):
  star.append(list(map(int,input().split())))

Max=0
for fx,fy in star:
  for sx,sy in star:
    if -L<=fx-sx<=L and -L<=fy-sy<=L:
      cnt=0
      x=min(fx,sx)
      y=min(fy,sy)
      for tx,ty in star:
        if x<=tx<=x+L and y<=ty<=y+L:
          cnt+=1
      if Max<cnt:
        Max=cnt
    else:
      continue

print(K-Max)
