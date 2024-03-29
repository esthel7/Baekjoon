import sys
input=sys.stdin.readline

def find(cnto,cntx,dot):
  # 연결이 되어 끝나거나 다 차서 끝나거나
  # 같으면 o가 연결, 다르면 x가 연결
  answer=False

  for i in range(3):
    first=l[i][0]
    if first=='.':
      continue
    oneline=True
    for j in range(1,3):
      if first!=l[i][j]:
        oneline=False
        break
    if oneline:
      if (cnto==cntx and first=='X') or (cnto+1==cntx and first=='O'):
        print('invalid')
        return
      answer=True

  for i in range(3):
    first=l[0][i]
    if first=='.':
      continue
    oneline=True
    for j in range(1,3):
      if first!=l[j][i]:
        oneline=False
        break
    if oneline:
      if (cnto==cntx and first=='X') or (cnto+1==cntx and first=='O'):
        print('invalid')
        return
      answer=True

  if l[0][0]==l[1][1]==l[2][2]:
    if (cnto==cntx and l[0][0]=='X') or (cnto+1==cntx and l[0][0]=='O'):
      print('invalid')
      return
    if l[0][0]!='.':
      answer=True
  if l[0][2]==l[1][1]==l[2][0]:
    if (cnto==cntx and l[0][2]=='X') or (cnto+1==cntx and l[0][2]=='O'):
      print('invalid')
      return
    if l[0][2]!='.':
      answer=True

  if not answer and dot: # 연결 안되었는데 끝남
    print('invalid')
    return
  print('valid')


while True:
  now=input().rstrip()
  if now=='end':
    break
  l=[]
  cntx=0
  cnto=0
  dot=False
  for j in range(3):
    l.append([])
    for k in range(3):
      if now[j*3+k]=='O':
        cnto+=1
      elif now[j*3+k]=='X':
        cntx+=1
      else:
        dot=True
      l[j].append(now[j*3+k])
  if (cnto!=cntx and cnto+1!=cntx) or cnto==cntx==0:
    print('invalid')
  else:
    find(cnto,cntx,dot)


