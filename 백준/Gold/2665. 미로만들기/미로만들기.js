const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function isSmall(a,b){
  if (a[0]<b[0]) return true
  return false
}

function heappush(q,item){
  q.push(item)
  let loc=q.length-1
  while(loc>1){
    const parent=Math.floor(loc/2)
    if (isSmall(q[loc],q[parent])){
      [q[loc],q[parent]]=[q[parent],q[loc]]
      loc=parent
    } else break
  }
}

function heappop(q){
  const value=q[1]
  if (q.length===2){
    q.pop()
    return value
  }
  q.splice(1,1,q.pop())
  let loc=1
  const last=q.length-1
  while(loc<last){
    const left=loc*2
    const right=left+1
    if (left>last) break
    else if (right>last){
      if (isSmall(q[left],q[loc])){
        [q[loc],q[left]]=[q[left],q[loc]]
      }
      break
    } else {
      const Min=isSmall(q[left],q[right])?left:right
      if (isSmall(q[Min],q[loc])){
        [q[loc],q[Min]]=[q[Min],q[loc]]
        loc=Min
      } else break
    }
  }
  return value
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const n=Number(input[iter++])
  const board=[]
  for(let i=0;i<n;i++){
    board.push(input[iter++].split(''))
  }

  const l=[...new Array(n)].map(item=>[...new Array(n)].map(item=>[false,0]))
  l[0][0]=[true,0]
  const xbox=[-1,1,0,0]
  const ybox=[0,0,-1,1]
  const q=[0,[0,0,0]]
  while(q.length>1){
    const [cnt,x,y]=heappop(q)
    if (l[x][y][1]!==cnt) continue
    if (x===n-1 && y===n-1){
      console.log(cnt)
      break
    }
    for(let i=0;i<4;i++){
      const newX=x+xbox[i]
      const newY=y+ybox[i]
      if (0<=newX && newX<n && 0<=newY && newY<n){
        const plus=board[newX][newY]==='0'?1:0
        if (!l[newX][newY][0]) l[newX][newY]=[true,cnt+plus]
        else if (l[newX][newY][1]>cnt+plus) l[newX][newY][1]=cnt+plus
        else continue
        heappush(q,[cnt+plus,newX,newY])
      }
    }
  }

  process.exit()
})
