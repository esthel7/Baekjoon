import sys
input=sys.stdin.readline

def find(i,num):
  while i<Len:
    if i+1<Len and S[i+1]=='(':
      tmp=int(S[i])
      [plus,i]=find(i+2,0)
      num+=tmp*plus
    elif S[i]==')':
      return [num,i]
    else:
      num+=1
    i+=1
  print(num)

S=list(input().rstrip())
Len=len(S)

find(0,0)

# 33(562(71(9)))
# 33(562(79))
# 33(567979)
# 3567979567979567979

# 3 / 3(562(71(9)))
