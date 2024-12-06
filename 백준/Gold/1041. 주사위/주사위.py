import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

if N==1:
  print(sum(l)-max(l))
  exit()

value=[min(l)]

# 3개면 4개, 2개면 n*8-8 1개면 n*n*6-(n+n-1+n-1)*6=(n*n-3*n-2)*6
# a 0, b 1, c 2, d 3, e 4, f 5

# 2side
# ab,ac,ad,ae,bc,bd,bf,ce,cf,de,df,ef
value.append(min(l[0]+l[1],l[0]+l[2],l[0]+l[3],l[0]+l[4],l[1]+l[2],l[1]+l[3],l[1]+l[5],l[2]+l[4],l[2]+l[5],l[3]+l[4],l[3]+l[5],l[4]+l[5]))

# 3side
# abc, abd, ace, ade, bcf, bdf, cef, def
value.append(min(l[0]+l[1]+l[2],l[0]+l[1]+l[3],l[0]+l[2]+l[4],l[0]+l[3]+l[4],l[1]+l[2]+l[5],l[1]+l[3]+l[5],l[2]+l[4]+l[5],l[3]+l[4]+l[5]))

print(value[0]*(N*N-4*N+4+4*(N*N-3*N+2))+value[1]*(N*4-8+(N*2-2)*2)+value[2]*4)
