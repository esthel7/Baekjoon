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
  const loc=1
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
  const [N,M]=input[iter++].split(' ').map(item=>Number(item))
  const b=[]
  const l=[]
  for(let i=0;i<N;i++){
    b.push(input[iter++].split('').map(item=>Number(item)))
    l.push([...b[i]])
  }
  
  const visit=[...new Array(N)].map(item=>[...new Array(M)].map(item=>false))
  const xbox=[-1,1,0,0]
  const ybox=[0,0,-1,1]
  let plus=[]

  function find(x,y){
    let cnt=1
    const q=[[x,y]]
    while(q.length>0){
      const [x,y]=q.shift()
      for(let i=0;i<4;i++){
        const newX=x+xbox[i]
        const newY=y+ybox[i]
        if (0<=newX && newX<N && 0<=newY && newY<M){
          if (visit[newX][newY]) continue
          visit[newX][newY]=true
          if (b[newX][newY]===0) {
            cnt+=1
            q.push([newX,newY])
          } else {
            plus.push([newX,newY])
          }
        }
      }
    }
    return cnt
  }

  for(let i=0;i<N;i++){
    for(let j=0;j<M;j++){
      if (visit[i][j]||b[i][j]===1) continue
      visit[i][j]=true
      plus=[]
      const cnt=find(i,j)
      // console.log('start',i,j,cnt,plus)
      for(let k=0;k<plus.length;k++){
        const [px,py]=plus[k]
        visit[px][py]=false
        l[px][py]+=cnt
        l[px][py]%=10
      }
    }
  }
  
  const answer=[]
  for(let i=0;i<N;i++){
    answer.push(l[i].map(item=>String(item)).join(''))
  }
  console.log(answer.join('\n'))
  process.exit()
})
