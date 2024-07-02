import sys
input=sys.stdin.readline

l=[]
for _ in range(5):
  now=input().rstrip().split()
  l.append([int(now[1]),now[0]])

l.sort()

# 1
diff=False
for i in range(1,5):
  if l[i][1]==l[i-1][1] and l[i][0]-1==l[i-1][0]:
    continue
  diff=True
  break

if not diff:
  print(900+l[4][0])
  exit(0)

# 2
if (l[0][0]==l[3][0] and l[4][0]!=l[3][0]) or (l[1][0]==l[4][0] and l[0][0]!=l[1][0]):
  print(l[1][0]+800)
  exit(0)

# 3
if l[0][0]==l[2][0] and l[3][0]==l[4][0]:
  print(l[0][0]*10+l[4][0]+700)
  exit(0)

if l[0][0]==l[1][0] and l[2][0]==l[4][0]:
  print(l[4][0]*10+l[0][0]+700)
  exit(0)

# 4
color=l[0][1]
diff=False
for i in range(1,5):
  if color==l[i][1]:
    continue
  diff=True
  break

if not diff:
  print(l[4][0]+600)
  exit(0)

# 5
start=l[0][0]
diff=False
for i in range(1,5):
  if start+1==l[i][0]:
    start=l[i][0]
    continue
  diff=True
  break

if not diff:
  print(l[4][0]+500)
  exit(0)

# 6
for i in range(3):
  if l[i][0]==l[i+2][0]:
    print(l[i][0]+400)
    exit(0)

# 7
for i in range(2):
  if l[i][0]==l[i+1][0]:
    for j in range(i+2,4):
      if l[j][0]==l[j+1][0]:
        print(l[j][0]*10+l[i][0]+300)
        exit(0)

# 8
for i in range(4):
  if l[i][0]==l[i+1][0]:
    print(l[i][0]+200)
    exit(0)

# 9
print(l[4][0]+100)
