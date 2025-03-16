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
    const right=loc*2+1
    if (left>=last) break
    else if (right>=last){
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
  const N=Number(input[iter++])
  const board=[...new Array(501)].map(item=>[...new Array(501)].map(item=>0))
  for(let i=0;i<N;i++){
    let [x1,y1,x2,y2]=input[iter++].split(' ').map(item=>Number(item))
    if (x1>x2){
      let cnt=x1
      x1=x2
      x2=cnt
    }
    if (y1>y2){
      let cnt=y1
      y1=y2
      y2=cnt
    }
    for(let x=x1;x<=x2;x++){
      if (x>500) break
      for(let y=y1;y<=y2;y++){
        if (y>500) break
        board[x][y]=1
      }
    }
  }
  const M=Number(input[iter++])
  for(let i=0;i<M;i++){
    let [x1,y1,x2,y2]=input[iter++].split(' ').map(item=>Number(item))
    if (x1>x2){
      let cnt=x1
      x1=x2
      x2=cnt
    }
    if (y1>y2){
      let cnt=y1
      y1=y2
      y2=cnt
    }
    for(let x=x1;x<=x2;x++){
      if (x>500) break
      for(let y=y1;y<=y2;y++){
        if (y>500) break
        board[x][y]=2
      }
    }
  }

  function newMove(x,y,newX,newY){
    if (board[newX][newY]===0){
      l[newX][newY]=l[x][y]
      return true
    }
    else if (board[newX][newY]===1){
      if (l[newX][newY]===l[x][y]-1) return false
      l[newX][newY]=l[x][y]-1
      return true
    }
    return false
  }

  const l=[...new Array(501)].map(item=>[...new Array(501)].map(item=>-2500))
  l[0][0]=0
  const q=[0,[0,0,0]]
  while(q.length>1){
    let [now,x,y]=heappop(q)
    // console.log(x,y,'now',now)
    if (x===500&&y===500){
      if (now===0) console.log(0)
      else console.log(now)
      process.exit()
    }
    now*=(-1)
    if (x+1<=500&&l[x+1][y]<l[x][y]) {
      if (newMove(x,y,x+1,y)) heappush(q,[-1*l[x+1][y],x+1,y])
    }
    if (x-1>=0&&l[x-1][y]<l[x][y]) {
      if (newMove(x,y,x-1,y)) heappush(q,[-1*l[x-1][y],x-1,y])
    }
    if (y+1<=500&&l[x][y+1]<l[x][y]) {
      if (newMove(x,y,x,y+1)) heappush(q,[-1*l[x][y+1],x,y+1])
    }
    if (y-1>=0&&l[x][y-1]<l[x][y]) {
      if (newMove(x,y,x,y-1)) heappush(q,[-1*l[x][y-1],x,y-1])
    }
  }

  console.log(-1)
  process.exit()
})
